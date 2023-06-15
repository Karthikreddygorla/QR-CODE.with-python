import qrcode
features=qrcode.QRCode(version=2,box_size=6,border=9)
features.make(fit=True)
img=qrcode.make("https://instagram.com/karthikreddygorla?igshid=YmMyMTA2M2Y=")
img.save("img.png")