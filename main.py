import qrcode  # import library

input_data = "https://github.com/ShaniaB417"  # name of website

qr = qrcode.QRCode(  # side of qr code box
    version=1,
    box_size=10,
    border=5
)

qr.add_data(input_data)
qr.make(fit=True)

img = qr.make_image(fill="black",
                    back_color="white")         # color of the image
img.save("Shania's GitHub.png")                           # name of saved image

# finished with exit code 0
