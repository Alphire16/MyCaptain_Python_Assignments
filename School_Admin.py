import csv
Yes = ["y","Y","yes","Yes","YES"]
No = ["n","N","no","No","NO"]
Head = ["Name","Age","PhnNo","Email"]
no = 1
def StuFileWrite(StuInfo_list):
    with open("Student_Data.csv","a+",newline = "") as StuData:
        StuWrite = csv.writer(StuData)
        if StuData.tell() == 0:
            StuWrite.writerow(Head)
        StuWrite.writerow(StuInfo_list)
def StuFileRead():
    with open("Student_Data.csv","r") as StuData:
        StuRead = csv.reader(StuData)
        for i,row in enumerate(StuRead):
            print(f"{i} | {row[0]} | {row[1]} | {row[2]} | {row[3]}")

while True:
    StuInfo = input(f"Enter your student info for student #{no} in this format:- Name Age PhnNo Email:\n")
    StuInfo_list = StuInfo.split(" ")
    print(f"Are these the correct values that you have entered?\nName: {StuInfo_list[0]}\nAge: {StuInfo_list[1]}\nPhnNo: {StuInfo_list[2]}\nEmail: {StuInfo_list[3]}")
    y_n = input("If Yes then press y, if No then press n:\n")
    if y_n in Yes:
        x = StuFileWrite(StuInfo_list)
    elif y_n in No:
        print("Re-Enter your values:")
        continue
    MoreStu = input("Do you want to add more Students?(y/n)\n")
    if MoreStu in Yes:
        no+=1
    elif MoreStu in No:
        break

StuFileRead()

