#Write a program to accept name of a file from user & display longest & smallest line from the same.
def LongestAndSmallest(fd):
    line = fd.readline()
    smallest=line
    longest=line
    while line != "":
        if len(longest)<len(line) :
            longest=line
        if len(smallest)>len(line) :
            smallest=line
        line = fd.readline()
    return longest,smallest
def main():
    fileName=input("Enter file name :")
    fd=open(fileName) #(r"storage/emulated/0/qpython/audio.conf")
    longest, smallest= LongestAndSmallest(fd)
    print ("Longest line="+longest)
    print ("smallest line="+ smallest)
if __name__== "__main__" :
    main()