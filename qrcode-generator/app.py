from re import T
import qrcode
import datetime
repeat = True
while(repeat):
    task = input("What you want to do? (Encode or Decore a QR Code)")
    if (task == 'Encode' or task == 'encode'):
        x = str(datetime.datetime.now())
        x = x.replace(':', "").replace('-', "").replace(' ', "").replace('.', "")
        data = input("Enter the url: ")
        img = qrcode.make(data)
        pathname = "QR"+x
        img.save(pathname + ".png")
    else:
        filename = input("Enter the filname of QR code image(with extension): ")
        import cv2
        d = cv2.QRCodeDetector()
        val, _, _ = d.detectAndDecode(cv2.imread(filename))
        print("Decoded text is: ", val)

    rinput = input("Do you want to repeat it: ")
    if(rinput == "y" or rinput == "yes" or rinput == "Y" or rinput == "YES"):
        repeat = True
    else:
        repeat = False

