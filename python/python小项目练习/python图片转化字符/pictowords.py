from PIL import Image


ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")


IMG = "ddd.jpg"
WIDTH = 300
HEIGHT = 300
OUTPUT = "output.txt"

def get_char(r,g,b,alpha=256):
	if alpha == 0:
		return ' '

	length = len(ascii_char)
	gray = int(0.2126*r+0.7152*g+0.0722*b)
	unit = (256.0 + 1)/length
	return ascii_char[int(gray/unit)]


if __name__ == "__main__":
	im = Image.open(IMG)
	im = im.resize((WIDTH,HEIGHT),Image.NEAREST)
	txt = ""
	for i in range(HEIGHT):
		for j in range(WIDTH):
			txt = txt + get_char(*im.getpixel((j,i)))
		txt = txt + '\n'
	print(txt)

	if OUTPUT:
		with open(OUTPUT,'w') as f:
			f.write(txt)
	else:
		with open("output.txt","w") as f:
			f.write(txt)

