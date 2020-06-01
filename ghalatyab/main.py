from mghalat import ghalat
class fileDirectory():
	
	def __init__(self, name):
		self.dirName = name 
	def bazKardaneFile(self) :
		self.khandaneFile = open(self.dirName) 
		return self.khandaneFile
	def tabdilBeList(self) :
		x = open(self.dirName)
		z =x.read() 
		self.tabdilList = z.split()
		return self.tabdilList

obj = fileDirectory("myfile.txt")
f=obj.tabdilBeList()
if __name__ =="__main__":
    try :
        ghalat(f)
    except :
        print("lotfan yek file dar hamin directory besaz ba name : myfile.txt")
    
