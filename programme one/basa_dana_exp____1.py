FB = open("fill_animals.txt", "r")
Quantity_Animals = dict()
  
for line in FB:
    line = line.strip()
    line = line.lower()
    words = line.split(" ")

    for word in words:

        if word in Quantity_Animals:

            Quantity_Animals[word] = Quantity_Animals[word] + 1

        else:

            Quantity_Animals[word] = 1

for key in list(Quantity_Animals.keys()):

    print(key, ":", Quantity_Animals[key])