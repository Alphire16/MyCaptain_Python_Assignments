FileType = {"py":"Python","pdf":"Portable Document Format","txt":"Text File","doc":"Word Document"}
FileName = input("Enter file name: ")
x = FileName.split(".")
print("The file type is ",FileType[x[-1]])
