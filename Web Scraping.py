#این کد وب اسکرپینگ را برای سایت کوئرا انجام میدهد

from tkinter import *
def BackEnd():
    from bs4 import BeautifulSoup
    import requests
    URL="https://quera.ir/careers/jobs?technologies=backend"
    URL2="https://quera.ir/careers/jobs?technologies=backend&page=2"
    URL3="https://quera.ir/careers/jobs?technologies=backend&page=3"
    URL4="https://quera.ir/careers/jobs?technologies=backend&page=4"
    URL5="https://quera.ir/careers/jobs?technologies=backend&page=5"
    
    response = requests.get(url=URL)
    response2 = requests.get(url=URL2)
    response3 = requests.get(url=URL3)
    response4 = requests.get(url=URL4)
    response5 = requests.get(url=URL5)
    soup=BeautifulSoup(response.content , 'html.parser')
    soup2=BeautifulSoup(response2.content , 'html.parser')
    soup3=BeautifulSoup(response3.content , 'html.parser')
    soup4=BeautifulSoup(response4.content , 'html.parser')
    soup5=BeautifulSoup(response5.content , 'html.parser')
    list3=[]
    result1=soup.findAll('span',class_="job-level hide-in-mobile")
    result22=soup2.findAll('span',class_="job-level hide-in-mobile")
    result33=soup3.findAll('span',class_="job-level hide-in-mobile")
    result44=soup4.findAll('span',class_="job-level hide-in-mobile")
    result55=soup5.findAll('span',class_="job-level hide-in-mobile")
    for result1 in result1:
        m= result1.text.strip()
        list3.append(m)
    for result22 in result22:
        u= result22.text.strip()
        list3.append(u)
    for result33 in result33:
        LL= result33.text.strip()
        list3.append(LL)
    for result44 in result44:
        LL1= result44.text.strip()
        list3.append(LL1)
    for result55 in result55:
        LL11= result55.text.strip()
        list3.append(LL11)
    z=len(list3)
    #print("***Number of job opportunities*** is :" , z)
    jobOppotunities.configure(text=" {}".format(round(z)) , bg='white')
    #print("_________________Experience level_________________")
    sumSENIOR=list3.count('ارشد (Senior)')
    sumSENIOR=(sumSENIOR/z)*100
    #print("Senior percentage is :" , sumSENIOR,"%")
    senior.configure(text=" {} %".format(round(sumSENIOR)), bg='white')

    sumJONIOR=list3.count('جوان (Junior)')
    sumJONIOR=(sumJONIOR/z)*100
    #print("Jonior percentage is :" , sumJONIOR , "%")
    jonior.configure(text="  {} %".format(round(sumJONIOR)), bg='white')
    sumINTERN=list3.count('کارآموز (Intern)')
    sumINTERN=(sumINTERN/z)*100
    #print("Intern percentage is :" , sumINTERN , "%")
    intern1.configure(text=" {} %".format(round(sumINTERN)), bg='white')
    sumLeader=list3.count('راهبر فنی (Lead)')
    sumLeader=(sumLeader/z)*100
    #print("Lead percentage is :" , sumLeader, "%")
    leader.configure(text="{} %".format(round(sumLeader)), bg='white')
    #print("__________________work time______________________ ")
    result2=soup.findAll('span',class_="job-collab")
    result21=soup2.findAll('span',class_="job-collab")
    result222=soup3.findAll('span',class_="job-collab")
    result23=soup4.findAll('span',class_="job-collab")
    result24=soup5.findAll('span',class_="job-collab")
    list4=[]
    for result2 in result2:
        l= result2.text.strip()
        t=l.replace("پروژه‌ای" , "PROJEH" , 100)
        c=t.replace("تمام‌وقت" , "tamamvaght", 100 )
        q=c.replace("پاره‌وقت" , "parehVaght" , 100)
        list4.append(q)
    for result21 in result21:
        l1= result21.text.strip()
        t1=l1.replace("پروژه‌ای" , "PROJEH" , 100)
        c1=t1.replace("تمام‌وقت" , "tamamvaght", 100 )
        q1=c1.replace("پاره‌وقت" , "parehVaght" , 100)
        list4.append(q1)
    for result222 in result222:
        l2= result222.text.strip()
        t2=l2.replace("پروژه‌ای" , "PROJEH" , 100)
        c2=t2.replace("تمام‌وقت" , "tamamvaght", 100 )
        q2=c2.replace("پاره‌وقت" , "parehVaght" , 100)
        list4.append(q2)
    for result23 in result23:
        l3= result23.text.strip()
        t3=l3.replace("پروژه‌ای" , "PROJEH" , 100)
        c3=t3.replace("تمام‌وقت" , "tamamvaght", 100 )
        q3=c3.replace("پاره‌وقت" , "parehVaght" , 100)
        list4.append(q3)
    for result24 in result24:
        l4= result24.text.strip()
        t4=l4.replace("پروژه‌ای" , "PROJEH" , 100)
        c4=t4.replace("تمام‌وقت" , "tamamvaght", 100 )
        q4=c4.replace("پاره‌وقت" , "parehVaght" , 100)
        list4.append(q4)
    ww=len(list4)
    sumPROJEH=list4.count('PROJEH')
    ProjectPercantage=(sumPROJEH/ww)*100
    #print("project Percenatge  is : " , ProjectPercantage)
    project.configure(text=" {} %".format(round(ProjectPercantage)), bg='white' )
    sumTAMAMVAGHT=list4.count('tamamvaght')
    TamamVAGHT=(sumTAMAMVAGHT/ww)*100
    #print("Full_time Percentage is  : " , TamamVAGHT)
    Fullttime.configure(text=" {} %".format(round(TamamVAGHT)), bg='white')
    sumPAREHVAGHT=list4.count("parehVaght")
    PARTtime=(sumPAREHVAGHT/ww)*100
    #print("Part-time percentage is : " ,PARTtime )
    PARTttime.configure(text="{} %".format(round(PARTtime)), bg='white')
    #print("__________________Skills needed to work____________________")
    result3=soup.findAll('span', class_="ui small tech label main")
    result31=soup2.findAll('span', class_="ui small tech label main")
    result32=soup3.findAll('span', class_="ui small tech label main")
    result333=soup4.findAll('span', class_="ui small tech label main")
    result34=soup5.findAll('span', class_="ui small tech label main")
    list1=[]
    for result3 in result3:
        a=  result3.text.strip()
        c=list1.append(a)
    for result31 in result31:
        a1=  result31.text.strip()
        c1=list1.append(a1)
    for result32 in result32:
        a2=  result3.text.strip()
        c2=list1.append(a2)
    for result333 in result333:
        a3=  result333.text.strip()
        c3=list1.append(a3)
    for result34 in result34:
        a4=  result34.text.strip()
        c4=list1.append(a4)
    w=len(list1)
    dict1=dict() 
    for elem in list1:
        if elem in dict1:
            dict1[elem] += 1
        else:
            dict1[elem] = 1  
    dict1 = { key:value for key, value in dict1.items() if value > 1}
    values=dict1.values()
    max1=max(values)
    KEY1=list(dict1.keys())[list(dict1.values()).index(max1)]
    newdict1=dict1.pop(KEY1)
    #print(dict1)
    values2=dict1.values()
    max2=max(values2)
    KEY2=list(dict1.keys())[list(dict1.values()).index(max2)]
    newdict1=dict1.pop(KEY2)
    values3=dict1.values()
    max3=max(values3)
    #print(max3)
    KEY3=list(dict1.keys())[list(dict1.values()).index(max3)]
    newdict1=dict1.pop(KEY3)
    listkey=[KEY1 ,KEY2 ,  KEY3]
    skillss.configure(text="{} ".format(listkey), bg='white')
    #print(listkey)
    #print("_______________Average salary______________")
    result4=soup.findAll('span', class_="job-salary")
    result41=soup2.findAll('span', class_="job-salary")
    result42=soup3.findAll('span', class_="job-salary")
    result43=soup4.findAll('span', class_="job-salary")
    result444=soup5.findAll('span', class_="job-salary")
    list5=[]
    for result4 in result4:
        M= result4.text.strip()
        A=M.replace("حقوق بیش از ۱۲ میلیون تومان" , "13" , 100)
        c=A.replace('حقوق تا ۱۲ میلیون تومان' , "12", 100 )
        y=c.replace("حقوق تا ۸ میلیون تومان" , "8" , 100)
        k=y.replace("حقوق تا ۲ میلیون تومان" , "2" , 100)
        o=k.replace("حقوق تا ۶ میلیون تومان" , "6" , 100)
        list5.append(o)
    for result41 in result41:
        M1= result41.text.strip()
        A1=M1.replace("حقوق بیش از ۱۲ میلیون تومان" , "13" , 100)
        c1=A1.replace('حقوق تا ۱۲ میلیون تومان' , "12", 100 )
        y1=c1.replace("حقوق تا ۸ میلیون تومان" , "8" , 100)
        k1=y1.replace("حقوق تا ۲ میلیون تومان" , "2" , 100)
        o1=k1.replace("حقوق تا ۶ میلیون تومان" , "6" , 100)
        list5.append(o1)
    for result42 in result42:
        M2= result42.text.strip()
        A2=M2.replace("حقوق بیش از ۱۲ میلیون تومان" , "13" , 100)
        c2=A2.replace('حقوق تا ۱۲ میلیون تومان' , "12", 100 )
        y2=c2.replace("حقوق تا ۸ میلیون تومان" , "8" , 100)
        k2=y2.replace("حقوق تا ۲ میلیون تومان" , "2" , 100)
        o2=k2.replace("حقوق تا ۶ میلیون تومان" , "6" , 100)
        list5.append(o2)
    for result43 in result43:
        M3= result43.text.strip()
        A3=M3.replace("حقوق بیش از ۱۲ میلیون تومان" , "13" , 100)
        c3=A3.replace('حقوق تا ۱۲ میلیون تومان' , "12", 100 )
        y3=c3.replace("حقوق تا ۸ میلیون تومان" , "8" , 100)
        k3=y3.replace("حقوق تا ۲ میلیون تومان" , "2" , 100)
        o3=k3.replace("حقوق تا ۶ میلیون تومان" , "6" , 100)
        list5.append(o3)
    for result444 in result444:
        M4= result444.text.strip()
        A4=M4.replace("حقوق بیش از ۱۲ میلیون تومان" , "13" , 100)
        c4=A4.replace('حقوق تا ۱۲ میلیون تومان' , "12", 100 )
        y4=c4.replace("حقوق تا ۸ میلیون تومان" , "8" , 100)
        k4=y4.replace("حقوق تا ۲ میلیون تومان" , "2" , 100)
        o4=k4.replace("حقوق تا ۶ میلیون تومان" , "6" , 100)
        list5.append(o4)
    ff=len(list5)
    salery2=list5.count("2")
    salery6=list5.count("6")
    salery8=list5.count("8")
    salery12=list5.count("12")
    salery13=list5.count("13")
    sumSALARY=2*salery2 + 6*salery6 + 8*salery8 + 12*salery12 + 13*salery13
    AVERAGE=sumSALARY/ff
    #print("***Average salary is " , AVERAGE , "milion toman***")
    AVERAGE1.configure(text=" {} milion toman $".format(round(AVERAGE) ), bg='white')
