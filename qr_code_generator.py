import pyqrcode
qr = pyqrcode.create("https://www.youtube.com/channel/UCkDAMU2uQOKuoUkNK_YY5Dg?view_as=subscriber")
qr.png('abc.png', scale=8)