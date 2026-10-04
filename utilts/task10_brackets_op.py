def check_brackets():
    s = input()
    c=0
    for i in s:
        if(i == "("):
            c+=1
        else:
            c-=1
        if(c<0):
            print("НЕТ")
            return
    if(c==0):
        print("ДА")
    else:
        print("НЕТ")