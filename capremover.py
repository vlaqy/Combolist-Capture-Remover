with open("combolist.txt", "r") as input_file:
    lines = input_file.readlines()

results = []
for line in lines:
    parts = line.split(':')
    email = parts[0]
    password = parts[1].split(' ')[0]
    result = f"{email}:{password}\n"
    results.append(result)

with open("combolistNOCAP.txt", "w") as output_file:
    output_file.writelines(results)
