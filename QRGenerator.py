import segno
import sys

class QRGenerator:

    def create_qr(QR_TEXT):
        return segno.make(QR_TEXT,micro=False)


    def save_qr(QR_TEXT, file_name):
        qr = QRGenerator.create_qr(QR_TEXT)
        qr.save(f"{file_name}.png", scale=10)


def validate():
    return True

def main():

    # Function called without arguments
    if(len(sys.argv) != 3):
        print(f"Usage: Python {sys.argv[0]} <link> <fileName>")
        return
    
    if not validate():
        return print("Erro")

    QRGenerator.save_qr(sys.argv[1],sys.argv[2])
    

main()