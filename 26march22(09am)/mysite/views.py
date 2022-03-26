from ast import arg
from asyncio.windows_events import NULL
from statistics import multimode
from wsgiref.util import request_uri
from click import password_option
import cursor
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
import mysql.connector as sql
from datetime import datetime
from django.contrib import messages
now = datetime.now() # current date and time
date_time = now.strftime("%d/%m/%Y, %H:%M:%S")


def posted_job(request):
    args={}
    m = sql.connect(host='localhost', user='root',passwd='', database='JobShip')
    cursor = m.cursor()
    jai=request.session.get('login_id')    
    # c3 = """select * from pinned_job where job_applicant_id=23 """.format(request.session.get('job_applicant_id'))
    c3 = """select * from pinned_job where job_applicant_id='{}'""".format(jai)# jai means job application id
    cursor.execute(c3)
    t = tuple(cursor.fetchall())
    p = list(t)
    print(p)
    l=[]
    for i in range (0,len(p)):
        comp={}
        pt =list(p[i])
        comp['sno']=pt[0]
        comp['job_applicant_id']=pt[1]
        comp['job_id']=pt[2]
        comp['time']=pt[3]
        # here we fetched the job_id but we have to show the job description like home page
        # so we have to fetch the job from job id
        c4="""select * from job where job_id='{}'""".format(pt[2])
        cursor.execute(c4)
        t1 = tuple(cursor.fetchall())
        p1 = list(t1)
        pt1= list(p1[0])
        print("this is job at job_id= ",pt[2]," is ",pt1)
        comp['comp_name']=pt1[1]
        comp['jobdescription']=pt1[2]
        comp['jobtitle']=pt1[3]
        comp['skills']=pt1[4]
        comp['skills']=pt1[4]
        comp['joblocation_address']=pt1[5]
        comp['vacencies']=pt1[6]
        comp['domain']=pt1[7]
        comp['linkedin']=pt1[8]



        l.append(comp)
    # args['jobs']=l  
    print("this is l:",l)   
    args['jobs']=l
       


    
    
    if request.method=="POST":
        m = sql.connect(host='localhost', user='root',passwd='', database='JobShip')
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():
            if key == "job_applicant_id":
                job_applicant_id = value

            if key == "job_id":
                job_id = value
        print('job applicant id is :',job_applicant_id)        
        c1 = """INSERT INTO pinned_job Values('{}','{}', '{}','{}');""".format(0,job_applicant_id,job_id,date_time)    
        cursor.execute(c1)
        m.commit() 

    return render(request,'posted_job.html')



def post_job(request):
    m = sql.connect(host='localhost', user='root',passwd='', database='JobShip')
    cursor = m.cursor()
    d = request.POST
    for key, value in d.items():
        if key == "jobtitle":
                jobtitle = value
        if key == "jobdescription":
                jobdescription = value
        if key == "skills":
                skills = value
        if key == "joblocation_address":
                joblocation_address = value
        if key == "vacencies":
                vacencies = value
        if key == "company":
                company = value
        if key == "domain":
                domain = value
        if key == "linkedin":
                linkedin = value

               

    # c1 = """INSERT INTO pinned_job Values('{}','{}', '{}','{}');""".format(0,job_applicant_id,job_id,date_time)   
    
    c1 = """INSERT INTO job Values('{}','{}', '{}','{}','{}','{}','{}','{}','{}','{}');""".format(0,company,jobdescription ,jobtitle,skills,joblocation_address,vacencies,domain,linkedin,date_time)    
    cursor.execute(c1)
    m.commit() 

    return redirect('/home/')


def delete_pinned_job(request):
    m = sql.connect(host='localhost', user='root',
                        passwd='', database='JobShip')
    cursor = m.cursor()

    d = request.POST
    for key, value in d.items():
            if key == "deleted_job_id":
                deleted_job_id = value
            if key == "job_applicant_id":
                job_applicant_id = value
    sql_delete_query = """DELETE FROM `pinned_job` WHERE job_id='{}' and job_applicant_id='{}'""".format(deleted_job_id,job_applicant_id)
    cursor.execute(sql_delete_query)
       
    m.commit()

    if request.method=="GET" and request.session.get('set')=='yes':
        return redirect('/pinned_job')
    elif request.method=="GET" and request.session.get('set')!='yes':
        return redirect('/')
    else:
        return redirect('/pinned_job')

    return redirect('/pinned_job')

