from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher
app = Flask(__name__)

#CAESAR CIPHER ALGORITHM
caesar_cipher = CaesarCipher()

@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    data = request.json 
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text =  caesar_cipher.encrypt_text