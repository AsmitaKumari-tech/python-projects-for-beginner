from re import T
import qrcode
import datetime
repeat = True
while(repeat):
    x = str(datetime.datetime.now())
    x = x.replace(':', "").replace('-', "").replace(' ', "").replace('.', "")
    data = input("Enter the url: ")
    img = qrcode.make(data)
    pathname = "QR"+x
    img.save(pathname + ".png")
    rinput = input("Do you want to repeat it: ")
    if(rinput == "y" or rinput == "yes" or rinput == "Y" or rinput == "YES"):
        repeat = True
    else:
        repeat = False