def pinned_job(request):
    args={}
    m = sql.connect(host='localhost', user='root',passwd='', database='JobShip')
    cursor = m.cursor()
    jai=request.session.get('job_applicant_id')    
    # c3 = """select * from pinned_job where job_applicant_id=23 """.format(request.session.get('job_applicant_id'))
    c3 = """select * from pinned_job where job_applicant_id='{}'""".format(jai)# jai means job application id
    cursor.execute(c3)
    t = tuple(cursor.fetchall())
    p = list(t)
    print(p)
    l=[]
    for i in range (0,len(p)):
        comp={}
        pt =list(p[i])
        comp['sno']=pt[0]
        comp['job_applicant_id']=pt[1]
        comp['job_id']=pt[2]
        comp['time']=pt[3]
        # here we fetched the job_id but we have to show the job description like home page
        # so we have to fetch the job from job id
        c4="""select * from job where job_id='{}'""".format(pt[2])
        cursor.execute(c4)
        t1 = tuple(cursor.fetchall())
        p1 = list(t1)
        pt1= list(p1[0])
        print("this is job at job_id= ",pt[2]," is ",pt1)
        comp['comp_name']=pt1[1]
        comp['jobdescription']=pt1[2]
        comp['jobtitle']=pt1[3]
        comp['skills']=pt1[4]
        comp['skills']=pt1[4]
        comp['joblocation_address']=pt1[5]
        comp['vacencies']=pt1[6]
        comp['domain']=pt1[7]
        comp['linkedin']=pt1[8]



        l.append(comp)
    # args['jobs']=l  
    print("this is l:",l)   
    args['jobs']=l
       


    
    
    if request.method=="POST":
        m = sql.connect(host='localhost', user='root',passwd='', database='JobShip')
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():
            if key == "job_applicant_id":
                job_applicant_id = value

            if key == "job_id":
                job_id = value
        print('job applicant id is :',job_applicant_id)        
        c1 = """INSERT INTO pinned_job Values('{}','{}', '{}','{}');""".format(0,job_applicant_id,job_id,date_time)    
        cursor.execute(c1)
        m.commit() 
        return redirect('/home/')  

    
            
    return render(request,'pinned_job.html',args)


def index(request):
    return render(request, 'index.html')
def home(request):
    m = sql.connect(host='localhost', user='root',
                        passwd='', database='JobShip')
    cursor = m.cursor()

    d = request.POST
    for key, value in d.items():
            if key == "email":
                em = value

            if key == "password":
                pwd = value
            if key =="q":
                q=value

    # c = "insert into job Values('job_id','company','jobdescription','jobtitle','skills','joblocation_address',current_timestamp(),'vacencies')"
    c = "select * from job order by job_id desc"
    # desc means it fetch the data in descending order

    cursor.execute(c)
    # m.commit() this is only for inserting the data
    t = tuple(cursor.fetchall())
    # for row in cursor:
    #     print(row)
    # a=[""]*11
    # print(t)
    p = list(t)
    args={'length':len(p)}

    # print(p)
    print("length of fetched data is :",len(p))
    # print("this is second index: ",p[1])
    # print("this is third index: ",p[2])
    # print("this is third index: ",list(p[2]))
    l=[]

    for i in range (0,len(p)):
        comp={}
        pt =list(p[i])
        comp['job_id']=pt[0]
        comp['name']=pt[1]
        comp['jobdescription']=pt[2]
        comp['jobtitle']=pt[3]
        comp['skills']=pt[4]
        comp['joblocation_address']=pt[5]
        comp['vacencies']=pt[6]
        comp['domain']=pt[7]
        comp['linkedin']=pt[8]
        
        # print(comp)
    # l.[i]=comp
        l.append(comp)
    #         print(pt[j],end=" | ")
    #         args[f"d{i}{j}"]=pt[j] #if you want to take individual element of a row as a key in dictonary
    #     # args[f"d{i}"]=pt #if you want to take a row as an array in one key of dictonary
        # print("it is pt :",pt)
            # it is pt : [4, 'company', 'jobdescription', 'jobtitle', 'skills', 'joblocation_address', datetime.datetime(2022, 3, 22, 18, 5, 21), 'vacencies']
