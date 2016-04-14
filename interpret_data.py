#!/usr/bin/python3
import json
import io
d = {}
count = 0
token_set = set()
with open("training_set") as f:
    for line in f.readlines():
        tokens =  [item for x in line.split("|raw ")[1:] for item in x.split() ]
        for token in tokens:
            if token.strip() not in token_set:
                d[token.strip()] = count
                count += 1
                token_set.add(token.strip())
rev_d = {}
for token, count in d.items():
    rev_d[count] = token
with io.open("reverse_hash", "w") as f:
    json.dump(rev_d, f, indent=4, ensure_ascii=False)
model_results = []
with open("wiki_model") as f:
    for i, line in enumerate(f):
        if i > 11:
            model_results.append(line)
unhashed = {}
for result in model_results:
    tokens = result.strip().split(" ")
    # We use a try block here because I had
    # a lot of trouble getting the bit-size
    # exactly right
    try:
        tokens[0] = rev_d[int(tokens[0])]
        parsed_numbers = []
        for token in tokens[1:]:
            parsed_numbers.append(float(token))
        unhashed[tokens[0]] = parsed_numbers
    except KeyError:
        break
for key, values in unhashed.items():
    for value in values:
        if value > 0.5:
            print(key, values)
            break