def FrontEnd():
    from bs4 import BeautifulSoup
    import requests
    URL="https://quera.ir/careers/jobs?technologies=frontend"
    URL2="https://quera.ir/careers/jobs?technologies=frontend&page=2"
    URL3="https://quera.ir/careers/jobs?technologies=frontend&page=3"
    URL4="https://quera.ir/careers/jobs?technologies=frontend&page=4"
    URL5="https://quera.ir/careers/jobs?technologies=frontend&page=5"
    response = requests.get(url=URL)
    response2 = requests.get(url=URL2)
    response3 = requests.get(url=URL3)
    response4 = requests.get(url=URL4)
    response5 = requests.get(url=URL5)
    soup=BeautifulSoup(response.content , 'html.parser')
    soup2=BeautifulSoup(response2.content , 'html.parser')
    soup3=BeautifulSoup(response3.content , 'html.parser')
    soup4=BeautifulSoup(response4.content , 'html.parser')
    soup5=BeautifulSoup(response5.content , 'html.parser')
    list3=[]
    result1=soup.findAll('span',class_="job-level hide-in-mobile")
    result22=soup2.findAll('span',class_="job-level hide-in-mobile")
    result33=soup3.findAll('span',class_="job-level hide-in-mobile")
    result44=soup4.findAll('span',class_="job-level hide-in-mobile")
    result55=soup5.findAll('span',class_="job-level hide-in-mobile")
    for result1 in result1:
        m= result1.text.strip()
        list3.append(m)
    for result22 in result22:
        u= result22.text.strip()
        list3.append(u)
    for result33 in result33:
        LL= result33.text.strip()
        list3.append(LL)
    for result44 in result44:
        LL1= result44.text.strip()
        list3.append(LL1)
    for result55 in result55:
        LL11= result55.text.strip()
        list3.append(LL11)
    z=len(list3)
    #print("***Number of job opportunities*** is :" , z)
    jobOppotunities.configure(text=" {}".format(round(z)) , bg='white')
    #print("_________________Experience level_________________")
    sumSENIOR=list3.count('ارشد (Senior)')
    sumSENIOR=(sumSENIOR/z)*100
    #print("Senior percentage is :" , sumSENIOR,"%")
    senior.configure(text=" {} %".format(round(sumSENIOR)), bg='white')
    sumJONIOR=list3.count('جوان (Junior)')
    sumJONIOR=(sumJONIOR/z)*100
    #print("Jonior percentage is :" , sumJONIOR , "%")
    jonior.configure(text="  {} %".format(sumJONIOR), bg='white')
    sumINTERN=list3.count('کارآموز (Intern)')
    sumINTERN=(sumINTERN/z)*100
    #print("Intern percentage is :" , sumINTERN , "%")
    intern1.configure(text=" {} %".format(round(sumINTERN)), bg='white')
    sumLeader=list3.count('راهبر فنی (Lead)')
    sumLeader=(sumLeader/z)*100
    #print("Lead percentage is :" , sumLeader, "%")
    leader.configure(text="{} %".format(round(sumLeader)), bg='white')
    #print("__________________work time______________________ ")
    result2=soup.findAll('span',class_="job-collab")
    result21=soup2.findAll('span',class_="job-collab")
    result222=soup3.findAll('span',class_="job-collab")
    result23=soup4.findAll('span',class_="job-collab")
    result24=soup5.findAll('span',class_="job-collab")
    list4=[]
    for result2 in result2:
        l= result2.text.strip()
        t=l.replace("پروژه‌ای" , "PROJEH" , 100)
        c=t.replace("تمام‌وقت" , "tamamvaght", 100 )
        q=c.replace("پاره‌وقت" , "parehVaght" , 100)
        list4.append(q)
    for result21 in result21:
        l1= result21.text.strip()
        t1=l1.replace("پروژه‌ای" , "PROJEH" , 100)
        c1=t1.replace("تمام‌وقت" , "tamamvaght", 100 )
        q1=c1.replace("پاره‌وقت" , "parehVaght" , 100)
        list4.append(q1)
    for result222 in result222:
        l2= result222.text.strip()
        t2=l2.replace("پروژه‌ای" , "PROJEH" , 100)
        c2=t2.replace("تمام‌وقت" , "tamamvaght", 100 )
        q2=c2.replace("پاره‌وقت" , "parehVaght" , 100)
        list4.append(q2)
    for result23 in result23:
        l3= result23.text.strip()
        t3=l3.replace("پروژه‌ای" , "PROJEH" , 100)
        c3=t3.replace("تمام‌وقت" , "tamamvaght", 100 )
        q3=c3.replace("پاره‌وقت" , "parehVaght" , 100)
        list4.append(q3)
    for result24 in result24:
        l4= result24.text.strip()
        t4=l4.replace("پروژه‌ای" , "PROJEH" , 100)
        c4=t4.replace("تمام‌وقت" , "tamamvaght", 100 )
        q4=c4.replace("پاره‌وقت" , "parehVaght" , 100)
        list4.append(q4)
    ww=len(list4)
    sumPROJEH=list4.count('PROJEH')
    ProjectPercantage=(sumPROJEH/ww)*100
    #print("project Percenatge  is : " , ProjectPercantage)
    project.configure(text=" {} %".format(round(ProjectPercantage)), bg='white' )
    sumTAMAMVAGHT=list4.count('tamamvaght')
    TamamVAGHT=(sumTAMAMVAGHT/ww)*100
    #print("Full_time Percentage is  : " , TamamVAGHT)
    Fullttime.configure(text=" {} %".format(round(TamamVAGHT)), bg='white')
    sumPAREHVAGHT=list4.count("parehVaght")
    PARTtime=(sumPAREHVAGHT/ww)*100
    #print("Part-time percentage is : " ,PARTtime )
    PARTttime.configure(text="{} %".format(round(PARTtime)), bg='white')
    result3=soup.findAll('span', class_="ui small tech label main")
    result31=soup2.findAll('span', class_="ui small tech label main")
    result32=soup3.findAll('span', class_="ui small tech label main")
    result333=soup4.findAll('span', class_="ui small tech label main")
    result34=soup5.findAll('span', class_="ui small tech label main")
    list1=[]
    for result3 in result3:
        a=  result3.text.strip()
        c=list1.append(a)
    for result31 in result31:
        a1=  result31.text.strip()
        c1=list1.append(a1)
    for result32 in result32:
        a2=  result3.text.strip()
        c2=list1.append(a2)
    for result333 in result333:
        a3=  result333.text.strip()
        c3=list1.append(a3)
    for result34 in result34:
        a4=  result34.text.strip()
        c4=list1.append(a4)
    w=len(list1)
    dict1=dict() 
    for elem in list1:
        if elem in dict1:
            dict1[elem] += 1
        else:
            dict1[elem] = 1  
    dict1 = { key:value for key, value in dict1.items() if value > 1}
    values=dict1.values()
    max1=max(values)
    KEY1=list(dict1.keys())[list(dict1.values()).index(max1)]
    newdict1=dict1.pop(KEY1)
    #print(dict1)
    values2=dict1.values()
    max2=max(values2)
    KEY2=list(dict1.keys())[list(dict1.values()).index(max2)]
    newdict1=dict1.pop(KEY2)
    values3=dict1.values()
    max3=max(values3)
    KEY3=list(dict1.keys())[list(dict1.values()).index(max3)]
    newdict1=dict1.pop(KEY3)
    listkey=[KEY1 ,KEY2 ,  KEY3]
    skillss.configure(text="{} ".format(listkey), bg='white')
    #print(listkey)
    #print("_______________Average salary______________")
    result4=soup.findAll('span', class_="job-salary")
    result41=soup2.findAll('span', class_="job-salary")
    result42=soup3.findAll('span', class_="job-salary")
    result43=soup4.findAll('span', class_="job-salary")
    result444=soup5.findAll('span', class_="job-salary")
    list5=[]
    for result4 in result4:
        M= result4.text.strip()
        A=M.replace("حقوق بیش از ۱۲ میلیون تومان" , "13" , 100)
        c=A.replace('حقوق تا ۱۲ میلیون تومان' , "12", 100 )
        y=c.replace("حقوق تا ۸ میلیون تومان" , "8" , 100)
        k=y.replace("حقوق تا ۲ میلیون تومان" , "2" , 100)
        o=k.replace("حقوق تا ۶ میلیون تومان" , "6" , 100)
        list5.append(o)
    for result41 in result41:
        M1= result41.text.strip()
        A1=M1.replace("حقوق بیش از ۱۲ میلیون تومان" , "13" , 100)
        c1=A1.replace('حقوق تا ۱۲ میلیون تومان' , "12", 100 )
        y1=c1.replace("حقوق تا ۸ میلیون تومان" , "8" , 100)
        k1=y1.replace("حقوق تا ۲ میلیون تومان" , "2" , 100)
        o1=k1.replace("حقوق تا ۶ میلیون تومان" , "6" , 100)
        list5.append(o1)
    for result42 in result42:
        M2= result42.text.strip()
        A2=M2.replace("حقوق بیش از ۱۲ میلیون تومان" , "13" , 100)
        c2=A2.replace('حقوق تا ۱۲ میلیون تومان' , "12", 100 )
        y2=c2.replace("حقوق تا ۸ میلیون تومان" , "8" , 100)
        k2=y2.replace("حقوق تا ۲ میلیون تومان" , "2" , 100)
        o2=k2.replace("حقوق تا ۶ میلیون تومان" , "6" , 100)
        list5.append(o2)
    for result43 in result43:
        M3= result43.text.strip()
        A3=M3.replace("حقوق بیش از ۱۲ میلیون تومان" , "13" , 100)
        c3=A3.replace('حقوق تا ۱۲ میلیون تومان' , "12", 100 )
        y3=c3.replace("حقوق تا ۸ میلیون تومان" , "8" , 100)
        k3=y3.replace("حقوق تا ۲ میلیون تومان" , "2" , 100)
        o3=k3.replace("حقوق تا ۶ میلیون تومان" , "6" , 100)
        list5.append(o3)
    for result444 in result444:
        M4= result444.text.strip()
        A4=M4.replace("حقوق بیش از ۱۲ میلیون تومان" , "13" , 100)
        c4=A4.replace('حقوق تا ۱۲ میلیون تومان' , "12", 100 )
        y4=c4.replace("حقوق تا ۸ میلیون تومان" , "8" , 100)
        k4=y4.replace("حقوق تا ۲ میلیون تومان" , "2" , 100)
        o4=k4.replace("حقوق تا ۶ میلیون تومان" , "6" , 100)
        list5.append(o4)
    ff=len(list5)
    salery2=list5.count("2")
    salery6=list5.count("6")
    salery8=list5.count("8")
    salery12=list5.count("12")
    salery13=list5.count("13")
    sumSALARY=2*salery2 + 6*salery6 + 8*salery8 + 12*salery12 + 13*salery13
    AVERAGE=sumSALARY/ff
    #print("***Average salary is " , AVERAGE , "milion toman***")
    AVERAGE1.configure(text=" {} milion toman $".format( round(AVERAGE)), bg='white')
    #print("__________________________________")
