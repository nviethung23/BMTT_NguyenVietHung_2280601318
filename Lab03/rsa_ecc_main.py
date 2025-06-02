import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.rsa_ecc import Ui_MainWindow
import requests


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect signals RSA
        self.ui.btn_gen_key_rsa.clicked.connect(self.call_api_gen_key_rsa)
        self.ui.btn_sign_rsa.clicked.connect(self.call_api_sign_rsa)
        self.ui.btn_verify_rsa.clicked.connect(self.call_api_verify_rsa)
        # Connect signals ECC
        self.ui.btn_gen_key_ecc.clicked.connect(self.call_api_gen_key_ecc)
        self.ui.btn_sign_ecc.clicked.connect(self.call_api_sign_ecc)
        self.ui.btn_verify_ecc.clicked.connect(self.call_api_verify_ecc)

    # ================= RSA ==================
    def call_api_gen_key_rsa(self):
        url = "http://127.0.0.1:5000/api/rsa/generate_keys"
        try:
            requests.get(url)
            QMessageBox.information(self, "Thông báo", "Tạo khóa RSA thành công!")
        except Exception as e:
            QMessageBox.warning(self, "Lỗi", str(e))

    def call_api_sign_rsa(self):
        url = "http://127.0.0.1:5000/api/rsa/sign"
        msg = self.ui.txt_message.toPlainText()
        payload = {"message": msg}
        try:
            res = requests.post(url, json=payload)
            if res.status_code == 200:
                self.ui.txt_signature.setText(res.json()["signature"])
                QMessageBox.information(self, "Thông báo", "Ký số RSA thành công!")
            else:
                QMessageBox.warning(self, "Lỗi", res.text)
        except Exception as e:
            QMessageBox.warning(self, "Lỗi", str(e))

    def call_api_verify_rsa(self):
        url = "http://127.0.0.1:5000/api/rsa/verify"
        msg = self.ui.txt_message.toPlainText()
        sign = self.ui.txt_signature.toPlainText()
        payload = {"message": msg, "signature": sign}
        try:
            res = requests.post(url, json=payload)
            if res.status_code == 200:
                ok = res.json()["is_verified"]
                if ok:
                    QMessageBox.information(self, "Kết quả xác minh RSA", "Chữ ký hợp lệ (RSA)")
                else:
                    QMessageBox.warning(self, "Kết quả xác minh RSA", "Chữ ký không hợp lệ (RSA)")
            else:
                QMessageBox.warning(self, "Lỗi", res.text)
        except Exception as e:
            QMessageBox.warning(self, "Lỗi", str(e))

    # ================= ECC ==================
    def call_api_gen_key_ecc(self):
        url = "http://127.0.0.1:5000/api/ecc/generate_keys"
        try:
            requests.get(url)
            QMessageBox.information(self, "Thông báo", "Tạo khóa ECC thành công!")
        except Exception as e:
            QMessageBox.warning(self, "Lỗi", str(e))

    def call_api_sign_ecc(self):
        url = "http://127.0.0.1:5000/api/ecc/sign"
        msg = self.ui.txt_message.toPlainText()
        payload = {"message": msg}
        try:
            res = requests.post(url, json=payload)
            if res.status_code == 200:
                self.ui.txt_signature.setText(res.json()["signature"])
                QMessageBox.information(self, "Thông báo", "Ký số ECC thành công!")
            else:
                QMessageBox.warning(self, "Lỗi", res.text)
        except Exception as e:
            QMessageBox.warning(self, "Lỗi", str(e))

    def call_api_verify_ecc(self):
        url = "http://127.0.0.1:5000/api/ecc/verify"
        msg = self.ui.txt_message.toPlainText()
        sign = self.ui.txt_signature.toPlainText()
        payload = {"message": msg, "signature": sign}
        try:
            res = requests.post(url, json=payload)
            if res.status_code == 200:
                ok = res.json()["is_verified"]
                if ok:
                    QMessageBox.information(self, "Kết quả xác minh ECC", "Chữ ký hợp lệ (ECC)")
                else:
                    QMessageBox.warning(self, "Kết quả xác minh ECC", "Chữ ký không hợp lệ (ECC)")
            else:
                QMessageBox.warning(self, "Lỗi", res.text)
        except Exception as e:
            QMessageBox.warning(self, "Lỗi", str(e))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