# this is args:  {'length': 3}
    # print("This is list of dictonories : ",l)
    args['jobs']=l
    # data={}
    #     # l.append(pt)
    #     print('\n')

    # print(l[1])
    # args['data':l]
    # data={'':''}

    # print("this is args: ",args)
    
    # pt = p[0]
    # print(p[0])
    # print("hello")
    # ptp = list(pt)
    
    # print(ptp) 
    # print("this is first index: ",ptp[0])
    #how to pass list in dictonary
    #pehle hm list ki length pass karayege
    #phir loop ki help se args mai multiple element pass karayege
    # kyuki hme lenght pata hai to agle page (template) par bhi uski help se ek hi row ka data print kar lenge
    return render(request, 'home.html',args)


def login(request):
    em = ''
    pwd = ''

    if request.method == "POST":
        m = sql.connect(host='localhost', user='root',
                        passwd='', database='JobShip')
        cursor = m.cursor()

        d = request.POST
        for key, value in d.items():
            if key == "email":
                em = value

            if key == "password":
                pwd = value
            if key =="q":
                q=value

        c = "select id,firstname,lastname,college,degree,specialization,start_year,end_year from student where email='{}' and password='{}'".format(
            em, pwd)
        cursor.execute(c)
        t = tuple(cursor.fetchall())
        # for row in cursor:
        #     print(row)
        # a=[""]*11
        print(t)
       

        if t == ():
            return HttpResponse(""" <script> 
            alert('Invalid Cridential');
            window.location='/login/'
            </script>""")
        else:
            p = list(t)
            pt = p[0]
            print(p[0])
            print("hello")
            ptp = list(pt)
            print(ptp)  # it is a list of the data saved in database
            # print(ptp[0])
            name = (ptp[1]+" "+ptp[2])
            # args = {'name': name, 'college': ptp[2], 'degree': ptp[3],
                    # 'specialization': ptp[4], 'start_year': ptp[5], 'end_year': ptp[6]}
            request.session['name']=name
            request.session['job_applicant_id']=ptp[0]
            request.session['email']=em
            request.session['password']=pwd
            request.session['set']='yes' #this is for setting the condition of session(session is set to yes)
#if session is clkeared then the value of request.session.get['set']is not equal to yes 😍
            return redirect('/user/')
    return render(request, 'login.html')


def login_company(request):
    em = ''
    pwd = ''
    gargs={'name':request.session.get('name')}
    if request.method == "POST":
        m = sql.connect(host='localhost', user='root',
                        passwd='', database='JobShip')
        cursor = m.cursor()

        d = request.POST
        for key, value in d.items():
            if key == "company_email":
                em = value

            if key == "company_password":
                pwd = value
            # if key =="q":
            #     q=value

        c = "select company_id,company_name,domain,establish_year,type_of_company,location,linkedin from company where email='{}' and password='{}'".format(em, pwd)
        cursor.execute(c)
        t = tuple(cursor.fetchall())
        # for row in cursor:
        #     print(row)
        # a=[""]*11
        print(t)
       

        if t == ():
            return HttpResponse(""" <script> 
            alert('Invalid Cridential');
            window.location='/login/'
            </script>""")
        else:
            p = list(t)
            pt = p[0]
            print(p[0])
            print("hello")
            ptp = list(pt)
            print(ptp)  # it is a list of the data saved in database
            # print(ptp[0])
            request.session['name']=ptp[1]
            request.session['iscompany']='yes'
            request.session['login_id']=ptp[0]
            request.session['email']=em
            request.session['domain']=ptp[2]
            request.session['establish_year']=ptp[3]
            request.session['toc']=ptp[4]
            request.session['location']=ptp[5]
            request.session['linkedin']=ptp[6]
            request.session['set']='yes' #this is for setting the condition of session(session is set to yes)
#if session is clkeared then the value of request.session.get['set']is not equal to yes 😍
            return redirect('/company/')
    return render(request, 'login_company.html')


