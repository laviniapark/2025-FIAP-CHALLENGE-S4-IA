from flask import Flask, request, jsonify
import numpy as np
import cv2
import pytesseract

app = Flask(__name__)

custom_config = r"--oem 3 --psm 7 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

@app.route("/upload", methods=["POST"])
def upload():
    if "image" not in request.files:
        return jsonify({"error": "nenhuma imagem enviada"}), 400

    file = request.files["image"]
    img_bytes = file.read()

    nparr = np.frombuffer(img_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.bilateralFilter(gray, 11, 17, 17)
    edged = cv2.Canny(gray, 30, 200)

    texto = pytesseract.image_to_string(gray, config=custom_config)

    placa = ''.join(c for c in texto if c.isalnum()).upper()

    if len(placa) >= 7:
        placa = placa[:7]

    return jsonify({"plate": placa})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
