import urllib2,HTMLParser,os

host = "http://viber.tsymbal.su/save.php?path=data/stickers/"
emotion = "022" #emotion
maxnum = 36 #number
tail = ".png&lang=en"
localSavePath = "/viber.tsymbal.su_" + emotion

title = emotion
path = os.getcwd()
new_path = os.path.join(path,title)
if not os.path.isdir(new_path):
	os.makedirs(new_path)

for i in range(0,maxnum):
	if i < 10:
		k = "0" + str(i)
	else:
		k = str(i)
	cont = urllib2.urlopen(host + emotion + k + tail).read()
	filename = new_path + localSavePath + k + ".png"
	print filename
	f = open(filename,'w+')
	f.write(cont)
	f.close
print "ok!"
