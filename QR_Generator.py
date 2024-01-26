import segno
import sys
import argparse
import os.path

class QRGenerator:

    default_filename = "QR_code_0"
    parser = argparse.ArgumentParser()

    def create_qr(QR_TEXT):
        return segno.make(QR_TEXT,micro=False)

    @staticmethod
    def save_qr(QR_TEXT, file_name):
        qr = QRGenerator.create_qr(QR_TEXT)
        qr.save(f"{file_name}.png", scale=10)
    @staticmethod
    def save_qr_with_scale(QR_TEXT, file_name, scale):
        qr = QRGenerator.create_qr(QR_TEXT)
        qr.save(f"{file_name}.png", scale=scale)

    def get_filename():

        qr_code_number = 0
        file_name = QRGenerator.default_filename

        while True:
            if( os.path.isfile(f"./{file_name}.png") ):
                qr_code_number = qr_code_number + 1
                file_name = file_name.rsplit('_', maxsplit=1)[0] + '_' + str(qr_code_number)
                continue

            return f"{file_name}"

    def validate(args):
        if(args.QR_TEXT is None):
            QRGenerator.parser.print_help()
            sys.exit(2)

        if(args.filename is None):
            args.filename = QRGenerator.get_filename()


    def get_args():
        

        QRGenerator.parser.add_argument("QR_TEXT",help="Text stored in the QR code")
        QRGenerator.parser.add_argument("--filename","--fn",type=str,help=" Name of the file to be stored (default: QR_code_[N] )")
        QRGenerator.parser.add_argument("--scale","--s",default=10,const=1,nargs="?",type=str,help=" Scale of the QR_CODE (default: 10 )")


        try:
            args = QRGenerator.parser.parse_args()
        except:
            args = None

        QRGenerator.validate(args)

        return args





def main():
    args = QRGenerator.get_args()
    QRGenerator.save_qr(args.QR_TEXT,args.filename,args.scale)
    


if __name__ == '__main__':
  main()