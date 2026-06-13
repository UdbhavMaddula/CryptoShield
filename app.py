import streamlit as st
import base64
import hashlib

from Crypto.Cipher import AES, DES
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


st.set_page_config(
    page_title="CryptoShield",
    page_icon="🛡️",
    layout="centered"
)


# ----------------------------- Helpers -----------------------------

def normalize_key(user_key):
    return hashlib.sha256(user_key.encode()).digest()


def normalize_des_key(user_key):
    """Converts user input into an 8-byte DES key. Educational use only."""
    return hashlib.md5(user_key.encode()).digest()[:8]


def encrypt_aes(plaintext, user_key):
    key = normalize_key(user_key)
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_data = pad(plaintext.encode(), AES.block_size)
    ciphertext = cipher.encrypt(padded_data)
    combined = iv + ciphertext
    encoded = base64.b64encode(combined).decode()

    return {
        "algorithm": "AES-256 CBC",
        "iv": iv.hex(),
        "ciphertext": encoded
    }


def decrypt_aes(encoded_ciphertext, user_key):
    try:
        combined = base64.b64decode(encoded_ciphertext)
        iv = combined[:16]
        ciphertext = combined[16:]
        key = normalize_key(user_key)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        padded_plaintext = cipher.decrypt(ciphertext)
        plaintext = unpad(padded_plaintext, AES.block_size).decode()

        return {"success": True, "plaintext": plaintext}

    except Exception:
        return {"success": False, "error": "Invalid key or corrupted ciphertext."}


def encrypt_des(plaintext, user_key):
    key = normalize_des_key(user_key)
    iv = get_random_bytes(8)
    cipher = DES.new(key, DES.MODE_CBC, iv)
    padded_data = pad(plaintext.encode(), DES.block_size)
    ciphertext = cipher.encrypt(padded_data)
    combined = iv + ciphertext
    encoded = base64.b64encode(combined).decode()

    return {
        "algorithm": "DES CBC",
        "iv": iv.hex(),
        "ciphertext": encoded
    }


def decrypt_des(encoded_ciphertext, user_key):
    try:
        combined = base64.b64decode(encoded_ciphertext)
        iv = combined[:8]
        ciphertext = combined[8:]
        key = normalize_des_key(user_key)
        cipher = DES.new(key, DES.MODE_CBC, iv)
        padded_plaintext = cipher.decrypt(ciphertext)
        plaintext = unpad(padded_plaintext, DES.block_size).decode()

        return {"success": True, "plaintext": plaintext}

    except Exception:
        return {"success": False, "error": "Invalid key or corrupted ciphertext."}


def generate_rsa_keys():
    key = RSA.generate(2048)
    return {
        "private_key": key.export_key().decode(),
        "public_key": key.publickey().export_key().decode()
    }


def encrypt_rsa(plaintext, public_key_text):
    try:
        public_key = RSA.import_key(public_key_text)
        cipher = PKCS1_OAEP.new(public_key)
        ciphertext = cipher.encrypt(plaintext.encode())
        encoded = base64.b64encode(ciphertext).decode()
        return {"success": True, "ciphertext": encoded}

    except Exception:
        return {"success": False, "error": "Invalid public key, or plaintext too long for this key size."}


def decrypt_rsa(encoded_ciphertext, private_key_text):
    try:
        private_key = RSA.import_key(private_key_text)
        cipher = PKCS1_OAEP.new(private_key)
        ciphertext = base64.b64decode(encoded_ciphertext)
        plaintext = cipher.decrypt(ciphertext).decode()
        return {"success": True, "plaintext": plaintext}

    except Exception:
        return {"success": False, "error": "Invalid private key or corrupted ciphertext."}


# ----------------------------- UI -----------------------------

st.title("🛡️ CryptoShield")
st.caption("AES, DES & RSA Encryption Playground — Learn How Encryption Works")

st.write(
    "Explore symmetric (AES, DES) and asymmetric (RSA) encryption by "
    "encrypting and decrypting text directly in your browser."
)

algorithm = st.selectbox(
    "Choose Algorithm",
    ["AES-256 (Recommended)", "DES (Legacy)", "RSA (Asymmetric)"]
)

st.divider()

