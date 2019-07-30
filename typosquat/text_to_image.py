from enum import Enum

from PIL import Image, ImageDraw, ImageFont

class Font(Enum):
	HELVETICA = "fonts/Helvetica.ttf"
	ARIAL = "fonts/Arial.ttf"
	OPEN_SANS = "fonts/OpenSans.ttf"
	VERDANA = "fonts/Verdana.ttf"

def draw_text(text, font=Font.HELVETICA, font_size=14, img_filename='test'):
	font = ImageFont.truetype(font.value, font_size)
	im = Image.new('RGB', (200, font_size), color=(255, 255, 255))
	draw = ImageDraw.Draw(im)
	draw.text((0, 0), text, font=font, fill=(0, 0, 0, 255))
	im.save("text_images/%s.png" % (img_filename), "PNG")
