'''2. Write a program to accept file from the user and print count of lines present in that file based on following filters
- if filter comes as empty then line count
- if filter comes as "^Hello", then line count should be of lines which starts with "Hello"
- if filter comes as "Hello$" then count lines which ends with Hello.
- if filter comes as "Hello" string in the line, then count lines.
'''
def CountLines(fd,string1):
    count=0
    line = fd.readline()
    while line != "":
        if string1[0]== "^" :
            if line[:-1].endswith(string1[1:]):
                count+=1
        elif string1[-1]== "$" :
            if  line.startswith(string1[0:-1]):
                count+=1
        else :
            if string1 in line:
                count += 1
        line = fd.readline()
    return count
def main():
    fileName=input("Enter file name :")
    string1 = input("Enter string :")
    string1 = input("Enter string :")
    fd=open(fileName) #(r"storage/emulated/0/qpython/audio.conf")
    print(CountLines(fd,string1))

if __name__== "__main__" :
    main()