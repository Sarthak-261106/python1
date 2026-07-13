def student_details(sid,sname,**marks):
    if len(marks)==0:
        print(f'{sname} was absent in exam')
    else:
        percent=sum(marks.values())/len(marks)
        print(f'{sname} secured {percent}% marks in exam')

student_details(165,'sarthak',wt=70,dbms=76,ada=81) 