def Mobile():
    from bs4 import BeautifulSoup
    import requests
    URL="https://quera.ir/careers/jobs?technologies=mobile"
    URL2="https://quera.ir/careers/jobs?technologies=mobile&page=2"
    URL3="https://quera.ir/careers/jobs?technologies=mobile&page=3"
    response = requests.get(url=URL)
    response2 = requests.get(url=URL2)
    response3 = requests.get(url=URL3)
    soup=BeautifulSoup(response.content , 'html.parser')
    soup2=BeautifulSoup(response2.content , 'html.parser')
    soup3=BeautifulSoup(response3.content , 'html.parser')
    list3=[]
    result1=soup.findAll('span',class_="job-level hide-in-mobile")
    result22=soup2.findAll('span',class_="job-level hide-in-mobile")
    result33=soup3.findAll('span',class_="job-level hide-in-mobile")
    for result1 in result1:
        m= result1.text.strip()
        list3.append(m)
    for result22 in result22:
        u= result22.text.strip()
        list3.append(u)
    for result33 in result33:
        LL= result33.text.strip()
        list3.append(LL)
    z=len(list3)
    #print("***Number of job opportunities*** is :" , z)
    jobOppotunities.configure(text=" {}".format(round(z)) , bg='white')
    #print("_________________Experience level_________________")
    sumSENIOR=list3.count('ارشد (Senior)')
    sumSENIOR=(sumSENIOR/z)*100
    #print("Senior percentage is :" , sumSENIOR,"%")
    senior.configure(text=" {} %".format(round(sumSENIOR)), bg='white')
    sumJONIOR=list3.count('جوان (Junior)')
    sumJONIOR=(sumJONIOR/z)*100
    #print("Jonior percentage is :" , sumJONIOR , "%")
    jonior.configure(text="  {} %".format(round(sumJONIOR)), bg='white')
    sumINTERN=list3.count('کارآموز (Intern)')
    sumINTERN=(sumINTERN/z)*100
    #print("Intern percentage is :" , sumINTERN , "%")
    intern1.configure(text=" {} %".format(round(sumINTERN)), bg='white')
    sumLeader=list3.count('راهبر فنی (Lead)')
    sumLeader=(sumLeader/z)*100
    #print("Lead percentage is :" , sumLeader, "%")
    leader.configure(text="{} %".format(round(sumLeader)), bg='white')
    #print("__________________work time______________________ ")
    result2=soup.findAll('span',class_="job-collab")
    result21=soup2.findAll('span',class_="job-collab")
    result222=soup3.findAll('span',class_="job-collab")
    list4=[]
    for result2 in result2:
        l= result2.text.strip()
        t=l.replace("پروژه‌ای" , "PROJEH" , 100)
        c=t.replace("تمام‌وقت" , "tamamvaght", 100 )
        q=c.replace("پاره‌وقت" , "parehVaght" , 100)
        list4.append(q)
    for result21 in result21:
        l1= result21.text.strip()
        t1=l1.replace("پروژه‌ای" , "PROJEH" , 100)
        c1=t1.replace("تمام‌وقت" , "tamamvaght", 100 )
        q1=c1.replace("پاره‌وقت" , "parehVaght" , 100)
        list4.append(q1)
    for result222 in result222:
        l2= result222.text.strip()
        t2=l2.replace("پروژه‌ای" , "PROJEH" , 100)
        c2=t2.replace("تمام‌وقت" , "tamamvaght", 100 )
        q2=c2.replace("پاره‌وقت" , "parehVaght" , 100)
        list4.append(q2)
    ww=len(list4)
    sumPROJEH=list4.count('PROJEH')
    ProjectPercantage=(sumPROJEH/ww)*100
    #print("project Percenatge  is : " , ProjectPercantage)
    project.configure(text=" {} %".format(round(ProjectPercantage)), bg='white' )
    sumTAMAMVAGHT=list4.count('tamamvaght')
    TamamVAGHT=(sumTAMAMVAGHT/ww)*100
    #print("Full_time Percentage is  : " , TamamVAGHT)
    Fullttime.configure(text=" {} %".format(round(TamamVAGHT)), bg='white')
    sumPAREHVAGHT=list4.count("parehVaght")
    PARTtime=(sumPAREHVAGHT/ww)*100
    #print("Part-time percentage is : " ,PARTtime )
    PARTttime.configure(text="{} %".format(round(PARTtime)), bg='white')
    #print("__________________Skills needed to work____________________")
    result3=soup.findAll('span', class_="ui small tech label main")
    result31=soup2.findAll('span', class_="ui small tech label main")
    result32=soup3.findAll('span', class_="ui small tech label main")
    list1=[]
    for result3 in result3:
        a=  result3.text.strip()
        c=list1.append(a)
    for result31 in result31:
        a1=  result31.text.strip()
        c1=list1.append(a1)
    for result32 in result32:
        a2=  result3.text.strip()
        c2=list1.append(a2)
    w=len(list1)
    dict1=dict() 
    for elem in list1:
        if elem in dict1:
            dict1[elem] += 1
        else:
            dict1[elem] = 1  
    dict1 = { key:value for key, value in dict1.items() if value > 1}
    values=dict1.values()
    max1=max(values)
    KEY1=list(dict1.keys())[list(dict1.values()).index(max1)]
    newdict1=dict1.pop(KEY1)
    #print(dict1)
    values2=dict1.values()
    max2=max(values2)
    KEY2=list(dict1.keys())[list(dict1.values()).index(max2)]
    newdict1=dict1.pop(KEY2)
    values3=dict1.values()
    max3=max(values3)
    KEY3=list(dict1.keys())[list(dict1.values()).index(max3)]
    newdict1=dict1.pop(KEY3)
    listkey=[KEY1 ,KEY2 ,  KEY3]
    skillss.configure(text="{} ".format(listkey), bg='white')
    #print(listkey)
    #print("_______________Average salary______________")
    result4=soup.findAll('span', class_="job-salary")
    result41=soup2.findAll('span', class_="job-salary")
    result42=soup3.findAll('span', class_="job-salary")
    list5=[]
    for result4 in result4:
        M= result4.text.strip()
        A=M.replace("حقوق بیش از ۱۲ میلیون تومان" , "13" , 100)
        c=A.replace('حقوق تا ۱۲ میلیون تومان' , "12", 100 )
        y=c.replace("حقوق تا ۸ میلیون تومان" , "8" , 100)
        k=y.replace("حقوق تا ۲ میلیون تومان" , "2" , 100)
        o=k.replace("حقوق تا ۶ میلیون تومان" , "6" , 100)
        list5.append(o)
    for result41 in result41:
        M1= result41.text.strip()
        A1=M1.replace("حقوق بیش از ۱۲ میلیون تومان" , "13" , 100)
        c1=A1.replace('حقوق تا ۱۲ میلیون تومان' , "12", 100 )
        y1=c1.replace("حقوق تا ۸ میلیون تومان" , "8" , 100)
        k1=y1.replace("حقوق تا ۲ میلیون تومان" , "2" , 100)
        o1=k1.replace("حقوق تا ۶ میلیون تومان" , "6" , 100)
        list5.append(o1)
    for result42 in result42:
        M2= result42.text.strip()
        A2=M2.replace("حقوق بیش از ۱۲ میلیون تومان" , "13" , 100)
        c2=A2.replace('حقوق تا ۱۲ میلیون تومان' , "12", 100 )
        y2=c2.replace("حقوق تا ۸ میلیون تومان" , "8" , 100)
        k2=y2.replace("حقوق تا ۲ میلیون تومان" , "2" , 100)
        o2=k2.replace("حقوق تا ۶ میلیون تومان" , "6" , 100)
        list5.append(o2)
    ff=len(list5)
    salery2=list5.count("2")
    salery6=list5.count("6")
    salery8=list5.count("8")
    salery12=list5.count("12")
    salery13=list5.count("13")
    sumSALARY=2*salery2 + 6*salery6 + 8*salery8 + 12*salery12 + 13*salery13
    AVERAGE=sumSALARY/ff
    #print("***Average salary is " , AVERAGE , "milion toman***")
    AVERAGE1.configure(text=" {} milion toman $".format( round(AVERAGE)), bg='white')
def JavaScript():
    from bs4 import BeautifulSoup
    import requests
    URL="https://quera.ir/careers/jobs?technologies=javascript"
    URL2="https://quera.ir/careers/jobs?technologies=javascript&page=2"
    URL3="https://quera.ir/careers/jobs?technologies=javascript&page=3"
    URL4="https://quera.ir/careers/jobs?technologies=javascript&page=4"
    URL5="https://quera.ir/careers/jobs?technologies=javascript&page=5"
    response = requests.get(url=URL)
    response2 = requests.get(url=URL2)
    response3 = requests.get(url=URL3)
    response4 = requests.get(url=URL4)
    response5 = requests.get(url=URL5)
    soup=BeautifulSoup(response.content , 'html.parser')
    soup2=BeautifulSoup(response2.content , 'html.parser')
    soup3=BeautifulSoup(response3.content , 'html.parser')
    soup4=BeautifulSoup(response4.content , 'html.parser')
    soup5=BeautifulSoup(response5.content , 'html.parser')
    list3=[]
    result1=soup.findAll('span',class_="job-level hide-in-mobile")
    result22=soup2.findAll('span',class_="job-level hide-in-mobile")
    result33=soup3.findAll('span',class_="job-level hide-in-mobile")
    result44=soup4.findAll('span',class_="job-level hide-in-mobile")
    result55=soup5.findAll('span',class_="job-level hide-in-mobile")
    for result1 in result1:
        m= result1.text.strip()
        list3.append(m)
    for result22 in result22:
        u= result22.text.strip()
        list3.append(u)
    for result33 in result33:
        LL= result33.text.strip()
        list3.append(LL)
    for result44 in result44:
        LL1= result44.text.strip()
        list3.append(LL1)
    for result55 in result55:
        LL11= result55.text.strip()
        list3.append(LL11)
    z=len(list3)
    #print("***Number of job opportunities*** is :" , z)
    jobOppotunities.configure(text=" {}".format(round(z)) , bg='white')
    #print("_________________Experience level_________________")
    sumSENIOR=list3.count('ارشد (Senior)')
    sumSENIOR=(sumSENIOR/z)*100
    #print("Senior percentage is :" , sumSENIOR,"%")
    senior.configure(text=" {} %".format(round(sumSENIOR)), bg='white')
    sumJONIOR=list3.count('جوان (Junior)')
    sumJONIOR=(sumJONIOR/z)*100
    #print("Jonior percentage is :" , sumJONIOR , "%")
    jonior.configure(text="  {} %".format(round(sumJONIOR)), bg='white')
    sumINTERN=list3.count('کارآموز (Intern)')
    sumINTERN=(sumINTERN/z)*100
    #print("Intern percentage is :" , sumINTERN , "%")
    intern1.configure(text=" {} %".format(round(sumINTERN)), bg='white')
    sumLeader=list3.count('راهبر فنی (Lead)')
    sumLeader=(sumLeader/z)*100
    #print("Lead percentage is :" , sumLeader, "%")
    leader.configure(text="{} %".format(round(sumLeader)), bg='white')
    #print("__________________work time______________________ ")
    #print("Job collabs for front_end developers: ")
    result2=soup.findAll('span',class_="job-collab")
    result21=soup2.findAll('span',class_="job-collab")
    result222=soup3.findAll('span',class_="job-collab")
    result23=soup4.findAll('span',class_="job-collab")
    result24=soup5.findAll('span',class_="job-collab")
    list4=[]
    for result2 in result2:
        l= result2.text.strip()
        t=l.replace("پروژه‌ای" , "PROJEH" , 100)
        c=t.replace("تمام‌وقت" , "tamamvaght", 100 )
        q=c.replace("پاره‌وقت" , "parehVaght" , 100)
        list4.append(q)
    for result21 in result21:
        l1= result21.text.strip()
        t1=l1.replace("پروژه‌ای" , "PROJEH" , 100)
        c1=t1.replace("تمام‌وقت" , "tamamvaght", 100 )
        q1=c1.replace("پاره‌وقت" , "parehVaght" , 100)
        list4.append(q1)
    for result222 in result222:
        l2= result222.text.strip()
        t2=l2.replace("پروژه‌ای" , "PROJEH" , 100)
        c2=t2.replace("تمام‌وقت" , "tamamvaght", 100 )
        q2=c2.replace("پاره‌وقت" , "parehVaght" , 100)
        list4.append(q2)
    for result23 in result23:
        l3= result23.text.strip()
        t3=l3.replace("پروژه‌ای" , "PROJEH" , 100)
        c3=t3.replace("تمام‌وقت" , "tamamvaght", 100 )
        q3=c3.replace("پاره‌وقت" , "parehVaght" , 100)
        list4.append(q3)
    for result24 in result24:
        l4= result24.text.strip()
        t4=l4.replace("پروژه‌ای" , "PROJEH" , 100)
        c4=t4.replace("تمام‌وقت" , "tamamvaght", 100 )
        q4=c4.replace("پاره‌وقت" , "parehVaght" , 100)
        list4.append(q4)
    ww=len(list4)
    sumPROJEH=list4.count('PROJEH')
    ProjectPercantage=(sumPROJEH/ww)*100
    #print("project Percenatge  is : " , ProjectPercantage)
    project.configure(text=" {} %".format(round(ProjectPercantage)), bg='white' )
    sumTAMAMVAGHT=list4.count('tamamvaght')
    TamamVAGHT=(sumTAMAMVAGHT/ww)*100
    #print("Full_time Percentage is  : " , TamamVAGHT)
    Fullttime.configure(text=" {} %".format(round(TamamVAGHT)), bg='white')
    sumPAREHVAGHT=list4.count("parehVaght")
    PARTtime=(sumPAREHVAGHT/ww)*100
    #print("Part-time percentage is : " ,PARTtime )
    PARTttime.configure(text="{} %".format(round(PARTtime)), bg='white')
    #print("__________________Skills needed to work____________________")
    result3=soup.findAll('span', class_="ui small tech label main")
    result31=soup2.findAll('span', class_="ui small tech label main")
    result32=soup3.findAll('span', class_="ui small tech label main")
    result333=soup4.findAll('span', class_="ui small tech label main")
    result34=soup5.findAll('span', class_="ui small tech label main")
    list1=[]
    for result3 in result3:
        a=  result3.text.strip()
        c=list1.append(a)
    for result31 in result31:
        a1=  result31.text.strip()
        c1=list1.append(a1)
    for result32 in result32:
        a2=  result3.text.strip()
        c2=list1.append(a2)
    for result333 in result333:
        a3=  result333.text.strip()
        c3=list1.append(a3)
    for result34 in result34:
        a4=  result34.text.strip()
        c4=list1.append(a4)
    w=len(list1)
    dict1=dict() 
    for elem in list1:
        if elem in dict1:
            dict1[elem] += 1
        else:
            dict1[elem] = 1  
    dict1 = { key:value for key, value in dict1.items() if value > 1}
    values=dict1.values()
    max1=max(values)
    KEY1=list(dict1.keys())[list(dict1.values()).index(max1)]
    newdict1=dict1.pop(KEY1)
    #print(dict1)
    values2=dict1.values()
    max2=max(values2)
    KEY2=list(dict1.keys())[list(dict1.values()).index(max2)]
    newdict1=dict1.pop(KEY2)
    values3=dict1.values()
    max3=max(values3)
    KEY3=list(dict1.keys())[list(dict1.values()).index(max3)]
    newdict1=dict1.pop(KEY3)
    listkey=[KEY1 ,KEY2 ,  KEY3]
    skillss.configure(text="{} ".format(listkey), bg='white')
    #print(listkey)
    #print("_______________Average salary______________")
    result4=soup.findAll('span', class_="job-salary")
    result41=soup2.findAll('span', class_="job-salary")
    result42=soup3.findAll('span', class_="job-salary")
    result43=soup4.findAll('span', class_="job-salary")
    result444=soup5.findAll('span', class_="job-salary")
    list5=[]
    for result4 in result4:
        M= result4.text.strip()
        A=M.replace("حقوق بیش از ۱۲ میلیون تومان" , "13" , 100)
        c=A.replace('حقوق تا ۱۲ میلیون تومان' , "12", 100 )
        y=c.replace("حقوق تا ۸ میلیون تومان" , "8" , 100)
        k=y.replace("حقوق تا ۲ میلیون تومان" , "2" , 100)
        o=k.replace("حقوق تا ۶ میلیون تومان" , "6" , 100)
        list5.append(o)
    for result41 in result41:
        M1= result41.text.strip()
        A1=M1.replace("حقوق بیش از ۱۲ میلیون تومان" , "13" , 100)
        c1=A1.replace('حقوق تا ۱۲ میلیون تومان' , "12", 100 )
        y1=c1.replace("حقوق تا ۸ میلیون تومان" , "8" , 100)
        k1=y1.replace("حقوق تا ۲ میلیون تومان" , "2" , 100)
        o1=k1.replace("حقوق تا ۶ میلیون تومان" , "6" , 100)
        list5.append(o1)
    for result42 in result42:
        M2= result42.text.strip()
        A2=M2.replace("حقوق بیش از ۱۲ میلیون تومان" , "13" , 100)
        c2=A2.replace('حقوق تا ۱۲ میلیون تومان' , "12", 100 )
        y2=c2.replace("حقوق تا ۸ میلیون تومان" , "8" , 100)
        k2=y2.replace("حقوق تا ۲ میلیون تومان" , "2" , 100)
        o2=k2.replace("حقوق تا ۶ میلیون تومان" , "6" , 100)
        list5.append(o2)
    for result43 in result43:
        M3= result43.text.strip()
        A3=M3.replace("حقوق بیش از ۱۲ میلیون تومان" , "13" , 100)
        c3=A3.replace('حقوق تا ۱۲ میلیون تومان' , "12", 100 )
        y3=c3.replace("حقوق تا ۸ میلیون تومان" , "8" , 100)
        k3=y3.replace("حقوق تا ۲ میلیون تومان" , "2" , 100)
        o3=k3.replace("حقوق تا ۶ میلیون تومان" , "6" , 100)
        list5.append(o3)
    for result444 in result444:
        M4= result444.text.strip()
        A4=M4.replace("حقوق بیش از ۱۲ میلیون تومان" , "13" , 100)
        c4=A4.replace('حقوق تا ۱۲ میلیون تومان' , "12", 100 )
        y4=c4.replace("حقوق تا ۸ میلیون تومان" , "8" , 100)
        k4=y4.replace("حقوق تا ۲ میلیون تومان" , "2" , 100)
        o4=k4.replace("حقوق تا ۶ میلیون تومان" , "6" , 100)
        list5.append(o4)
    ff=len(list5)
    salery2=list5.count("2")
    salery6=list5.count("6")
    salery8=list5.count("8")
    salery12=list5.count("12")
    salery13=list5.count("13")
    sumSALARY=2*salery2 + 6*salery6 + 8*salery8 + 12*salery12 + 13*salery13
    AVERAGE=sumSALARY/ff
    #print("***Average salary is " , AVERAGE , "milion toman***")
    AVERAGE1.configure(text=" {} milion toman $".format(round( AVERAGE)), bg='white')
