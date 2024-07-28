# pip install qrcode[pil]
# run this command into your terminal
import qrcode as qr
image = qr.make("https://www.youtube.com/watch?v=9sekgEXGm-E&list=RD9sekgEXGm-E&start_radio=1")
image.save("Fassla.png")