from PIL import Image
import imagehash

substitutions = {
	"0": ["O"],
	"c": ["o"],
	"e": ["o"],
	"l": ["I", "1"],
	"m": ["rn", "n"],
	"t": ["l"],
	"u": ["v"],
	"w": ["vv", "v"],
}

# gets similarity score of between letter substitutions given that their png file exists in text_images/{letter}.png
def get_similarity_score(substitutions):
	scores = {}
	for char in substitutions:
		hash = imagehash.average_hash(Image.open('text_images/{}.png'.format(char)))
		for other_char in substitutions[char]:
			otherhash = imagehash.average_hash(Image.open('text_images/{}.png'.format(other_char)))
			print("score for ", char, " and ", other_char, "is ", abs(hash - otherhash))
			scores[(char, other_char)] = abs(hash - otherhash)
			scores[(other_char, char)] = abs(hash - otherhash)
	max_score = max(scores.values())
	for score in scores:
		# we want to normalize the scores to fit between .5 and 1
		scores[score] = 1 - scores[score]/max_score/2
	return scores