def company(request):
    id=request.session.get('email')
   
    # args = {'name': request.session.get('name'),'email':request.session.get('email')}
    def comp_info(id):
        m = sql.connect(host='localhost', user='root',passwd='', database='JobShip')
        cursor = m.cursor()
        q = """select name, location, email, domain, phone, summary,type_of_company , est_year ,about ,linkedin ,language_worked_with ,collab_tools ,opsys ,plateform_worked_with,honor_or_reward ,honor_or_reward_desc from comp_profile where email='{}'""".format(id)
        cursor.execute(q)
        t = tuple(cursor.fetchall())
        p = list(t)
        print(t)
        pt = p[0]
        print(p[0])
        ptp = list(pt)
        print(ptp)  # it is a list of the data saved in database
        # print('length of ptp is: ',len(ptp))
        kwargs = {'name':ptp[0],'location':ptp[1],'email':ptp[2],'domain':ptp[3],'phone':ptp[4],'summary':ptp[5],'type_of_company':ptp[6],'est_year':ptp[7],'about':ptp[8],'linkedin':ptp[9],'language_worked_with':ptp[10],'collab_tools':ptp[11],'opsys':ptp[12],'plateform_worked_with':ptp[13],'honor_or_reward':ptp[14],'honor_or_reward_desc':ptp[15],'cn':'cn'}
        return kwargs
    # get request
    print('you are:', request.session.get('name'))

    print('your id:', request.session.get('email'))
    # request.session.set_expiry(1200) #this is to expire the session within 20 min of inactivity
    # this is the query function
    def query(fieldname,variable):
        c = """UPDATE comp_profile SET {}='{}' WHERE email='{}';""".format(fieldname,variable,id)
        cursor.execute(c)
        m.commit()

   
            
    if request.method=="POST":
        m = sql.connect(host='localhost', user='root',passwd='', database='JobShip')
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():
            if key =="company_name":
                name = value
                query('name',name)
            if key=="location":
                location=value
                query('location',location)

            if key=="domain":
                domain=value
                query('domain',domain)

            if key=="phone":
                phone=value
                query('phone',phone)

            if key=="summary":
                summary=value
                query('summary',summary)

            if key=="toc":
                toc=value
                query('type_of_company',toc)

            if key=="est_year":
                est_year=value
                query('est_year',est_year)

                
            if key=="about":
                about=value
                query('about',about)

            if key=="honor_or_reward":
                honor_or_reward=value
                query('honor_or_reward',honor_or_reward)

            if key=="honor_or_reward_desc":
                honor_or_reward_desc=value
                query('honor_or_reward_desc',honor_or_reward_desc)

        # useer
        
        print('your id within user post fxn',id)
        # post ewquest
        kwargs=comp_info(id)

        return render(request, 'company.html',kwargs)


    if  request.session.get('set')!='yes':
        return redirect('/')
    else: 
        # kwargs has to declare in else block if we call it before posr request block it will throw an error
        kwargs=comp_info(id)    
        return render(request, 'company.html',kwargs)


def logout(request):
    request.session.clear()
    return redirect('/')    


def test(request):
    
    if request.method=="POST":
        m = sql.connect(host='localhost', user='root',passwd='', database='test')
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():
            if key == "name":
                name = value
            if key==   "password":
                password=value
            if key==   "email":
                email=value
            if key==   "dob":
                dob=value

        # INSERT INTO `test2` (`sno`, `name`, `email`, `password`) VALUES ('1', 'uh', 'kjhjg', 'jkjbkj');        
        c1 = """INSERT INTO test2  Values('{}','{}', '{}', '{}','{}');""".format('',name,password,email,dob)
        c2 = """INSERT INTO test Values('{}','{}', '{}', '{}');""".format('',name,password,'email')
        cursor.execute(c1)
        cursor.execute(c2)
        m.commit()
    id=request.session.get('email')

    def company_info(id):
        m = sql.connect(host='localhost', user='root',passwd='', database='JobShip')
        cursor = m.cursor()
        q = "select name,place,email,website,phone,summary,experience,college,degree,timePeriod,certificate_name,certificate_desc,database_worked_with,language_worked_with,collab_tools,opsys,plateform_worked_with,honor_or_reward,honor_or_reward_desc from stud_profile where email='{}'".format(id)
        cursor.execute(q)
        t = tuple(cursor.fetchall())
        p = list(t)
        pt = p[0]
        print(p[0])
        ptp = list(pt)
        print(ptp)  # it is a list of the data saved in database
        # print('length of ptp is: ',len(ptp))
        kwargs = {'name':ptp[0],'place':ptp[1],'email':ptp[2],'website':ptp[3],'phone':ptp[4],'summary':ptp[5],'experience':ptp[6],'college':ptp[7],'degree':ptp[8],'timePeriod':ptp[9],'certificate_name':ptp[10],'certificate_desc':ptp[11],'database_worked_with':ptp[12],'language_worked_with':ptp[13],'collab_tools':ptp[14],'opsys':ptp[15],'plateform_worked_with':ptp[16],'honor_or_reward':ptp[17],'honor_or_reward_desc':ptp[18],'cn':'cn'}
        return kwargs
    return render(request, 'company.html')