def React():
    from bs4 import BeautifulSoup
    import requests
    URL="https://quera.ir/careers/jobs?technologies=reactjs"
    URL2="https://quera.ir/careers/jobs?technologies=reactjs&page=2"
    URL3="https://quera.ir/careers/jobs?technologies=reactjs&page=3"
    URL4="https://quera.ir/careers/jobs?technologies=reactjs&page=4"
    URL5="https://quera.ir/careers/jobs?technologies=reactjs&page=5"
    response = requests.get(url=URL)
    response2 = requests.get(url=URL2)
    response3 = requests.get(url=URL3)
    response4 = requests.get(url=URL4)
    response5 = requests.get(url=URL5)
    soup=BeautifulSoup(response.content , 'html.parser')
    soup2=BeautifulSoup(response2.content , 'html.parser')
    soup3=BeautifulSoup(response3.content , 'html.parser')
    soup4=BeautifulSoup(response4.content , 'html.parser')
    soup5=BeautifulSoup(response5.content , 'html.parser')
    list3=[]
    result1=soup.findAll('span',class_="job-level hide-in-mobile")
    result22=soup2.findAll('span',class_="job-level hide-in-mobile")
    result33=soup3.findAll('span',class_="job-level hide-in-mobile")
    result44=soup4.findAll('span',class_="job-level hide-in-mobile")
    result55=soup5.findAll('span',class_="job-level hide-in-mobile")
    for result1 in result1:
        m= result1.text.strip()
        list3.append(m)
    for result22 in result22:
        u= result22.text.strip()
        list3.append(u)
    for result33 in result33:
        LL= result33.text.strip()
        list3.append(LL)
    for result44 in result44:
        LL1= result44.text.strip()
        list3.append(LL1)
    for result55 in result55:
        LL11= result55.text.strip()
        list3.append(LL11)
    z=len(list3)
    #print("***Number of job opportunities*** is :" , z)
    jobOppotunities.configure(text=" {}".format(round(z)) , bg='white')
    #print("_________________Experience level_________________")
    sumSENIOR=list3.count('ارشد (Senior)')
    sumSENIOR=(sumSENIOR/z)*100
    #print("Senior percentage is :" , sumSENIOR,"%")
    senior.configure(text=" {} %".format(round(sumSENIOR)), bg='white')
    sumJONIOR=list3.count('جوان (Junior)')
    sumJONIOR=(sumJONIOR/z)*100
    #print("Jonior percentage is :" , sumJONIOR , "%")
    jonior.configure(text="  {} %".format(round(sumJONIOR)), bg='white')
    sumINTERN=list3.count('کارآموز (Intern)')
    sumINTERN=(sumINTERN/z)*100
    #print("Intern percentage is :" , sumINTERN , "%")
    intern1.configure(text=" {} %".format(round(sumINTERN)), bg='white')
    sumLeader=list3.count('راهبر فنی (Lead)')
    sumLeader=(sumLeader/z)*100
    #print("Lead percentage is :" , sumLeader, "%")
    leader.configure(text="{} %".format(round(sumLeader)), bg='white')
    #print("__________________work time______________________ ")
    result2=soup.findAll('span',class_="job-collab")
    result21=soup2.findAll('span',class_="job-collab")
    result222=soup3.findAll('span',class_="job-collab")
    result23=soup4.findAll('span',class_="job-collab")
    result24=soup5.findAll('span',class_="job-collab")
    list4=[]
    for result2 in result2:
        l= result2.text.strip()
        t=l.replace("پروژه‌ای" , "PROJEH" , 100)
        c=t.replace("تمام‌وقت" , "tamamvaght", 100 )
        q=c.replace("پاره‌وقت" , "parehVaght" , 100)
        list4.append(q)
    for result21 in result21:
        l1= result21.text.strip()
        t1=l1.replace("پروژه‌ای" , "PROJEH" , 100)
        c1=t1.replace("تمام‌وقت" , "tamamvaght", 100 )
        q1=c1.replace("پاره‌وقت" , "parehVaght" , 100)
        list4.append(q1)
    for result222 in result222:
        l2= result222.text.strip()
        t2=l2.replace("پروژه‌ای" , "PROJEH" , 100)
        c2=t2.replace("تمام‌وقت" , "tamamvaght", 100 )
        q2=c2.replace("پاره‌وقت" , "parehVaght" , 100)
        list4.append(q2)
    for result23 in result23:
        l3= result23.text.strip()
        t3=l3.replace("پروژه‌ای" , "PROJEH" , 100)
        c3=t3.replace("تمام‌وقت" , "tamamvaght", 100 )
        q3=c3.replace("پاره‌وقت" , "parehVaght" , 100)
        list4.append(q3)
    for result24 in result24:
        l4= result24.text.strip()
        t4=l4.replace("پروژه‌ای" , "PROJEH" , 100)
        c4=t4.replace("تمام‌وقت" , "tamamvaght", 100 )
        q4=c4.replace("پاره‌وقت" , "parehVaght" , 100)
        list4.append(q4)
    ww=len(list4)
    sumPROJEH=list4.count('PROJEH')
    ProjectPercantage=(sumPROJEH/ww)*100
    #print("project Percenatge  is : " , ProjectPercantage)
    project.configure(text=" {} %".format(round(ProjectPercantage)), bg='white' )
    sumTAMAMVAGHT=list4.count('tamamvaght')
    TamamVAGHT=(sumTAMAMVAGHT/ww)*100
    #print("Full_time Percentage is  : " , TamamVAGHT)
    Fullttime.configure(text=" {} %".format(round(TamamVAGHT)), bg='white')
    sumPAREHVAGHT=list4.count("parehVaght")
    PARTtime=(sumPAREHVAGHT/ww)*100
    #print("Part-time percentage is : " ,PARTtime )
    PARTttime.configure(text="{} %".format(round(PARTtime)), bg='white')
    #print("__________________Skills needed to work____________________")
    result3=soup.findAll('span', class_="ui small tech label main")
    result31=soup2.findAll('span', class_="ui small tech label main")
    result32=soup3.findAll('span', class_="ui small tech label main")
    result333=soup4.findAll('span', class_="ui small tech label main")
    result34=soup5.findAll('span', class_="ui small tech label main")
    list1=[]
    for result3 in result3:
        a=  result3.text.strip()
        c=list1.append(a)
    for result31 in result31:
        a1=  result31.text.strip()
        c1=list1.append(a1)
    for result32 in result32:
        a2=  result3.text.strip()
        c2=list1.append(a2)
    for result333 in result333:
        a3=  result333.text.strip()
        c3=list1.append(a3)
    for result34 in result34:
        a4=  result34.text.strip()
        c4=list1.append(a4)
    w=len(list1)
    dict1=dict() 
    for elem in list1:
        if elem in dict1:
            dict1[elem] += 1
        else:
            dict1[elem] = 1  
    dict1 = { key:value for key, value in dict1.items() if value > 1}
    values=dict1.values()
    max1=max(values)
    KEY1=list(dict1.keys())[list(dict1.values()).index(max1)]
    newdict1=dict1.pop(KEY1)
    #print(dict1)
    values2=dict1.values()
    max2=max(values2)
    KEY2=list(dict1.keys())[list(dict1.values()).index(max2)]
    newdict1=dict1.pop(KEY2)
    values3=dict1.values()
    max3=max(values3)
    KEY3=list(dict1.keys())[list(dict1.values()).index(max3)]
    newdict1=dict1.pop(KEY3)
    listkey=[KEY1 ,KEY2 ,  KEY3]
    skillss.configure(text="{} ".format(listkey), bg='white')
    #print(listkey)
    #print("_______________Average salary______________")
    result4=soup.findAll('span', class_="job-salary")
    result41=soup2.findAll('span', class_="job-salary")
    result42=soup3.findAll('span', class_="job-salary")
    result43=soup4.findAll('span', class_="job-salary")
    result444=soup5.findAll('span', class_="job-salary")
    list5=[]
    for result4 in result4:
        M= result4.text.strip()
        A=M.replace("حقوق بیش از ۱۲ میلیون تومان" , "13" , 100)
        c=A.replace('حقوق تا ۱۲ میلیون تومان' , "12", 100 )
        y=c.replace("حقوق تا ۸ میلیون تومان" , "8" , 100)
        k=y.replace("حقوق تا ۲ میلیون تومان" , "2" , 100)
        o=k.replace("حقوق تا ۶ میلیون تومان" , "6" , 100)
        list5.append(o)
    for result41 in result41:
        M1= result41.text.strip()
        A1=M1.replace("حقوق بیش از ۱۲ میلیون تومان" , "13" , 100)
        c1=A1.replace('حقوق تا ۱۲ میلیون تومان' , "12", 100 )
        y1=c1.replace("حقوق تا ۸ میلیون تومان" , "8" , 100)
        k1=y1.replace("حقوق تا ۲ میلیون تومان" , "2" , 100)
        o1=k1.replace("حقوق تا ۶ میلیون تومان" , "6" , 100)
        list5.append(o1)
    for result42 in result42:
        M2= result42.text.strip()
        A2=M2.replace("حقوق بیش از ۱۲ میلیون تومان" , "13" , 100)
        c2=A2.replace('حقوق تا ۱۲ میلیون تومان' , "12", 100 )
        y2=c2.replace("حقوق تا ۸ میلیون تومان" , "8" , 100)
        k2=y2.replace("حقوق تا ۲ میلیون تومان" , "2" , 100)
        o2=k2.replace("حقوق تا ۶ میلیون تومان" , "6" , 100)
        list5.append(o2)
    for result43 in result43:
        M3= result43.text.strip()
        A3=M3.replace("حقوق بیش از ۱۲ میلیون تومان" , "13" , 100)
        c3=A3.replace('حقوق تا ۱۲ میلیون تومان' , "12", 100 )
        y3=c3.replace("حقوق تا ۸ میلیون تومان" , "8" , 100)
        k3=y3.replace("حقوق تا ۲ میلیون تومان" , "2" , 100)
        o3=k3.replace("حقوق تا ۶ میلیون تومان" , "6" , 100)
        list5.append(o3)
    for result444 in result444:
        M4= result444.text.strip()
        A4=M4.replace("حقوق بیش از ۱۲ میلیون تومان" , "13" , 100)
        c4=A4.replace('حقوق تا ۱۲ میلیون تومان' , "12", 100 )
        y4=c4.replace("حقوق تا ۸ میلیون تومان" , "8" , 100)
        k4=y4.replace("حقوق تا ۲ میلیون تومان" , "2" , 100)
        o4=k4.replace("حقوق تا ۶ میلیون تومان" , "6" , 100)
        list5.append(o4)
    ff=len(list5)
    salery2=list5.count("2")
    salery6=list5.count("6")
    salery8=list5.count("8")
    salery12=list5.count("12")
    salery13=list5.count("13")
    sumSALARY=2*salery2 + 6*salery6 + 8*salery8 + 12*salery12 + 13*salery13
    AVERAGE=sumSALARY/ff
    #print("***Average salary is " , AVERAGE , "milion toman***")
    AVERAGE1.configure(text=" {} milion toman $".format( round(AVERAGE)), bg='white')
