import csv
import decimal

cr = csv.reader(open("data/rawSizes.csv","rU"))
widths = csv.writer(open("data/widths.csv","wb"))
heights = csv.writer(open("data/heights.csv","wb"))
aspectRatios = csv.writer(open("data/aspectRatios.csv","wb"))
dimensions = csv.writer(open("data/dimensions.csv","wb"))

widths.writerow(["width","pageviews"])
heights.writerow(["height","pageviews"])
aspectRatios.writerow(["aspectRatio","pageviews"])
dimensions.writerow(["width","height","pageviews"])

head = cr.next()
widthsDict = {}
heightsDict = {}
aspectRatiosDict = {}
for row in cr:
	dims = row[0]
	pageviews = row[2]
	if dims.find("x") == -1:
		continue
	w = dims.split("x")[0]
	h = dims.split("x")[1]
	if h != "0":
		aspectRatio = round(float(w)/float(h), 4)
	else:
		aspectRatio = 0

	dimensions.writerow([w, h, pageviews])

	if w not in widthsDict:
		widthsDict[w] = 0
	widthsDict[w] += int(pageviews)

	if h not in heightsDict:
		heightsDict[h] = 0
	heightsDict[h] += int(pageviews)

	if aspectRatio not in aspectRatiosDict:
		aspectRatiosDict[aspectRatio] = 0
	aspectRatiosDict[aspectRatio] += int(pageviews)

for w in widthsDict:
	widths.writerow([w, widthsDict[w]])

for h in heightsDict:
	heights.writerow([h, heightsDict[h]])

for ar in aspectRatiosDict:
	aspectRatios.writerow([ar, aspectRatiosDict[ar]])

