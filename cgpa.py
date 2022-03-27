def cgpa_display():
    total1=0
    gtotal=0
    grades={"s":"10","S":"10","a":"9","A":"9","b":"8","B":"8","c":"7","C":"7","d":"6","D":"6","e":"5","E":"5","f":"4","F":"4"}
    name=input("Enter the student name")
    dept=input("Enter the department:")
    year=input("Enter the year of student:") 
    sem=input("Enter the semester of the student:")
    n=int(input("Enter the No. of Subjects:"))
    print("Enter the grades in (S-E) F-arrear")
    marks=[]
    for entry in range(n):
        sc=input("\n Enter the subject code:")
        ma=input("\n Enter the grades in (S-E):")
        g=float(input("\n Enter the grade points:"))
        if ma in grades:
            m=float(grades[ma]) 
            ma=ma.upper() 
            entry=(sc,g,m,ma) 
            marks.append(entry) 
            if ma=="F":
                mn="0"
            else:
                mn="1"
    if mn=="0":
        print("NAME:",name)
        print("DEPARTMENT:",dept)
        print("YEAR:",year)
        print("SEMESTER:",sem)
        print("Subject code Grade")
        for entry in marks:
            sc,g,m,ma=entry
            print(sc,"\t\t",ma) 
            print("CGPA=ARREAR")
    else:
        print("\n\tNAME:",name,"\t\tDEPARTMENT:",dept) 
        print("\n\tYEAR:",year,"\t\tSEMESTER:",sem)
        print("\n Subject code Grade")
        for entry in marks:
            sc,g,m,ma=entry 
            print("\n\t",sc,"\t\t",ma) 
            total1=total1+m*g 
            gtotal=gtotal+g 
            cgpa=total1/gtotal 
            print("\n\nCGPA=",cgpa) 
            
            
cgpa_display()
input("\n Press enter key to exit....")

            