def settings(request):
    return render(request, 'settings.html')


def signup_company(request):
    args={'':''}
    name=''
    em=''
    pwd=''
    domain=''
    est_year=''
    toc=''
    if request.method=="GET" and request.session.get('set')=='yes':
        return redirect('/')
    #  and request.session.get['set']!='yes'
    if request.method == "POST":
        
        m = sql.connect(host='localhost', user='root',passwd='', database='jobship')
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():
            if key == "company_name":
                name = value
            if key == "email":
                em = value
            if key == "password":
                pwd = value
            if key == "domain":
                domain = value
            if key == "location":
                loc = value
            if key == "establish_year":
                est_year = value
            if key == "type_of_company":
                toc = value
            if key == "linkedin":
                linkedin = value
            
          
      
        
      
            #  INSERT INTO `company` (`company_id`, `company_name`, `email`, `password`, `domain`, `establish_year`, `type_of_company`, `location`) VALUES ('2', 'akdj', 'klhklh', 'lkjlk', 'lkj', '2022-03-02', 'lknk', 'lkn');
        c1="""INSERT INTO company Values('{}','{}','{}','{}','{}','{}','{}','{}','{}');""".format(0,name,em,pwd,domain,est_year,toc,loc,linkedin)    
        c2="""INSERT INTO comp_profile Values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}');""".format(0,name,loc,em,domain,'phone','summary',toc,est_year,'about your company',linkedin,'','','','','','')    
        
        cursor.execute(c1)
        cursor.execute(c2)
        m.commit()

        request.session['name']=name
        request.session['email']=em
        request.session['domain']=domain
        request.session['iscompany']='yes'
        request.session['linkedin']=linkedin
        request.session['set']='yes'
        args={'name':name,'email':em}

        return redirect('/company/')
    return render(request, 'signup_company.html')


def signup(request):
    # this is test branch
    fn = ''  # firstname
    ln = ''  # lastname
    em = ''  # email
    confem = ''  # confirmationemail
    pwd = ''  # password
    confpwd = ''  # confirmationpassword
    clg = ''  # college
    deg = ''  # degree
    spz = ''  # specialization
    sy = ''  # start_year
    ey = ''  # end_year
    
    if request.method=="GET" and request.session.get('set')=='yes':
        return redirect('/')
  
    #  and request.session.get['set']!='yes'
    if request.method == "POST":
        
        m = sql.connect(host='localhost', user='root',passwd='', database='jobship')
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():
            if key == "firstname":
                fn = value
            if key == "lastname":
                ln = value
            if key == "email":
                em = value
            # if key == "confemail":
            #     confem = value
            if key == "password":
                pwd = value
            # if key == "password":
            #     confpwd = value
            if key == "college":
                clg = value
            if key == "degree":
                deg = value
            if key == "specialization":
                spz = value
            if key == "start_year":
                sy = value
            if key == "end_year":
                ey = value
                
            args = [fn, ln, em, pwd, clg, deg, spz, sy, ey]
            summary="This optional section can help you stand out to recruiters. If this section is empty, it will not appear on your resume."
            experience="This section is empty and won't appear in your resume."
      
        name=fn+" "+ln
        time_period=sy+"-"+ey
      
        c1 = """INSERT INTO student Values('{}','{}', '{}', '{}','{}','{}','{}','{}','{}','{}',current_timestamp());""".format(0, args[0], args[1], args[2], args[3], args[4], args[5], args[6], args[7], args[8])
        c2 = """INSERT INTO stud_profile Values('{}','{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');""".format(0,name,'place',em,'wesite','phone','summary','experience',clg,deg,time_period,'cn','cd','dbs','lww','ct','opsys','pww','har','hard')
        cursor.execute(c1)
        cursor.execute(c2)
        m.commit()

        request.session['name']=name
        request.session['email']=em
        request.session['set']='yes'

        return redirect('/user/')
        # request.session.['name']=name
    # elif request.session.get('set')=='yes':
    #     return redirect('/')
    
    return render(request, 'signup.html')    
    

