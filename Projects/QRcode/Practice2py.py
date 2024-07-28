import qrcode
from PIL import Image

qr = qrcode.QRCode(version =1,
                   error_correction=qrcode.ERROR_CORRECT_H,
                   box_size=10,
                   border=4,)
qr.add_data('https://www.youtube.com/watch?v=9sekgEXGm-E&list=RD9sekgEXGm-E&start_radio=1')
qr.make(fit=True)
image=qr.make_image(fill_color="red",back_color="blue")
image.save("Song.png")