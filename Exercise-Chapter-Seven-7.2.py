
file_name = raw_input("Enter the file name:\n")
file_hand = open(file_name,'r')
counter = 0
num = 0
avj = 0
for line in file_hand:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence: 0.8475"):
        continue
    counter = counter + 1
    num = num + float(line[20:])
    avj = num / counter
print("Average spam confidence:" , avj)