def Python():
    from bs4 import BeautifulSoup
    import requests
    URL="https://quera.ir/careers/jobs?technologies=python"
    URL2="https://quera.ir/careers/jobs?technologies=python&page=2"
    URL3="https://quera.ir/careers/jobs?technologies=python&page=3"
    URL4="https://quera.ir/careers/jobs?technologies=python&page=4"
    URL5="https://quera.ir/careers/jobs?technologies=python&page=5"
    response = requests.get(url=URL)
    response2 = requests.get(url=URL2)
    response3 = requests.get(url=URL3)
    response4 = requests.get(url=URL4)
    response5 = requests.get(url=URL5)
    soup=BeautifulSoup(response.content , 'html.parser')
    soup2=BeautifulSoup(response2.content , 'html.parser')
    soup3=BeautifulSoup(response3.content , 'html.parser')
    soup4=BeautifulSoup(response4.content , 'html.parser')
    soup5=BeautifulSoup(response5.content , 'html.parser')
    list3=[]
    result1=soup.findAll('span',class_="job-level hide-in-mobile")
    result22=soup2.findAll('span',class_="job-level hide-in-mobile")
    result33=soup3.findAll('span',class_="job-level hide-in-mobile")
    result44=soup4.findAll('span',class_="job-level hide-in-mobile")
    result55=soup5.findAll('span',class_="job-level hide-in-mobile")
    for result1 in result1:
        m= result1.text.strip()
        list3.append(m)
    for result22 in result22:
        u= result22.text.strip()
        list3.append(u)
    for result33 in result33:
        LL= result33.text.strip()
        list3.append(LL)
    for result44 in result44:
        LL1= result44.text.strip()
        list3.append(LL1)
    for result55 in result55:
        LL11= result55.text.strip()
        list3.append(LL11)
    z=len(list3)
    #print("***Number of job opportunities*** is :" , z)
    jobOppotunities.configure(text=" {}".format(round(z)) , bg='white')
    #print("_________________Experience level_________________")
    sumSENIOR=list3.count('ارشد (Senior)')
    sumSENIOR=(sumSENIOR/z)*100
    #print("Senior percentage is :" , sumSENIOR,"%")
    senior.configure(text=" {} %".format(round(sumSENIOR)), bg='white')
    sumJONIOR=list3.count('جوان (Junior)')
    sumJONIOR=(sumJONIOR/z)*100
    #print("Jonior percentage is :" , sumJONIOR , "%")
    jonior.configure(text="  {} %".format(round(sumJONIOR)), bg='white')
    sumINTERN=list3.count('کارآموز (Intern)')
    sumINTERN=(sumINTERN/z)*100
    #print("Intern percentage is :" , sumINTERN , "%")
    intern1.configure(text=" {} %".format(round(sumINTERN)), bg='white')
    sumLeader=list3.count('راهبر فنی (Lead)')
    sumLeader=(sumLeader/z)*100
    #print("Lead percentage is :" , sumLeader, "%")
    leader.configure(text="{} %".format(round(sumLeader)), bg='white')
    #print("__________________work time______________________ ")
    result2=soup.findAll('span',class_="job-collab")
    result21=soup2.findAll('span',class_="job-collab")
    result222=soup3.findAll('span',class_="job-collab")
    result23=soup4.findAll('span',class_="job-collab")
    result24=soup5.findAll('span',class_="job-collab")
    list4=[]
    for result2 in result2:
        l= result2.text.strip()
        t=l.replace("پروژه‌ای" , "PROJEH" , 100)
        c=t.replace("تمام‌وقت" , "tamamvaght", 100 )
        q=c.replace("پاره‌وقت" , "parehVaght" , 100)
        list4.append(q)
    for result21 in result21:
        l1= result21.text.strip()
        t1=l1.replace("پروژه‌ای" , "PROJEH" , 100)
        c1=t1.replace("تمام‌وقت" , "tamamvaght", 100 )
        q1=c1.replace("پاره‌وقت" , "parehVaght" , 100)
        list4.append(q1)
    for result222 in result222:
        l2= result222.text.strip()
        t2=l2.replace("پروژه‌ای" , "PROJEH" , 100)
        c2=t2.replace("تمام‌وقت" , "tamamvaght", 100 )
        q2=c2.replace("پاره‌وقت" , "parehVaght" , 100)
        list4.append(q2)
    for result23 in result23:
        l3= result23.text.strip()
        t3=l3.replace("پروژه‌ای" , "PROJEH" , 100)
        c3=t3.replace("تمام‌وقت" , "tamamvaght", 100 )
        q3=c3.replace("پاره‌وقت" , "parehVaght" , 100)
        list4.append(q3)
    for result24 in result24:
        l4= result24.text.strip()
        t4=l4.replace("پروژه‌ای" , "PROJEH" , 100)
        c4=t4.replace("تمام‌وقت" , "tamamvaght", 100 )
        q4=c4.replace("پاره‌وقت" , "parehVaght" , 100)
        list4.append(q4)
    ww=len(list4)
    sumPROJEH=list4.count('PROJEH')
    ProjectPercantage=(sumPROJEH/ww)*100
    #print("project Percenatge  is : " , ProjectPercantage)
    project.configure(text=" {} %".format(round(ProjectPercantage)), bg='white' )
    sumTAMAMVAGHT=list4.count('tamamvaght')
    TamamVAGHT=(sumTAMAMVAGHT/ww)*100
    #print("Full_time Percentage is  : " , TamamVAGHT)
    Fullttime.configure(text=" {} %".format(round(TamamVAGHT)), bg='white')
    sumPAREHVAGHT=list4.count("parehVaght")
    PARTtime=(sumPAREHVAGHT/ww)*100
    #print("Part-time percentage is : " ,PARTtime )
    PARTttime.configure(text="{} %".format(round(PARTtime)), bg='white')
    #print("__________________Skills needed to work____________________")
    result3=soup.findAll('span', class_="ui small tech label main")
    result31=soup2.findAll('span', class_="ui small tech label main")
    result32=soup3.findAll('span', class_="ui small tech label main")
    result333=soup4.findAll('span', class_="ui small tech label main")
    result34=soup5.findAll('span', class_="ui small tech label main")
    list1=[]
    for result3 in result3:
        a=  result3.text.strip()
        c=list1.append(a)
    for result31 in result31:
        a1=  result31.text.strip()
        c1=list1.append(a1)
    for result32 in result32:
        a2=  result3.text.strip()
        c2=list1.append(a2)
    for result333 in result333:
        a3=  result333.text.strip()
        c3=list1.append(a3)
    for result34 in result34:
        a4=  result34.text.strip()
        c4=list1.append(a4)
    w=len(list1)
    dict1=dict() 
    for elem in list1:
        if elem in dict1:
            dict1[elem] += 1
        else:
            dict1[elem] = 1  
    dict1 = { key:value for key, value in dict1.items() if value > 1}
    values=dict1.values()
    max1=max(values)
    KEY1=list(dict1.keys())[list(dict1.values()).index(max1)]
    newdict1=dict1.pop(KEY1)
    #print(dict1)
    values2=dict1.values()
    max2=max(values2)
    KEY2=list(dict1.keys())[list(dict1.values()).index(max2)]
    newdict1=dict1.pop(KEY2)
    values3=dict1.values()
    max3=max(values3)
    KEY3=list(dict1.keys())[list(dict1.values()).index(max3)]
    newdict1=dict1.pop(KEY3)
    listkey=[KEY1 ,KEY2 ,  KEY3]
    skillss.configure(text="{} ".format(listkey), bg='white')
    #print(listkey)
    #print("_______________Average salary______________")
    result4=soup.findAll('span', class_="job-salary")
    result41=soup2.findAll('span', class_="job-salary")
    result42=soup3.findAll('span', class_="job-salary")
    result43=soup4.findAll('span', class_="job-salary")
    result444=soup5.findAll('span', class_="job-salary")
    list5=[]
    for result4 in result4:
        M= result4.text.strip()
        A=M.replace("حقوق بیش از ۱۲ میلیون تومان" , "13" , 100)
        c=A.replace('حقوق تا ۱۲ میلیون تومان' , "12", 100 )
        y=c.replace("حقوق تا ۸ میلیون تومان" , "8" , 100)
        k=y.replace("حقوق تا ۲ میلیون تومان" , "2" , 100)
        o=k.replace("حقوق تا ۶ میلیون تومان" , "6" , 100)
        list5.append(o)
    for result41 in result41:
        M1= result41.text.strip()
        A1=M1.replace("حقوق بیش از ۱۲ میلیون تومان" , "13" , 100)
        c1=A1.replace('حقوق تا ۱۲ میلیون تومان' , "12", 100 )
        y1=c1.replace("حقوق تا ۸ میلیون تومان" , "8" , 100)
        k1=y1.replace("حقوق تا ۲ میلیون تومان" , "2" , 100)
        o1=k1.replace("حقوق تا ۶ میلیون تومان" , "6" , 100)
        list5.append(o1)
    for result42 in result42:
        M2= result42.text.strip()
        A2=M2.replace("حقوق بیش از ۱۲ میلیون تومان" , "13" , 100)
        c2=A2.replace('حقوق تا ۱۲ میلیون تومان' , "12", 100 )
        y2=c2.replace("حقوق تا ۸ میلیون تومان" , "8" , 100)
        k2=y2.replace("حقوق تا ۲ میلیون تومان" , "2" , 100)
        o2=k2.replace("حقوق تا ۶ میلیون تومان" , "6" , 100)
        list5.append(o2)
    for result43 in result43:
        M3= result43.text.strip()
        A3=M3.replace("حقوق بیش از ۱۲ میلیون تومان" , "13" , 100)
        c3=A3.replace('حقوق تا ۱۲ میلیون تومان' , "12", 100 )
        y3=c3.replace("حقوق تا ۸ میلیون تومان" , "8" , 100)
        k3=y3.replace("حقوق تا ۲ میلیون تومان" , "2" , 100)
        o3=k3.replace("حقوق تا ۶ میلیون تومان" , "6" , 100)
        list5.append(o3)
    for result444 in result444:
        M4= result444.text.strip()
        A4=M4.replace("حقوق بیش از ۱۲ میلیون تومان" , "13" , 100)
        c4=A4.replace('حقوق تا ۱۲ میلیون تومان' , "12", 100 )
        y4=c4.replace("حقوق تا ۸ میلیون تومان" , "8" , 100)
        k4=y4.replace("حقوق تا ۲ میلیون تومان" , "2" , 100)
        o4=k4.replace("حقوق تا ۶ میلیون تومان" , "6" , 100)
        list5.append(o4)
    ff=len(list5)
    salery2=list5.count("2")
    salery6=list5.count("6")
    salery8=list5.count("8")
    salery12=list5.count("12")
    salery13=list5.count("13")
    sumSALARY=2*salery2 + 6*salery6 + 8*salery8 + 12*salery12 + 13*salery13
    AVERAGE=sumSALARY/ff
    #print("***Average salary is " , AVERAGE , "milion toman***")
    AVERAGE1.configure(text=" {} milion toman $".format( round(AVERAGE)), bg='white')
