from cipher.vigenere import VigenereCipher

#VIGENERE CIPHER ALGORITHM
vigenere_cipher = VigenereCipher()

@app.route("/api2/vigenere/encrypt", methods=["POST"])
def vigenere_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = (data['key'])
    encrypted_text =  vigenere_cipher.vigenere_encrypt(plain_text, key)
    return jsonify ({'encrypted_text': encrypted_text})

@app.route("/api2/vigenere/decrypt", methods=["POST"])
def vigenere_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = (data['key'])
    decrypted_text =  vigenere_cipher.vigenere_decrypt(cipher_text, key)
    return jsonify ({'encrypted_text': decrypted_text})
    