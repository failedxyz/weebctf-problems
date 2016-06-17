from PIL import Image

text = """He's climbin' in your Windows
He's snatchin' your secrets up
Tryna' steal em' so y'all need to

Hide your flags, hide your waifus
Hide your flags, hide your waifus
weeb{Hide_your_flags,_hide_your_waifus}
and hide your password
Cuz' they're stealin errthing out there

You don't have to come and confess
We're lookin' for you
We gon' find you
We gon' find you"""

im = Image.open("sos_original.png")
w, h = im.size
data = im.load()

for i in range(len(text)):
	(x, y) = i % w, i // w
	A = ord(text[i])
	r, g, b, a = data[x, y]
	B = r
	C = A ^ B
	im.putpixel((x, y), (C, g, b))

im = im.transpose(Image.FLIP_LEFT_RIGHT)
im.save("sos_logo.png", "PNG")