# ----------------------------- RSA -----------------------------
if "RSA" in algorithm:

    st.subheader("🔑 RSA Key Generation")

    st.info(
        "RSA uses two keys:\n\n"
        "🔓 **Public Key** — used for encryption.\n\n"
        "🔐 **Private Key** — used for decryption.\n\n"
        "This concept forms the basis of HTTPS, digital certificates, "
        "and secure communication."
    )

    if "rsa_keys" not in st.session_state:
        st.session_state.rsa_keys = None

    if st.button("Generate RSA Key Pair"):
        st.session_state.rsa_keys = generate_rsa_keys()

    if st.session_state.rsa_keys:
        st.success("RSA Key Pair Generated Successfully!")

        with st.expander("View Generated Keys"):
            st.subheader("Public Key")
            st.code(st.session_state.rsa_keys["public_key"])

            st.subheader("Private Key")
            st.code(st.session_state.rsa_keys["private_key"])

    tab_encrypt, tab_decrypt = st.tabs(["🔐 Encrypt", "🔓 Decrypt"])

    with tab_encrypt:
        st.subheader("RSA Encryption")

        rsa_text = st.text_area("Enter Plaintext", key="rsa_plain")

        public_key_input = st.text_area(
            "Public Key",
            value=(
                st.session_state.rsa_keys["public_key"]
                if st.session_state.rsa_keys else ""
            ),
            height=150,
            key="rsa_pub_key"
        )

        if st.button("Encrypt using RSA"):
            if rsa_text and public_key_input:
                result = encrypt_rsa(rsa_text, public_key_input)

                if result["success"]:
                    st.success("RSA Encryption Successful!")
                    st.subheader("Ciphertext")
                    st.code(result["ciphertext"])
                else:
                    st.error(result["error"])
            else:
                st.warning("Please enter both plaintext and a public key.")

    with tab_decrypt:
        st.subheader("RSA Decryption")

        rsa_ciphertext = st.text_area("Paste Ciphertext", key="rsa_cipher")

        private_key_input = st.text_area(
            "Private Key",
            value=(
                st.session_state.rsa_keys["private_key"]
                if st.session_state.rsa_keys else ""
            ),
            height=150,
            key="rsa_priv_key"
        )

        if st.button("Decrypt using RSA"):
            if rsa_ciphertext and private_key_input:
                result = decrypt_rsa(rsa_ciphertext, private_key_input)

                if result["success"]:
                    st.success("RSA Decryption Successful!")
                    st.subheader("Recovered Plaintext")
                    st.code(result["plaintext"])
                else:
                    st.error(result["error"])
            else:
                st.warning("Please enter ciphertext and a private key.")

    st.divider()
    st.subheader("📘 Educational Insight")
    st.info(
        "RSA is an **asymmetric** algorithm: encryption and decryption use "
        "different keys. It underpins HTTPS, digital signatures, and key "
        "exchange protocols, but is slow for large data — so it's typically "
        "used to encrypt a symmetric key (e.g., AES), not the data itself."
    )

# ----------------------------- AES / DES -----------------------------
else:

    is_aes = "AES" in algorithm

    operation = st.radio("Choose Operation", ["Encrypt", "Decrypt"], horizontal=True)

    text_label = "Enter Plaintext" if operation == "Encrypt" else "Enter Ciphertext (Base64)"
    text = st.text_area(text_label, height=150)

    key = st.text_input("Enter Secret Key", type="password")

    if operation == "Encrypt":
        if st.button("🔐 Encrypt"):
            if text and key:
                result = encrypt_aes(text, key) if is_aes else encrypt_des(text, key)

                st.success("Encryption Successful!")
                st.subheader("Encryption Breakdown")

                st.write(f"**Algorithm:** {result['algorithm']}")
                st.write("**Initialization Vector (IV):**")
                st.code(result["iv"])
                st.write("**Ciphertext (Base64):**")
                st.code(result["ciphertext"])

                if is_aes:
                    st.info(
                        "AES uses symmetric encryption — the same key is used "
                        "for both encryption and decryption."
                    )
                else:
                    st.info(
                        "DES uses symmetric encryption — the same key is used "
                        "for both encryption and decryption. Note: DES is "
                        "insecure and shown here for educational purposes only."
                    )
            else:
                st.warning("Please enter both text and a secret key.")

    else:
        if st.button("🔓 Decrypt"):
            if text and key:
                result = decrypt_aes(text, key) if is_aes else decrypt_des(text, key)

                if result["success"]:
                    st.success("Decryption Successful!")
                    st.subheader("Recovered Plaintext")
                    st.code(result["plaintext"])
                    st.info(
                        f"The original message was recovered using the same "
                        f"{'AES' if is_aes else 'DES'} secret key."
                    )
                else:
                    st.error(result["error"])
            else:
                st.warning("Please enter ciphertext and a secret key.")

    st.divider()
    st.subheader("📘 Educational Insight")

    if is_aes:
        st.info(
            "**AES (Advanced Encryption Standard)** is one of the strongest "
            "symmetric encryption algorithms and is widely used in:\n\n"
            "- WhatsApp\n"
            "- VPNs\n"
            "- Banking Systems\n"
            "- BitLocker\n"
            "- Enterprise Security Solutions\n\n"
            "AES-256 is considered secure for modern applications."
        )
    else:
        st.warning(
            "**⚠️ DES Warning**\n\n"
            "DES (Data Encryption Standard) was once widely used for "
            "protecting sensitive information. It is included in "
            "CryptoShield for educational purposes to demonstrate the "
            "evolution of cryptography.\n\n"
            "**Why is DES insecure today?**\n"
            "- Uses only a 56-bit effective key\n"
            "- Vulnerable to brute-force attacks\n"
            "- Replaced by AES in modern systems\n\n"
            "**Real-world significance:**\n"
            "- Historical banking systems\n"
            "- Early government standards\n"
            "- Cryptography education\n\n"
            "DES should **NOT** be used in production environments."
        )

st.divider()
st.caption("Developed by Udbhav | CryptoShield")