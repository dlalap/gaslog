gasFile = open('gasLog.txt')
gasFileRead = gasFile.readlines()
gasFile.close()

print(gasFileRead)

# Initiate Data Read
pumpId = []
mileage = []
date = []
gallons = []
cost = []

cycle = 0
for line in gasFileRead:
	if line != '\n':
		if cycle == 0: # PUMP ID AND MILEAGE
			miSpace = line.find(' ')
			pumpId.append(line[2:miSpace])
			mileage.append(line[miSpace+1:-1])
		if cycle == 1:	# DATE
			firstSlash = line.find('/')
			secondSlash = line.find('/',firstSlash+1)
			date.append('20'+line[secondSlash+1:-1]+'-'+line[:firstSlash]+'-'+line[firstSlash+1:secondSlash])
		if cycle == 2:	# GALLONS
			galSpace = line.find(' ')
			gallons.append(line[galSpace+1:-1])
		if cycle == 3:	# COST
			costSpace = line.find(' ')
			cost.append(line[costSpace+2:-1])
		cycle += 1
		if cycle > 3: cycle = 0
print(pumpId)
print(mileage)
print(date)
print(gallons)
print(cost)

