import re

log = open('gasLog.txt')
logToAnalyze = log.read()
print(logToAnalyze)
pattern = re.compile(r'Mi')
singleSpace = re.compile(r'\s')
spaces = re.compile(r'\s\s')
newLine = re.compile(r'\n')
matches = pattern.finditer(logToAnalyze)
findSpaces = spaces.finditer(logToAnalyze)

# DATA COLUMNS
pumpId = []
mileage = []
pumpDate = []
pumpCost = []

# for match in matches:
# 	w0 = match.span()[0]
# 	w1 = match.span()[1]
# 	print(logToAnalyze[w0:w1+])
start = 0
cycle = 0
for space in findSpaces:
	end = space.span()[0]
	currentIter = logToAnalyze[start:end]
	print(currentIter, 'CYCLE',cycle)
	print('\nANALYSIS\n')
	findNewLine = newLine.finditer(currentIter)
	subStart = 0
	subCycle = 0

	# Analysis by line
	for line in findNewLine:
		print('LINE:',line)
		subEnd = line.span()[0]
		lineAnalysis = currentIter[subStart:subEnd]
		print(lineAnalysis, 'subCycle',subCycle)
		subStart = line.span()[1]

		# If cycle is 0, this is the line with the log number and mileage.
		# We need to find the first occurance of the space.
		if lineAnalysis[:2] == "Mi":
			# print(lineAnalysis[0:singleSpace.finditer(lineAnalysis).span()[0]])
			miSpace = lineAnalysis.find(' ')
			print('MILE LOG NUMBER = ',lineAnalysis[2:miSpace])
			print('MILEAGE = ',lineAnalysis[miSpace:])
		
		# Analyzing the date line
		if subCycle == 1:
			firstSlash = lineAnalysis.find('/')
			secondSlash = lineAnalysis.find('/',firstSlash+1)
			year = int('20'+lineAnalysis[secondSlash+1:])
			day = int(lineAnalysis[firstSlash+1:secondSlash])
			month = int(lineAnalysis[:firstSlash])
			print(str(month),str(day),str(year))

		# Analyzing the gallons line
		if subCycle == 2:
			gallonSpace = lineAnalysis.find(' ')
			gallons = float(lineAnalysis[gallonSpace+1:])
			print(gallons)

		if subCycle == 3:

			costSpace = lineAnalysis.find(' ')
			cost = lineAnalysis[costSpace+1:]
			print(cost)
		subCycle += 1

	print('\n')
	start = space.span()[1]
	cycle += 1;