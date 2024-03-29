import json

scores = {('0', 'O'): 0.5, ('O', '0'): 0.5, ('c', 'o'): 0.8362068965517242, ('o', 'c'): 0.8362068965517242, ('e', 'o'): 0.8793103448275862,
	('o', 'e'): 0.8793103448275862, ('l', 'I'): 0.9094827586206896, ('I', 'l'): 0.9094827586206896, ('l', '1'): 0.7931034482758621,
	('1', 'l'): 0.7931034482758621, ('m', 'rn'): 0.9698275862068966, ('rn', 'm'): 0.9698275862068966, ('m', 'n'): 0.6810344827586207,
	('n', 'm'): 0.6810344827586207, ('t', 'l'): 0.75, ('l', 't'): 0.75, ('t', 'f'): 0.8448275862068966, ('f', 't'): 0.8448275862068966,
	('u', 'v'): 0.8405172413793103, ('v', 'u'): 0.8405172413793103, ('w', 'vv'): 0.896551724137931, ('vv', 'w'): 0.896551724137931,
	('w', 'v'): 0.7241379310344828, ('v', 'w'): 0.7241379310344828}

# Assuming Linux. Word list may also be at /usr/dict/words. 
# If not on Linux, grab yourself an enlish word list and insert here:
words = set(x.strip().lower() for x in open("/usr/share/dict/words").readlines())
words -= set("bcdefghjklmnopqrtvwxyz")
words -= set(("ex", "rs", "ra", "frobnicate"))

common_typos = json.loads(open('typosquat/typos.json').read())

def get_similar_domain_names(domain_name):
	# if not check_domain_name_is_vaild(domain_name):
		# return "invalid domain name"
	name, tld = check_domain_name_is_vaild(domain_name)

	substitutions = {
		"0": ["O"],
		"1": ["l"],
		"c": ["o"],
		"e": ["o"],
		"f": ["t"],
		"I": ["l"],
		"l": ["I", "1"],
		"m": ["rn", "n"],
		"n": ["m"],
		"o": ["c"],
		"t": ["l", "f"],
		"u": ["v"],
		"v": ["u"],
		"w": ["vv", "v"],
	}

	tld_substitutions = {
		"com": ["co"]
	}
	# compute all relevant substitutions
	similar_domain_names = {}
	for key in substitutions.keys():
		for value in substitutions[key]:
			for occurrence in find_and_replace_all_occurrences(name, tld, key, value):
				similar_domain_names[occurrence] = scores[(key, value)]
	# also: double letters -> single letter
	for occurrence in double_to_single_replacements(name, tld):
		similar_domain_names[occurrence] = .5
	
	# common typos
	for occurrence in common_typo_occurrences(name, tld):
		if occurrence in similar_domain_names:
			similar_domain_names[occurrence] += .5
		else:
			similar_domain_names[occurrence] = .5

	# tld substitutions
	if tld in tld_substitutions:
		for sub in tld_substitutions[tld]:
			similar_domain_names[name + "." + sub] = .5
	#return similar_domain_names
	return sorted(similar_domain_names, key=similar_domain_names.get, reverse=True)[:10]


def find_and_replace_all_occurrences(name, tld, prev_substring, new_substring):
	domain_name_list = []
	for i in range(len(name) - len(prev_substring) + 1):
		if name[i:i+len(prev_substring)] == prev_substring:
			# compute new substring
			new_string = name[:i] + new_substring + name[i+len(prev_substring):]
			domain_name_list.append(new_string + "." + tld)
	return domain_name_list


def double_to_single_replacements(name, tld):
	domain_name_list = []
	for i in range(len(name) - 1):
		if name[i] == name[i + 1]:
			new_string = name[:i] + name[i+1:]
			domain_name_list.append(new_string + "." + tld)
	return domain_name_list


def common_typo_occurrences(name, tld):
	
	domain_name_list = []
	split_strings = substrings_in_set(name, words)
	replaced_words = set()

	for list_strings in split_strings:
		for i in range(len(list_strings)):
			if list_strings[i] not in replaced_words and list_strings[i] in common_typos:
				domain_name_list += [''.join(list_strings[:i]) + typo + ''.join(list_strings[i+1:]) + '.' + tld for typo in common_typos[list_strings[i]]]
			replaced_words.add(list_strings[i])
	
	return domain_name_list


def substrings_in_set(s, words):
    if s in words:
        yield [s]
    for i in range(1, len(s)):
        if s[:i] not in words and not s[:i].isdigit():
            continue
        for rest in substrings_in_set(s[i:], words):
            yield [s[:i]] + rest


def check_domain_name_is_vaild(domain_name):
	# returns TLD and name if valid, throws exception? if false
	index = domain_name.find('.')
	if index == -1:
		# assume .com
		name = domain_name
		tld = "com"
	else:
		name = domain_name[:index]
		tld = domain_name[index + 1:]
		if len(tld) == 0 or name == 0:
			raise RuntimeError("domain name or TLD must not be empty")
	# assert name and TLD are alphanumeric
	if not name.isalnum() or not tld.isalnum():
		raise RuntimeError("domain name must be alphanumeric")
	return name, tld