def PHP():
    from bs4 import BeautifulSoup
    import requests
    URL="https://quera.ir/careers/jobs?technologies=php"
    URL2="https://quera.ir/careers/jobs?technologies=php&page=2"
    URL3="https://quera.ir/careers/jobs?technologies=php&page=3"
    URL4="https://quera.ir/careers/jobs?technologies=php&page=4"
    response = requests.get(url=URL)
    response2 = requests.get(url=URL2)
    response3 = requests.get(url=URL3)
    response4 = requests.get(url=URL4)
    soup=BeautifulSoup(response.content , 'html.parser')
    soup2=BeautifulSoup(response2.content , 'html.parser')
    soup3=BeautifulSoup(response3.content , 'html.parser')
    soup4=BeautifulSoup(response4.content , 'html.parser')
    list3=[]
    result1=soup.findAll('span',class_="job-level hide-in-mobile")
    result22=soup2.findAll('span',class_="job-level hide-in-mobile")
    result33=soup3.findAll('span',class_="job-level hide-in-mobile")
    result44=soup4.findAll('span',class_="job-level hide-in-mobile")
    for result1 in result1:
        m= result1.text.strip()
        list3.append(m)
    for result22 in result22:
        u= result22.text.strip()
        list3.append(u)
    for result33 in result33:
        LL= result33.text.strip()
        list3.append(LL)
    for result44 in result44:
        LL1= result44.text.strip()
        list3.append(LL1)
    z=len(list3)
    #print("***Number of job opportunities*** is :" , z)
    jobOppotunities.configure(text=" {}".format(round(z)) , bg='white')
    #print("_________________Experience level_________________")
    sumSENIOR=list3.count('ارشد (Senior)')
    sumSENIOR=(sumSENIOR/z)*100
    #print("Senior percentage is :" , sumSENIOR,"%")
    senior.configure(text=" {} %".format(round(sumSENIOR)), bg='white')
    sumJONIOR=list3.count('جوان (Junior)')
    sumJONIOR=(sumJONIOR/z)*100
    #print("Jonior percentage is :" , sumJONIOR , "%")
    jonior.configure(text="  {} %".format(round(sumJONIOR)), bg='white')
    sumINTERN=list3.count('کارآموز (Intern)')
    sumINTERN=(sumINTERN/z)*100
    #print("Intern percentage is :" , sumINTERN , "%")
    intern1.configure(text=" {} %".format(round(sumINTERN)), bg='white')
    sumLeader=list3.count('راهبر فنی (Lead)')
    sumLeader=(sumLeader/z)*100
    #print("Lead percentage is :" , sumLeader, "%")
    leader.configure(text="{} %".format(round(sumLeader)), bg='white')
    #print("__________________work time______________________ ")
    result2=soup.findAll('span',class_="job-collab")
    result21=soup2.findAll('span',class_="job-collab")
    result222=soup3.findAll('span',class_="job-collab")
    result23=soup4.findAll('span',class_="job-collab")
    list4=[]
    for result2 in result2:
        l= result2.text.strip()
        t=l.replace("پروژه‌ای" , "PROJEH" , 100)
        c=t.replace("تمام‌وقت" , "tamamvaght", 100 )
        q=c.replace("پاره‌وقت" , "parehVaght" , 100)
        list4.append(q)
    for result21 in result21:
        l1= result21.text.strip()
        t1=l1.replace("پروژه‌ای" , "PROJEH" , 100)
        c1=t1.replace("تمام‌وقت" , "tamamvaght", 100 )
        q1=c1.replace("پاره‌وقت" , "parehVaght" , 100)
        list4.append(q1)
    for result222 in result222:
        l2= result222.text.strip()
        t2=l2.replace("پروژه‌ای" , "PROJEH" , 100)
        c2=t2.replace("تمام‌وقت" , "tamamvaght", 100 )
        q2=c2.replace("پاره‌وقت" , "parehVaght" , 100)
        list4.append(q2)
    for result23 in result23:
        l3= result23.text.strip()
        t3=l3.replace("پروژه‌ای" , "PROJEH" , 100)
        c3=t3.replace("تمام‌وقت" , "tamamvaght", 100 )
        q3=c3.replace("پاره‌وقت" , "parehVaght" , 100)
        list4.append(q3)
    ww=len(list4)
    sumPROJEH=list4.count('PROJEH')
    ProjectPercantage=(sumPROJEH/ww)*100
    #print("project Percenatge  is : " , ProjectPercantage)
    project.configure(text=" {} %".format(round(ProjectPercantage)), bg='white' )
    sumTAMAMVAGHT=list4.count('tamamvaght')
    TamamVAGHT=(sumTAMAMVAGHT/ww)*100
    #print("Full_time Percentage is  : " , TamamVAGHT)
    Fullttime.configure(text=" {} %".format(round(TamamVAGHT)), bg='white')
    sumPAREHVAGHT=list4.count("parehVaght")
    PARTtime=(sumPAREHVAGHT/ww)*100
    #print("Part-time percentage is : " ,PARTtime )
    PARTttime.configure(text="{} %".format(round(PARTtime)), bg='white')
    #print("__________________Skills needed to work____________________")
    result3=soup.findAll('span', class_="ui small tech label main")
    result31=soup2.findAll('span', class_="ui small tech label main")
    result32=soup3.findAll('span', class_="ui small tech label main")
    result333=soup4.findAll('span', class_="ui small tech label main")
    list1=[]
    for result3 in result3:
        a=  result3.text.strip()
        c=list1.append(a)
    for result31 in result31:
        a1=  result31.text.strip()
        c1=list1.append(a1)
    for result32 in result32:
        a2=  result3.text.strip()
        c2=list1.append(a2)
    for result333 in result333:
        a3=  result333.text.strip()
        c3=list1.append(a3)
    w=len(list1)
    dict1=dict() 
    for elem in list1:
        if elem in dict1:
            dict1[elem] += 1
        else:
            dict1[elem] = 1  
    dict1 = { key:value for key, value in dict1.items() if value > 1}
    values=dict1.values()
    max1=max(values)
    KEY1=list(dict1.keys())[list(dict1.values()).index(max1)]
    newdict1=dict1.pop(KEY1)
    #print(dict1)
    values2=dict1.values()
    max2=max(values2)
    KEY2=list(dict1.keys())[list(dict1.values()).index(max2)]
    newdict1=dict1.pop(KEY2)
    values3=dict1.values()
    max3=max(values3)
    KEY3=list(dict1.keys())[list(dict1.values()).index(max3)]
    newdict1=dict1.pop(KEY3)
    listkey=[KEY1 ,KEY2 ,  KEY3]
    skillss.configure(text="{} ".format(listkey), bg='white')
    #print(listkey)
    #print("_______________Average salary______________")
    result4=soup.findAll('span', class_="job-salary")
    result41=soup2.findAll('span', class_="job-salary")
    result42=soup3.findAll('span', class_="job-salary")
    result43=soup4.findAll('span', class_="job-salary")
    list5=[]
    for result4 in result4:
        M= result4.text.strip()
        A=M.replace("حقوق بیش از ۱۲ میلیون تومان" , "13" , 100)
        c=A.replace('حقوق تا ۱۲ میلیون تومان' , "12", 100 )
        y=c.replace("حقوق تا ۸ میلیون تومان" , "8" , 100)
        k=y.replace("حقوق تا ۲ میلیون تومان" , "2" , 100)
        o=k.replace("حقوق تا ۶ میلیون تومان" , "6" , 100)
        list5.append(o)
    for result41 in result41:
        M1= result41.text.strip()
        A1=M1.replace("حقوق بیش از ۱۲ میلیون تومان" , "13" , 100)
        c1=A1.replace('حقوق تا ۱۲ میلیون تومان' , "12", 100 )
        y1=c1.replace("حقوق تا ۸ میلیون تومان" , "8" , 100)
        k1=y1.replace("حقوق تا ۲ میلیون تومان" , "2" , 100)
        o1=k1.replace("حقوق تا ۶ میلیون تومان" , "6" , 100)
        list5.append(o1)
    for result42 in result42:
        M2= result42.text.strip()
        A2=M2.replace("حقوق بیش از ۱۲ میلیون تومان" , "13" , 100)
        c2=A2.replace('حقوق تا ۱۲ میلیون تومان' , "12", 100 )
        y2=c2.replace("حقوق تا ۸ میلیون تومان" , "8" , 100)
        k2=y2.replace("حقوق تا ۲ میلیون تومان" , "2" , 100)
        o2=k2.replace("حقوق تا ۶ میلیون تومان" , "6" , 100)
        list5.append(o2)
    for result43 in result43:
        M3= result43.text.strip()
        A3=M3.replace("حقوق بیش از ۱۲ میلیون تومان" , "13" , 100)
        c3=A3.replace('حقوق تا ۱۲ میلیون تومان' , "12", 100 )
        y3=c3.replace("حقوق تا ۸ میلیون تومان" , "8" , 100)
        k3=y3.replace("حقوق تا ۲ میلیون تومان" , "2" , 100)
        o3=k3.replace("حقوق تا ۶ میلیون تومان" , "6" , 100)
        list5.append(o3)
    ff=len(list5)
    salery2=list5.count("2")
    salery6=list5.count("6")
    salery8=list5.count("8")
    salery12=list5.count("12")
    salery13=list5.count("13")
    sumSALARY=2*salery2 + 6*salery6 + 8*salery8 + 12*salery12 + 13*salery13
    AVERAGE=sumSALARY/ff
    #print("***Average salary is " , AVERAGE , "milion toman***")
    AVERAGE1.configure(text=" {} milion toman $".format( round(AVERAGE)), bg='white')
def Java():
    from bs4 import BeautifulSoup
    import requests
    URL="https://quera.ir/careers/jobs?technologies=java"
    URL2="https://quera.ir/careers/jobs?technologies=java&page=2"
    URL3="https://quera.ir/careers/jobs?technologies=java&page=3"
    response = requests.get(url=URL)
    response2 = requests.get(url=URL2)
    response3 = requests.get(url=URL3)
    soup=BeautifulSoup(response.content , 'html.parser')
    soup2=BeautifulSoup(response2.content , 'html.parser')
    soup3=BeautifulSoup(response3.content , 'html.parser')
    list3=[]
    result1=soup.findAll('span',class_="job-level hide-in-mobile")
    result22=soup2.findAll('span',class_="job-level hide-in-mobile")
    result33=soup3.findAll('span',class_="job-level hide-in-mobile")
    for result1 in result1:
        m= result1.text.strip()
        list3.append(m)
    for result22 in result22:
        u= result22.text.strip()
        list3.append(u)
    for result33 in result33:
        LL= result33.text.strip()
        list3.append(LL)
    z=len(list3)
    #print("***Number of job opportunities*** is :" , z)
    jobOppotunities.configure(text=" {}".format(round(z)) , bg='white')
    #print("_________________Experience level_________________")
    sumSENIOR=list3.count('ارشد (Senior)')
    sumSENIOR=(sumSENIOR/z)*100
    #print("Senior percentage is :" , sumSENIOR,"%")
    senior.configure(text=" {} %".format(round(sumSENIOR)), bg='white')
    sumJONIOR=list3.count('جوان (Junior)')
    sumJONIOR=(sumJONIOR/z)*100
    #print("Jonior percentage is :" , sumJONIOR , "%")
    jonior.configure(text="  {} %".format(round(sumJONIOR)), bg='white')
    sumINTERN=list3.count('کارآموز (Intern)')
    sumINTERN=(sumINTERN/z)*100
    #print("Intern percentage is :" , sumINTERN , "%")
    intern1.configure(text=" {} %".format(round(sumINTERN)), bg='white')
    sumLeader=list3.count('راهبر فنی (Lead)')
    sumLeader=(sumLeader/z)*100
    #print("Lead percentage is :" , sumLeader, "%")
    leader.configure(text="{} %".format(round(sumLeader)), bg='white')
    #print("__________________work time______________________ ")
    result2=soup.findAll('span',class_="job-collab")
    result21=soup2.findAll('span',class_="job-collab")
    result222=soup3.findAll('span',class_="job-collab")
    list4=[]
    for result2 in result2:
        l= result2.text.strip()
        t=l.replace("پروژه‌ای" , "PROJEH" , 100)
        c=t.replace("تمام‌وقت" , "tamamvaght", 100 )
        q=c.replace("پاره‌وقت" , "parehVaght" , 100)
        list4.append(q)
    for result21 in result21:
        l1= result21.text.strip()
        t1=l1.replace("پروژه‌ای" , "PROJEH" , 100)
        c1=t1.replace("تمام‌وقت" , "tamamvaght", 100 )
        q1=c1.replace("پاره‌وقت" , "parehVaght" , 100)
        list4.append(q1)
    for result222 in result222:
        l2= result222.text.strip()
        t2=l2.replace("پروژه‌ای" , "PROJEH" , 100)
        c2=t2.replace("تمام‌وقت" , "tamamvaght", 100 )
        q2=c2.replace("پاره‌وقت" , "parehVaght" , 100)
        list4.append(q2)
    ww=len(list4)
    sumPROJEH=list4.count('PROJEH')
    ProjectPercantage=(sumPROJEH/ww)*100
    #print("project Percenatge  is : " , ProjectPercantage)
    project.configure(text=" {} %".format(round(ProjectPercantage)), bg='white' )
    sumTAMAMVAGHT=list4.count('tamamvaght')
    TamamVAGHT=(sumTAMAMVAGHT/ww)*100
    #print("Full_time Percentage is  : " , TamamVAGHT)
    Fullttime.configure(text=" {} %".format(round(TamamVAGHT)), bg='white')
    sumPAREHVAGHT=list4.count("parehVaght")
    PARTtime=(sumPAREHVAGHT/ww)*100
    #print("Part-time percentage is : " ,PARTtime )
    PARTttime.configure(text="{} %".format(round(PARTtime)), bg='white')
    #print("__________________Skills needed to work____________________")
    result3=soup.findAll('span', class_="ui small tech label main")
    result31=soup2.findAll('span', class_="ui small tech label main")
    result32=soup3.findAll('span', class_="ui small tech label main")
    list1=[]
    for result3 in result3:
        a=  result3.text.strip()
        c=list1.append(a)
    for result31 in result31:
        a1=  result31.text.strip()
        c1=list1.append(a1)
    for result32 in result32:
        a2=  result3.text.strip()
        c2=list1.append(a2)
    w=len(list1)
    dict1=dict() 
    for elem in list1:
        if elem in dict1:
            dict1[elem] += 1
        else:
            dict1[elem] = 1  
    dict1 = { key:value for key, value in dict1.items() if value > 1}
    values=dict1.values()
    max1=max(values)
    KEY1=list(dict1.keys())[list(dict1.values()).index(max1)]
    newdict1=dict1.pop(KEY1)
    #print(dict1)
    values2=dict1.values()
    max2=max(values2)
    KEY2=list(dict1.keys())[list(dict1.values()).index(max2)]
    newdict1=dict1.pop(KEY2)
    values3=dict1.values()
    max3=max(values3)
    KEY3=list(dict1.keys())[list(dict1.values()).index(max3)]
    #a=listkey.append(KEY1)
    newdict1=dict1.pop(KEY3)
    listkey=[KEY1 ,KEY2 ,  KEY3]
    skillss.configure(text="{} ".format(listkey), bg='white')
    #print(listkey)
    #print("_______________Average salary______________")
    result4=soup.findAll('span', class_="job-salary")
    result41=soup2.findAll('span', class_="job-salary")
    result42=soup3.findAll('span', class_="job-salary")
    list5=[]
    for result4 in result4:
        M= result4.text.strip()
        A=M.replace("حقوق بیش از ۱۲ میلیون تومان" , "13" , 100)
        c=A.replace('حقوق تا ۱۲ میلیون تومان' , "12", 100 )
        y=c.replace("حقوق تا ۸ میلیون تومان" , "8" , 100)
        k=y.replace("حقوق تا ۲ میلیون تومان" , "2" , 100)
        o=k.replace("حقوق تا ۶ میلیون تومان" , "6" , 100)
        list5.append(o)
    for result41 in result41:
        M1= result41.text.strip()
        A1=M1.replace("حقوق بیش از ۱۲ میلیون تومان" , "13" , 100)
        c1=A1.replace('حقوق تا ۱۲ میلیون تومان' , "12", 100 )
        y1=c1.replace("حقوق تا ۸ میلیون تومان" , "8" , 100)
        k1=y1.replace("حقوق تا ۲ میلیون تومان" , "2" , 100)
        o1=k1.replace("حقوق تا ۶ میلیون تومان" , "6" , 100)
        list5.append(o1)
    for result42 in result42:
        M2= result42.text.strip()
        A2=M2.replace("حقوق بیش از ۱۲ میلیون تومان" , "13" , 100)
        c2=A2.replace('حقوق تا ۱۲ میلیون تومان' , "12", 100 )
        y2=c2.replace("حقوق تا ۸ میلیون تومان" , "8" , 100)
        k2=y2.replace("حقوق تا ۲ میلیون تومان" , "2" , 100)
        o2=k2.replace("حقوق تا ۶ میلیون تومان" , "6" , 100)
        list5.append(o2)
    ff=len(list5)
    salery2=list5.count("2")
    salery6=list5.count("6")
    salery8=list5.count("8")
    salery12=list5.count("12")
    salery13=list5.count("13")
    sumSALARY=2*salery2 + 6*salery6 + 8*salery8 + 12*salery12 + 13*salery13
    AVERAGE=sumSALARY/ff
    #print("***Average salary is " , AVERAGE , "milion toman***")
    AVERAGE1.configure(text=" {} milion toman $".format( round(AVERAGE)), bg='white')
