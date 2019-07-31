import json
file = open('old_typos.json')
file_str = file.read()
data = json.loads(file_str)

new_data = {}
for thing in data:
    correct = thing['correct'].lower()
    typo = thing['typo'].lower()
    if correct != typo:
        if correct not in new_data:
            new_data[correct] = [typo]
        else:
            new_data[correct].append(typo)
with open('typos.json', 'w') as outfile:
    json.dump(new_data, outfile)
