from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from . models import Student
# Create your views here.

def homepage(request):
    return render(request,'home.html')


def aboutpage(request):
    return render(request,'about.html')

def shop(request):
    return render(request,'shop.html')

def contactpage(request):
    return render(request,'contact.html')

def formpage(request):
    return render(request,'form.html')

def saveSessionData(request):
    request.session['username'] = "smitpatel"
    return HttpResponse("session created")

def getSessionData(request):
    if request.session.has_key('username'):
        msg = request.session['username']           
        return HttpResponse(msg)
    else:
        return HttpResponse("session variable not present ")

def deleteSessionData(request):
    del request.session['username']
    return HttpResponse("session Removed")

def getSessionData2(request):
    msg = request.session['username']
    return HttpResponse(msg)

def formpageprocess(request):
    a = int(request.POST["txt1"])
    b = int(request.POST["txt2"])
    c = a + b
    msg = "A value is",a,"B value is ",b,"sum is ",c
    d = ""
    if c == 30:
        d= "IF Condition called"
    elif c<30:
        d = "Else if called"
    else:
        d ="Else Called"        
    return  render(request,"ans.html",{'mya':a,'myb':b,'myc':c,'myd':d})

def login(request):
    return render(request,'login.html')

def loginprocess(request):
    txt1 = request.POST['email']
    request.session['myemail'] = txt1
    return redirect(dashboard)

def dashboard(request):
    if request.session.has_key('myemail'):
        return render(request,"dashboard.html")
    else:
        return redirect(login)

def logout(request):
    del request.session['myemail']
    return redirect(login)

def mailsenddemo(request):
    subject = 'django mail demo'
    message ='hello how are you ?'
    email_form = settings.EMAIL_HOST_USER
    recipient_list = ['P05276236@gmail.com']
    send_mail( subject, message, email_form, recipient_list)
    return HttpResponse("Mail sent")

def addstudentform(request):
    return render(request,'add-student.html')

def addstudentformprocess(request):
    txt1 = request.POST['txt1']
    txt2 = request.POST['txt2']
    txt3 = request.POST['txt3']
    txt4 = request.POST['txt4']
    Student.objects.create(name=txt1,mobile=txt2,email=txt3,address=txt4)
    return HttpResponse("Thank you")