def user(request):
    id=request.session.get('email')

    # args = {'name': request.session.get('name'),'email':request.session.get('email')}
    def user_info(id):
        m = sql.connect(host='localhost', user='root',passwd='', database='JobShip')
        cursor = m.cursor()
        q = "select name,place,email,website,phone,summary,experience,college,degree,timePeriod,certificate_name,certificate_desc,database_worked_with,language_worked_with,collab_tools,opsys,plateform_worked_with,honor_or_reward,honor_or_reward_desc from stud_profile where email='{}'".format(id)
        cursor.execute(q)
        t = tuple(cursor.fetchall())
        p = list(t)
        pt = p[0]
        print(p[0])
        ptp = list(pt)
        print(ptp)  # it is a list of the data saved in database
        # print('length of ptp is: ',len(ptp))
        kwargs = {'name':ptp[0],'place':ptp[1],'email':ptp[2],'website':ptp[3],'phone':ptp[4],'summary':ptp[5],'experience':ptp[6],'college':ptp[7],'degree':ptp[8],'timePeriod':ptp[9],'certificate_name':ptp[10],'certificate_desc':ptp[11],'database_worked_with':ptp[12],'language_worked_with':ptp[13],'collab_tools':ptp[14],'opsys':ptp[15],'plateform_worked_with':ptp[16],'honor_or_reward':ptp[17],'honor_or_reward_desc':ptp[18],'cn':'cn'}
        return kwargs
    # get request
   
    print('you are:', request.session.get('name'))

    print('your id:', request.session.get('email'))
    request.session.set_expiry(1200) #this is to expire the session within 20 min of inactivity
    # this is the query function
    def query(fieldname,variable):
        c = """UPDATE stud_profile SET {}='{}' WHERE email='{}';""".format(fieldname,variable,id)
        cursor.execute(c)
        m.commit()

  
            
    if request.method=="POST":
        m = sql.connect(host='localhost', user='root',passwd='', database='JobShip')
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():
            if key =="name":
                name = value
                query('name',name)
            if key=="place":
                place=value
                query('place',place)

            # if key=="email":
            #     email=value
            #     query('email',email)
                # student_query('email', email)
                # email_change_query="""UPDATE student SET email='{}' WHERE email='{}';""".format(fieldname,variable,id)

            if key=="website":
                website=value
                query('website',website)

            if key=="phone":
                phone=value
                query('phone',phone)

            if key=="summary":
                summary=value
                query('summary',summary)

            if key=="experience":
                experience=value
                query('experience',experience)

            if key=="college":
                college=value
                query('college',college)

                
            if key=="degree":
                degree=value
                query('degree',degree)

                
            if key=="timePeriod":
                timePeriod=value
                query('timePeriod',timePeriod)

            if key=="certificate_name":
                certificate_name=value
                query('certificate_name',certificate_name)

            if key=="certificate_desc":
                certificate_desc=value
                query('certificate_desc',certificate_desc)

            if key=="database_worked_with":
                database_worked_with=value
                query('database_worked_with',database_worked_with)

            if key=="language_worked_with":
                language_worked_with=value
                query('language_worked_with',language_worked_with)

            if key=="collab_tools":
                collab_tools=value
                query('collab_tools',collab_tools)

            if key=="opsys":
                opsys=value
                query('opsys',opsys)

            if key=="plateform_worked_with":
                plateform_worked_with=value
                query('plateform_worked_with',plateform_worked_with)

            if key=="honor_or_reward":
                honor_or_reward=value
                query('honor_or_reward',honor_or_reward)

            if key=="honor_or_reward_desc":
                honor_or_reward_desc=value
                query('honor_or_reward_desc',honor_or_reward_desc)

        # useer
        
        print('your id within user post fxn',id)
        # post ewquest
        kwargs=user_info(id)

        return render(request, 'user.html',kwargs)


    if request.session.get('set')!='yes':
        return redirect('/')
    else: 
        kwargs=user_info(id)    
        return render(request, 'user.html',kwargs)

def logout(request):
    request.session.clear()
    return redirect('/')    


def test(request):
    
    if request.method=="POST":
        m = sql.connect(host='localhost', user='root',passwd='', database='test')
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():
            if key == "name":
                name = value
            if key==   "password":
                password=value
            if key==   "email":
                email=value
            if key==   "dob":
                dob=value

        # INSERT INTO `test2` (`sno`, `name`, `email`, `password`) VALUES ('1', 'uh', 'kjhjg', 'jkjbkj');        
        c1 = """INSERT INTO test2  Values('{}','{}', '{}', '{}','{}');""".format('',name,password,email,dob)
        c2 = """INSERT INTO test Values('{}','{}', '{}', '{}');""".format('',name,password,'email')
        cursor.execute(c1)
        cursor.execute(c2)
        m.commit()
   
    return render(request,'test.html')    

def job():
    pass








