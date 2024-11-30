import qrcode #import it by opening the cmd prompt and type"pip install qrcode[pil]".NOTE:-must have python in your system
features=qrcode.QRCode(version=2,box_size=6,border=9)
features.make(fit=True)
img=qrcode.make("https://instagram.com/karthikreddygorla?igshid=YmMyMTA2M2Y=") # put the link which you want to get the QR code
img = qr_code_generator.make_image(fill_color="black", back_color="yellow") #make some style by adding colors
img.save("qr.png") 
