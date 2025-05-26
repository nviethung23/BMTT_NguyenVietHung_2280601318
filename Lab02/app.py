from flask import Flask, render_template, request
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayFairCipher
from cipher.transposition import TranspositionCipher

app = Flask(__name__)

caesar = CaesarCipher()
vigenere = VigenereCipher()
railfence = RailFenceCipher()
playfair = PlayFairCipher()
trans = TranspositionCipher()

@app.route("/")
def home():
    return render_template("index.html")

# ---------------- CAESAR ----------------
@app.route("/caesar", methods=["GET", "POST"])
def caesar_page():
    result = None
    mode = None
    if request.method == "POST":
        if 'inputPlainText' in request.form:
            result = caesar.encrypt_text(request.form['inputPlainText'], int(request.form['inputKeyPlain']))
            mode = 'encrypt'
        elif 'inputCipherText' in request.form:
            result = caesar.decrypt_text(request.form['inputCipherText'], int(request.form['inputKeyCipher']))
            mode = 'decrypt'
    return render_template("caesar.html", result=result, mode=mode)

# ---------------- VIGENERE ----------------
@app.route("/vigenere", methods=["GET", "POST"])
def vigenere_page():
    result = None
    mode = None
    if request.method == "POST":
        if 'inputPlainText' in request.form:
            result = vigenere.vigenere_encrypt(request.form['inputPlainText'], request.form['inputKeyPlain'])
            mode = 'encrypt'
        elif 'inputCipherText' in request.form:
            result = vigenere.vigenere_decrypt(request.form['inputCipherText'], request.form['inputKeyCipher'])
            mode = 'decrypt'
    return render_template("vigenere.html", result=result, mode=mode)

# ---------------- RAIL FENCE ----------------
@app.route("/railfence", methods=["GET", "POST"])
def railfence_page():
    result = None
    mode = None
    if request.method == "POST":
        if 'inputPlainText' in request.form:
            result = railfence.rail_fence_encrypt(request.form['inputPlainText'], int(request.form['inputKeyPlain']))
            mode = 'encrypt'
        elif 'inputCipherText' in request.form:
            result = railfence.rail_fence_decrypt(request.form['inputCipherText'], int(request.form['inputKeyCipher']))
            mode = 'decrypt'
    return render_template("railfence.html", result=result, mode=mode)

# ---------------- PLAYFAIR ----------------
@app.route("/playfair", methods=["GET", "POST"])
def playfair_page():
    result = None
    mode = None
    if request.method == "POST":
        if 'inputPlainText' in request.form:
            matrix = playfair.create_playfair_matrix(request.form['inputKeyPlain'])
            result = playfair.playfair_encrypt(request.form['inputPlainText'], matrix)
            mode = 'encrypt'
        elif 'inputCipherText' in request.form:
            matrix = playfair.create_playfair_matrix(request.form['inputKeyCipher'])
            result = playfair.playfair_decrypt(request.form['inputCipherText'], matrix)
            mode = 'decrypt'
    return render_template("playfair.html", result=result, mode=mode)

# ---------------- TRANSPOSITION ----------------
@app.route("/transposition", methods=["GET", "POST"])
def transposition_page():
    result = None
    mode = None
    if request.method == "POST":
        if 'inputPlainText' in request.form:
            result = trans.encrypt(request.form['inputPlainText'], int(request.form['inputKeyPlain']))
            mode = 'encrypt'
        elif 'inputCipherText' in request.form:
            result = trans.decrypt(request.form['inputCipherText'], int(request.form['inputKeyCipher']))
            mode = 'decrypt'
    return render_template("transposition.html", result=result, mode=mode)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