def CSharp():
    from bs4 import BeautifulSoup
    import requests
    URL="https://quera.ir/careers/jobs?technologies=c%23"
    URL2="https://quera.ir/careers/jobs?technologies=c%23&page=2"
    URL3="https://quera.ir/careers/jobs?technologies=c%23&page=3"
    response = requests.get(url=URL)
    response2 = requests.get(url=URL2)
    response3 = requests.get(url=URL3)
    soup=BeautifulSoup(response.content , 'html.parser')
    soup2=BeautifulSoup(response2.content , 'html.parser')
    soup3=BeautifulSoup(response3.content , 'html.parser')
    list3=[]
    result1=soup.findAll('span',class_="job-level hide-in-mobile")
    result22=soup2.findAll('span',class_="job-level hide-in-mobile")
    result33=soup3.findAll('span',class_="job-level hide-in-mobile")
    for result1 in result1:
        m= result1.text.strip()
        list3.append(m)
    for result22 in result22:
        u= result22.text.strip()
        list3.append(u)
    for result33 in result33:
        LL= result33.text.strip()
        list3.append(LL)
    z=len(list3)
    #print("***Number of job opportunities*** is :" , z)
    jobOppotunities.configure(text=" {}".format(round(z)) , bg='white')
    #print("_________________Experience level_________________")
    sumSENIOR=list3.count('ارشد (Senior)')
    sumSENIOR=(sumSENIOR/z)*100
    #print("Senior percentage is :" , sumSENIOR,"%")
    senior.configure(text=" {} %".format(round(sumSENIOR)), bg='white')
    sumJONIOR=list3.count('جوان (Junior)')
    sumJONIOR=(sumJONIOR/z)*100
    #print("Jonior percentage is :" , sumJONIOR , "%")
    jonior.configure(text="  {} %".format(round(sumJONIOR)), bg='white')
    sumINTERN=list3.count('کارآموز (Intern)')
    sumINTERN=(sumINTERN/z)*100
    #print("Intern percentage is :" , sumINTERN , "%")
    intern1.configure(text=" {} %".format(round(sumINTERN)), bg='white')
    sumLeader=list3.count('راهبر فنی (Lead)')
    sumLeader=(sumLeader/z)*100
    #print("Lead percentage is :" , sumLeader, "%")
    leader.configure(text="{} %".format(round(sumLeader)), bg='white')
    #print("__________________work time______________________ ")
    #print("Job collabs for front_end developers: ")
    result2=soup.findAll('span',class_="job-collab")
    result21=soup2.findAll('span',class_="job-collab")
    result222=soup3.findAll('span',class_="job-collab")
    list4=[]
    for result2 in result2:
        l= result2.text.strip()
        t=l.replace("پروژه‌ای" , "PROJEH" , 100)
        c=t.replace("تمام‌وقت" , "tamamvaght", 100 )
        q=c.replace("پاره‌وقت" , "parehVaght" , 100)
        list4.append(q)
    for result21 in result21:
        l1= result21.text.strip()
        t1=l1.replace("پروژه‌ای" , "PROJEH" , 100)
        c1=t1.replace("تمام‌وقت" , "tamamvaght", 100 )
        q1=c1.replace("پاره‌وقت" , "parehVaght" , 100)
        list4.append(q1)
    for result222 in result222:
        l2= result222.text.strip()
        t2=l2.replace("پروژه‌ای" , "PROJEH" , 100)
        c2=t2.replace("تمام‌وقت" , "tamamvaght", 100 )
        q2=c2.replace("پاره‌وقت" , "parehVaght" , 100)
        list4.append(q2)
    ww=len(list4)
    sumPROJEH=list4.count('PROJEH')
    ProjectPercantage=(sumPROJEH/ww)*100
    #print("project Percenatge  is : " , ProjectPercantage)
    project.configure(text=" {} %".format(round(ProjectPercantage)), bg='white' )
    sumTAMAMVAGHT=list4.count('tamamvaght')
    TamamVAGHT=(sumTAMAMVAGHT/ww)*100
    #print("Full_time Percentage is  : " , TamamVAGHT)
    Fullttime.configure(text=" {} %".format(round(TamamVAGHT)), bg='white')
    sumPAREHVAGHT=list4.count("parehVaght")
    PARTtime=(sumPAREHVAGHT/ww)*100
    #print("Part-time percentage is : " ,PARTtime )
    PARTttime.configure(text="{} %".format(round(PARTtime)), bg='white')
    #print("__________________Skills needed to work____________________")
    result3=soup.findAll('span', class_="ui small tech label main")
    result31=soup2.findAll('span', class_="ui small tech label main")
    result32=soup3.findAll('span', class_="ui small tech label main")
    list1=[]
    for result3 in result3:
        a=  result3.text.strip()
        c=list1.append(a)
    for result31 in result31:
        a1=  result31.text.strip()
        c1=list1.append(a1)
    for result32 in result32:
        a2=  result3.text.strip()
        c2=list1.append(a2)
    w=len(list1)
    dict1=dict() 
    for elem in list1:
        if elem in dict1:
            dict1[elem] += 1
        else:
            dict1[elem] = 1  
    dict1 = { key:value for key, value in dict1.items() if value > 1}
    values=dict1.values()
    max1=max(values)
    KEY1=list(dict1.keys())[list(dict1.values()).index(max1)]
    newdict1=dict1.pop(KEY1)
    #print(dict1)
    values2=dict1.values()
    max2=max(values2)
    KEY2=list(dict1.keys())[list(dict1.values()).index(max2)]
    newdict1=dict1.pop(KEY2)
    values3=dict1.values()
    max3=max(values3)
    KEY3=list(dict1.keys())[list(dict1.values()).index(max3)]
    newdict1=dict1.pop(KEY3)
    listkey=[KEY1 ,KEY2 ,  KEY3]
    skillss.configure(text="{} ".format(listkey), bg='white')
    #print(listkey)
    #print("_______________Average salary______________")
    result4=soup.findAll('span', class_="job-salary")
    result41=soup2.findAll('span', class_="job-salary")
    result42=soup3.findAll('span', class_="job-salary")
    list5=[]
    for result4 in result4:
        M= result4.text.strip()
        A=M.replace("حقوق بیش از ۱۲ میلیون تومان" , "13" , 100)
        c=A.replace('حقوق تا ۱۲ میلیون تومان' , "12", 100 )
        y=c.replace("حقوق تا ۸ میلیون تومان" , "8" , 100)
        k=y.replace("حقوق تا ۲ میلیون تومان" , "2" , 100)
        o=k.replace("حقوق تا ۶ میلیون تومان" , "6" , 100)
        list5.append(o)
    for result41 in result41:
        M1= result41.text.strip()
        A1=M1.replace("حقوق بیش از ۱۲ میلیون تومان" , "13" , 100)
        c1=A1.replace('حقوق تا ۱۲ میلیون تومان' , "12", 100 )
        y1=c1.replace("حقوق تا ۸ میلیون تومان" , "8" , 100)
        k1=y1.replace("حقوق تا ۲ میلیون تومان" , "2" , 100)
        o1=k1.replace("حقوق تا ۶ میلیون تومان" , "6" , 100)
        list5.append(o1)
    for result42 in result42:
        M2= result42.text.strip()
        A2=M2.replace("حقوق بیش از ۱۲ میلیون تومان" , "13" , 100)
        c2=A2.replace('حقوق تا ۱۲ میلیون تومان' , "12", 100 )
        y2=c2.replace("حقوق تا ۸ میلیون تومان" , "8" , 100)
        k2=y2.replace("حقوق تا ۲ میلیون تومان" , "2" , 100)
        o2=k2.replace("حقوق تا ۶ میلیون تومان" , "6" , 100)
        list5.append(o2)
    ff=len(list5)
    salery2=list5.count("2")
    salery6=list5.count("6")
    salery8=list5.count("8")
    salery12=list5.count("12")
    salery13=list5.count("13")
    sumSALARY=2*salery2 + 6*salery6 + 8*salery8 + 12*salery12 + 13*salery13
    AVERAGE=sumSALARY/ff
    #print("***Average salary is " , AVERAGE , "milion toman***")
    AVERAGE1.configure(text=" {} milion toman $".format( round(AVERAGE)), bg='white')
