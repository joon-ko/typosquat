from PIL import Image, ImageDraw, ImageFont

def draw_text(text, font_size=14, img_filename='test'):
	font = ImageFont.truetype("fonts/Helvetica-Normal.ttf", font_size)
	im = Image.new('RGB', (200, font_size), color=(255, 255, 255))
	draw = ImageDraw.Draw(im)
	draw.text((0, 0), text, font=font, fill=(0, 0, 0, 255))
	im.save("text_images/%s.png" % (img_filename), "PNG")
