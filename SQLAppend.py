with open("data.txt", "r") as ins:
    array = []
    for line in ins:
        array.append(line.rstrip('\n'))
    print array