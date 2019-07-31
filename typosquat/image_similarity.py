from PIL import Image
import imagehash
from text_to_image import Font
fonts = [Font.HELVETICA, Font.ARIAL, Font.OPEN_SANS, Font.VERDANA]

substitutions = {
	"0": ["O"],
	"c": ["o"],
	"e": ["o"],
	"l": ["I", "1"],
	"m": ["rn", "n"],
	"t": ["l", "f"],
	"u": ["v"],
	"w": ["vv", "v"],
}

# gets similarity score of between letter substitutions given that their png file exists in text_images/{letter}.png
def get_similarity_score(substitutions):
	scores = {}
	for char in substitutions:
		for other_char in substitutions[char]:
			scores[(char, other_char)] = []
			scores[(other_char, char)] = []
			for font in fonts:
				hash = imagehash.average_hash(Image.open('text_images/{}.png'.format(char + str(font))))
				otherhash = imagehash.average_hash(Image.open('text_images/{}.png'.format(other_char + str(font))))
				print("score for ", char, " and ", other_char, "is ", abs(hash - otherhash), " for the font ", font)
				scores[(char, other_char)].append(abs(hash - otherhash))
				scores[(other_char, char)].append(abs(hash - otherhash))
	# average the scores
	for score in scores:
		scores[score] = sum(scores[score])/4
	max_score = max(scores.values())
	for score in scores:
		# we want to normalize the scores to fit between .5 and 1
		scores[score] = 1 - scores[score]/max_score/2
	return scores
print(get_similarity_score(substitutions))