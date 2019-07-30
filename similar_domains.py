def get_similar_domain_names(domain_name):
	# if not check_domain_name_is_vaild(domain_name):
		# return "invalid domain name"
	name, tld = check_domain_name_is_vaild(domain_name)

	substitutions = {
		"0": ["O"],
		"1": ["l"],
		"c": ["o"],
		"e": ["o"],
		"I": ["l"],
		"l": ["I", "1"],
		"m": ["rn", "n"],
		"n": ["m"],
		"o": ["c"],
		"t": ["l"],
		"u": ["v"],
		"v": ["u"],
		"w": ["vv", "v"],
	}
	# compute all relevant substitutions
	similar_domain_names = []
	for key in substitutions.keys():
		for value in substitutions[key]:
			similar_domain_names += find_and_replace_all_occurrences(name, tld, key, value)
	# also: double letters -> single letter
	similar_domain_names += double_to_single_replacements(name, tld)
	return similar_domain_names


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