def linux():
    from bs4 import BeautifulSoup
    import requests
    URL="https://quera.ir/careers/jobs?technologies=linux"
    URL2="https://quera.ir/careers/jobs?technologies=linux&page=2"
    response = requests.get(url=URL)
    response2 = requests.get(url=URL2)
    soup=BeautifulSoup(response.content , 'html.parser')
    soup2=BeautifulSoup(response2.content , 'html.parser')
    list3=[]
    result1=soup.findAll('span',class_="job-level hide-in-mobile")
    result22=soup2.findAll('span',class_="job-level hide-in-mobile")
    for result1 in result1:
        m= result1.text.strip()
        list3.append(m)
    for result22 in result22:
        u= result22.text.strip()
        list3.append(u)
    z=len(list3)
    #print("***Number of job opportunities*** is :" , z)
    jobOppotunities.configure(text=" {}".format(z) , bg='white')
    #print("_________________Experience level_________________")
    sumSENIOR=list3.count('ارشد (Senior)')
    sumSENIOR=(sumSENIOR/z)*100
    #print("Senior percentage is :" ,sumSENIOR,"%")
    senior.configure(text=" {} %".format( round(sumSENIOR)), bg='white')
    sumJONIOR=list3.count('جوان (Junior)')
    sumJONIOR=(sumJONIOR/z)*100
    #print("Jonior percentage is :" , sumJONIOR , "%")
    jonior.configure(text="  {} %".format( round(sumJONIOR)), bg='white')
    sumINTERN=list3.count('کارآموز (Intern)')
    sumINTERN=(sumINTERN/z)*100
    #print("Intern percentage is :" , sumINTERN , "%")
    intern1.configure(text=" {} %".format( round(sumINTERN)), bg='white')
    sumLeader=list3.count('راهبر فنی (Lead)')
    sumLeader=(sumLeader/z)*100
    #print("Lead percentage is :" , sumLeader, "%")
    leader.configure(text="{} %".format( round(sumLeader)), bg='white')
    #print("__________________work time______________________ ")
    #print("Job collabs for linux developers: ")
    result2=soup.findAll('span',class_="job-collab")
    result21=soup2.findAll('span',class_="job-collab")
    list4=[]
    for result2 in result2:
        l= result2.text.strip()
        t=l.replace("پروژه‌ای" , "PROJEH" , 100)
        c=t.replace("تمام‌وقت" , "tamamvaght", 100 )
        q=c.replace("پاره‌وقت" , "parehVaght" , 100)
        list4.append(q)
    for result21 in result21:
        l1= result21.text.strip()
        t1=l1.replace("پروژه‌ای" , "PROJEH" , 100)
        c1=t1.replace("تمام‌وقت" , "tamamvaght", 100 )
        q1=c1.replace("پاره‌وقت" , "parehVaght" , 100)
        list4.append(q1)
    ww=len(list4)
    sumPROJEH=list4.count('PROJEH')
    ProjectPercantage=(sumPROJEH/ww)*100
    #print("project Percenatge  is : " , ProjectPercantage)
    project.configure(text=" {} %".format( round(ProjectPercantage)), bg='white' )
    sumTAMAMVAGHT=list4.count('tamamvaght')
    TamamVAGHT=(sumTAMAMVAGHT/ww)*100
    #print("Full_time Percentage is  : " , TamamVAGHT)
    Fullttime.configure(text=" {} %".format( round(TamamVAGHT)), bg='white')
    sumPAREHVAGHT=list4.count("parehVaght")
    PARTtime=(sumPAREHVAGHT/ww)*100
    #print("Part-time percentage is : " ,PARTtime )
    PARTttime.configure(text="{} %".format( round(PARTtime)), bg='white')
    #print("__________________Skills needed to work____________________")
    result3=soup.findAll('span', class_="ui small tech label main")
    result31=soup2.findAll('span', class_="ui small tech label main")
    list1=[]
    for result3 in result3:
        a=  result3.text.strip()
        c=list1.append(a)
    for result31 in result31:
        a1=  result31.text.strip()
        c1=list1.append(a1)
    w=len(list1)
    dict1=dict() 
    for elem in list1:
        if elem in dict1:
            dict1[elem] += 1
        else:
            dict1[elem] = 1  
    dict1 = { key:value for key, value in dict1.items() if value > 1}
    values=dict1.values()
    max1=max(values)
    KEY1=list(dict1.keys())[list(dict1.values()).index(max1)]
    newdict1=dict1.pop(KEY1)
    #print(dict1)
    values2=dict1.values()
    max2=max(values2)
    KEY2=list(dict1.keys())[list(dict1.values()).index(max2)]
    newdict1=dict1.pop(KEY2)
    values3=dict1.values()
    max3=max(values3)
    KEY3=list(dict1.keys())[list(dict1.values()).index(max3)]
    newdict1=dict1.pop(KEY3)
    listkey=[KEY1 ,KEY2 ,  KEY3]
    skillss.configure(text="{} ".format(listkey), bg='white')
    #print(listkey)
    #print("_______________Average salary______________")
    result4=soup.findAll('span', class_="job-salary")
    result41=soup2.findAll('span', class_="job-salary")
    list5=[]
    for result4 in result4:
        M= result4.text.strip()
        A=M.replace("حقوق بیش از ۱۲ میلیون تومان" , "13" , 100)
        c=A.replace('حقوق تا ۱۲ میلیون تومان' , "12", 100 )
        y=c.replace("حقوق تا ۸ میلیون تومان" , "8" , 100)
        k=y.replace("حقوق تا ۲ میلیون تومان" , "2" , 100)
        o=k.replace("حقوق تا ۶ میلیون تومان" , "6" , 100)
        list5.append(o)
    for result41 in result41:
        M1= result41.text.strip()
        A1=M1.replace("حقوق بیش از ۱۲ میلیون تومان" , "13" , 100)
        c1=A1.replace('حقوق تا ۱۲ میلیون تومان' , "12", 100 )
        y1=c1.replace("حقوق تا ۸ میلیون تومان" , "8" , 100)
        k1=y1.replace("حقوق تا ۲ میلیون تومان" , "2" , 100)
        o1=k1.replace("حقوق تا ۶ میلیون تومان" , "6" , 100)
        list5.append(o1)
    ff=len(list5)
    salery2=list5.count("2")
    salery6=list5.count("6")
    salery8=list5.count("8")
    salery12=list5.count("12")
    salery13=list5.count("13")
    sumSALARY=2*salery2 + 6*salery6 + 8*salery8 + 12*salery12 + 13*salery13
    AVERAGE=sumSALARY/ff
    #print("***Average salary is " , AVERAGE , "milion toman***")
    AVERAGE1.configure(text=" {} milion toman $".format(  round(AVERAGE)), bg='white')
window = Tk()
window.title("WebScraping")
window.minsize(800,700)
window.maxsize(800,650)
window.geometry('400x500')
window.resizable(width=False , height=False)
window.configure(bg="gray30")
Label(window,text="________WEB    SCRAPING________" , font=(" Caslon",32 ) , foreground="black" , background="gray30").pack()
a=Label(window,text="_____Please Enter which techology are you looking for?_____" , font=("Tahoma",16 ) , foreground="black" , background="gray30").pack()
menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=window.quit)
window .config(menu=menubar)
btnbackend = Button(window)
btnfrontend = Button(window)
btnmobile = Button(window)
btnjavascript = Button(window)
btnreact = Button(window)
btnpython = Button(window)
btnphp = Button(window)
btnjava = Button(window)
btncsharp = Button(window)
btnlinux = Button(window)
btnbackend.configure(text="1.Back_end",font=("Brandon Grotesque",10 ),bg="orange2",fg="black" , command=BackEnd)
btnfrontend.configure(text="2.Front_end",font=("Brandon Grotesque",10 ),bg="orange2",fg="black" ,command=FrontEnd)
btnmobile.configure(text="3.Mobile",font=("Brandon Grotesque",10 ),bg="cyan",fg="black" , command=Mobile)
btnjavascript.configure(text="4.JavaScript",font=("Brandon Grotesque",10 ),bg="cyan2",fg="black" , command=JavaScript)
btnreact.configure(text="5.React",font=("Brandon Grotesque",10 ),bg="orange2",fg="black" , command=React)
btnpython.configure(text="6.python",font=("Brandon Grotesque",10 ),bg="orange2",fg="black" , command=Python)
btnphp.configure(text="7.PHP",font=("Brandon Grotesque",10 ),bg="cyan",fg="black" , command=PHP)
btnjava.configure(text="8.JAVA",font=("Brandon Grotesque",10 ),bg="cyan",fg="black" , command=Java)
btncsharp.configure(text="9.CSharp",font=("Brandon Grotesque",10 ),bg="orange2",fg="black" , command=CSharp)
btnlinux.configure(text=" 10.Linux ",font=("Brandon Grotesque",10 ),bg="orange2",fg="black" , command=linux)
btnbackend.pack()
btnbackend.place (x=3, y=100)
btnfrontend.pack()
btnfrontend.place (x=85, y=100)
btnmobile.pack()
btnmobile.place (x=165, y=100)
btnjavascript.pack()
btnjavascript.place (x=225, y=100)
btnreact.pack()
btnreact.place (x=305, y=100)
btnpython.pack()
btnpython.place (x=454, y=100)
btnphp.pack()
btnphp.place (x=517, y=100)
btnjava.pack()
btnjava.place (x=568, y=100)
btncsharp.pack()
btncsharp.place (x=625, y=100)
btnlinux.pack()
btnlinux.place (x=690, y=100)
btnquit = Button(window)
btninfo=Button(window)
text1=Label(window,text="__________Experience level_________" , font=("Brandon Grotesque",12) , foreground="white" , background="gray30")
text1.pack()
text1.place (x=11, y=140)
seniortext=Label(window,text="senior percentage:" , font=("Brandon Grotesque",16 ) , foreground="white" , background="gray30")
seniortext.pack()
seniortext.place (x=1, y=170)
seniorblank=seniortext=Label(window,text=" "*30, font=("Brandon Grotesque",16 ) , foreground="white" , background="white")
seniorblank.pack()
seniorblank.place(x=180, y=170)
joniortext=Label(window,text="jonior percentage:" , font=("Brandon Grotesque",16 ) , foreground="white" , background="gray30")
joniortext.pack()
joniortext.place (x=1, y=205)
joniortext=seniortext=Label(window,text=" "*30 , font=("Brandon Grotesque",16 ) , foreground="white" , background="white")
joniortext.pack()
joniortext.place(x=180, y=205)
interntext=Label(window,text="intern percentage:" , font=("Brandon Grotesque",16 ) , foreground="white" , background="gray30")
interntext.pack()
interntext.place (x=1, y=240)
interntext=seniortext=Label(window,text=" "*30, font=("Brandon Grotesque",16 ) , foreground="white" , background="white")
interntext.pack()
interntext.place(x=180, y=240)
leadertext=Label(window,text="Lead percentage:" , font=("Brandon Grotesque",16 ) , foreground="white" , background="gray30")
leadertext.pack()
leadertext.place (x=1, y=275)
leaderblank=Label(window,text=" "*30 , font=("Brandon Grotesque",16 ) , foreground="white" , background="white")
leaderblank.pack()
leaderblank.place(x=180, y=275)
text2=Label(window,text="____________Work Time___________" , font=("Brandon Grotesque",12) , foreground="white" , background="gray30")
text21=Label(window,text="_*___*___*____*___*___*___*__*___*____*___*___" , font=("Brandon Grotesque",10) , foreground="white" , background="gray30")
text2.pack()
text2.place (x=390, y=140)
text21.pack()
text21.place(x=390, y=163)
projecttext=Label(window,text="project percentage:" , font=("Brandon Grotesque",16 ) , foreground="white" , background="gray30")
projecttext.pack()
projecttext.place (x=380, y=200)
projectblank=Label(window,text=" "*36, font=("Brandon Grotesque",16 ) , foreground="white" , background="white")
projectblank.pack()
projectblank.place(x=570, y=200)
fulltimetext=Label(window,text="Fulltime percentage:" , font=("Brandon Grotesque",16 ) , foreground="white" , background="gray30")
fulltimetext.pack()
fulltimetext.place (x=380, y=235)
fulltimeblank=Label(window,text=" "*35 , font=("Brandon Grotesque",16 ) , foreground="white" , background="white")
fulltimeblank.pack()
fulltimeblank.place(x=575, y=235)
parttimetext=Label(window,text="Parttime percentage:" , font=("Brandon Grotesque",16 ) , foreground="white" , background="gray30")
parttimetext.pack()
parttimetext.place (x=380, y=270)
parttimeblank=Label(window,text=" "*34, font=("Brandon Grotesque",16 ) , foreground="white" , background="white")
parttimeblank.pack()
parttimeblank.place(x=583, y=270)
jobOppotunitiestext=Label(window,text="Number of job opportunities:" , font=("Brandon Grotesque",16 ) , foreground="white" , background="gray30")
jobOppotunitiestext.pack()
jobOppotunitiestext.place (x=0, y=370)
jobOppotunitiesblank=Label(window,text=" "*80 , font=("Brandon Grotesque",16 ) , foreground="blue" , background="white")
jobOppotunitiesblank.pack()
jobOppotunitiesblank.place(x=265, y=370)
incometext=Label(window,text="Average income:" , font=("Brandon Grotesque",16 ) , foreground="white" , background="gray30")
incometext.pack()
incometext.place (x=0, y=405)
incomeblank=Label(window,text=" "*80 , font=("Brandon Grotesque",16 ) , foreground="blue" , background="white")
incomeblank.pack()
incomeblank.place(x=265, y=405)
skilltext=Label(window,text="Skills needed to work:" , font=("Brandon Grotesque",16 ) , foreground="white" , background="gray30")
skilltext.pack()
skilltext.place (x=0, y=440)
skillblank=Label(window,text=" "*80 , font=("Brandon Grotesque",16 ) , foreground="blue" , background="white")
skillblank.pack()
skillblank.place(x=265, y=440)
btnquit.configure(text="              EXIT              ",bg="turquoise2",fg="red" , command=window.quit)
btnquit.pack()
btnquit.place (x=580, y=550)
from tkinter import messagebox
def show_info():
   messagebox.showinfo("Show info", "This application helps you to find the information you need more easily from the Internet .By clicking on the name of each technology, you can find the job information you need ")
btninfo.configure(text="              guidance              ",bg="turquoise2",fg="red" , command=show_info)
btninfo.pack()
btninfo.place (x=400, y=550)
jobOppotunities=Label(window)
jobOppotunities.pack()
jobOppotunities.place (x=305, y=373)
senior=Label(window)
senior.pack()
senior.place (x=220, y=175)
jonior=Label(window)
jonior.pack()
jonior.place (x=220, y=210)
intern1=Label(window)
intern1.pack()
intern1.place (x=220, y=245)
leader=Label(window)
leader.pack()
leader.pack()
leader.place (x=220, y=280)
project=Label(window)
project.pack()
project.place (x=600, y=205)
Fullttime=Label(window)
Fullttime.pack()
Fullttime.place (x=600,  y=240)
PARTttime=Label(window)
PARTttime.pack()
PARTttime.place (x=583, y=270)
AVERAGE1=Label(window)
AVERAGE1.pack()
AVERAGE1.place (x=280, y=410)
skillss=Label(window)
skillss.pack()
skillss.place (x=265, y=445)
window.mainloop()
