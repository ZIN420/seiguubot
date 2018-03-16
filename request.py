# This Python file uses the following encoding: utf-8

request = ""

idols = {"haruka":2 ,"chihaya":3 ,"miki":4 ,"yukiho":5 ,"yayoi":6 ,"makoto":7 ,"iori":8 ,"takane":9 ,"ritsuko":10,
"azusa":11 ,"ami":12 ,"hibiki":13 ,"mirai":14 ,"shizuka":15 ,"tsubasa":16 ,"kotoha":17 ,"elena":18 ,"minako":19 ,
"megumi":20 ,"matsuri":21 ,"serika":22 ,"akane":23 ,"anna":24 ,"roco":25 ,"yuriko":26 ,"sayoko":27 ,"arisa":28 ,
"umi":29 ,"iku":30 ,"tomoka":31 ,"emily":32 ,"shiho":33 ,"ayumu":34 ,"hinata":35 ,"kana":36 ,"nao":37 ,
"chizuru":38 ,"konomi":39 ,"tamaki":40 ,"fuka":41 ,"miya":42 ,"noriko":43 ,"mizuki":44 ,"karen":45 ,"rio":46 ,
"subaru":47 ,"reika":48 ,"momoko":49 ,"julia":50 ,"tsumugi":51 ,"kaori":52 }

fields = ["color", "seiyuu", "nick", "char", "birthday", "birthplace", "twitter", "social", "blog", "site"]
fieldsp = ["Image Color: ", "Seiyuu: ", "Nickname: ", "Character: ", "Birthday: ", "Birthplace: ", "Twitter: ", "Social Media: ", "Blog: ", "Website: "]
#print(idols.values())

def parserequest(request):

	request = request.lower()
	query = ""  
	output = ""
	x,y = [],[]
	sep = request.split(" ")

	
	for ele in sep:
		index = idols.get(ele)
		if index is not None:
			y.append(index-2)

	for field in fields:
		if field in request:
			x.append(fields.index(field))

	
	#print(x, y)
	return (x,y)


def printreq(x, y, values):
	output = ""
	for row in y:
		output += "|"

		output += str(values[row][3] + " |")
		output += "Seiyuu: " + str(values[row][1] + " |")
		for col in x:
			output += str(fieldsp[col] + " "+ values[row][col]+ " |")
		output += "\n"
	return(str(output))
		#print("next")
	#print("done")

#print(parserequest("haruka seiyuu nick char"))







