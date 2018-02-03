def readlines(fd):
   line=(fd.readline())
   while line!="":
      print (line)
      line=fd.readline()

def main():
   fd=open(r"storage/emulated/0/qpython/a.txt")
   readlines(fd)
if __name__== "__main__" :
   main()