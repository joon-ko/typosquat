from PIL import Image, ImageDraw, ImageFont

def draw_text(text, font_size=14, img_filename='test'):
	font = ImageFont.truetype("fonts/Helvetica-Normal.ttf", font_size)
	im = Image.new('RGB', (200, font_size), color=(255, 255, 255))
	draw = ImageDraw.Draw(im)
	draw.text((0, 0), text, font=font, fill=(0, 0, 0, 255))
	im.save("text_images/%s.png" % (img_filename), "PNG")

substitutions = ['e', 'u', 't', 'O', '1', 'rn', 'm', 'l', '0', 'o', 'vv', 'c', 'w', 'I', 'n', 'v']
	
for char in substitutions:
	draw_text(char, img_filename=char)