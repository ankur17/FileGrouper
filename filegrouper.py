import os
def part_word(a):
	plus=a.index("+")
	dot=a.index(".")
	return a[plus+1:dot]+"+"+a[:plus]+a[dot:]
p = "C:\\Users\\Apache-PC\\Desktop\\mytest"
p = raw_input("Enter the path of the folder")
#print os.path.split(os.path.abspath(p))    # Its the absolute path 
part_word("Ankur+ji.txt")
l =  os.listdir(p)
faulty_words = list()
for a in l:
	try:
		new_word=part_word(a) 
		os.rename(os.path.join(p,a),os.path.join(p,new_word))
	except Exception, e:
		faulty_words.append(a)
		pass
	#print new_word
	#os.rename(p+"\\"+os.listdir(p)[1],p+"\\""ola.txt")
print "Following are the list of the words that could not be renamed:"
for a in faulty_words:
	print a