from enum import Enum

from PIL import Image, ImageDraw, ImageFont

class Font(Enum):
	HELVETICA = "fonts/Helvetica.ttf"
	ARIAL = "fonts/Arial.ttf"
	OPEN_SANS = "fonts/OpenSans.ttf"
	VERDANA = "fonts/Verdana.ttf"

def draw_text(text, font=Font.HELVETICA, font_size=100, img_filename='test'):
	font = ImageFont.truetype(font.value, font_size)
	ascent, descent = font.getmetrics()
	(width, baseline), (offset_x, offset_y) = font.font.getsize(text)
	im = Image.new('RGB', (width, ascent - offset_y + descent), color=(255, 255, 255))
	draw = ImageDraw.Draw(im)
	draw.text((0, 0), text, font=font, fill=(0, 0, 0, 255))
	im.save("text_images/%s.png" % (img_filename), "PNG")

substitutions = ['e', 'u', 't', 'O', '1', 'rn', 'm', 'l', '0', 'o', 'vv', 'c', 'w', 'I', 'n', 'v', 'f']

for char in substitutions:
	for font in [Font.HELVETICA, Font.ARIAL, Font.OPEN_SANS, Font.VERDANA]:
		draw_text(char, font=font, img_filename=char+str(font))
