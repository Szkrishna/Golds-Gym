from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from appauth.models import Contact, MembershipPlan, Trainer, Enrollment, Gallery, Attendance


# Create your views here.
def home(request):
    return render(request,"index.html")

def signup(request):
    if request.method=="POST":
        username=request.POST.get('usernumber')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')

        if len(username)>10 or len(username)<10:
            messages.info(request,"Phone Number Must be 10 Digits")
            return redirect('/signup')

        if pass1!=pass2:
            messages.info(request,"Password is not Matching")
            return redirect('/signup')
       
        try:
            if User.objects.get(username=username):
                messages.warning(request,"Phone Number is Taken")
                return redirect('/signup')
           
        except Exception as identifier:
            pass
        
        try:
            if User.objects.get(email=email):
                messages.warning(request,"Email is Taken")
                return redirect('/signup')
           
        except Exception as identifier:
            pass
        
        myuser=User.objects.create_user(username,email,pass1)
        myuser.save()
        messages.success(request,"User is Created Please Login")
        return redirect('/handlelogin')
        
        
    return render(request,"signup.html")


def handlelogin(request):
    if request.method=="POST":        
        username=request.POST.get('usernumber')
        pass1=request.POST.get('pass1')
        myuser=authenticate(username=username,password=pass1)
        if myuser is not None:
            login(request,myuser)
            return redirect('/')
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('/handlelogin')
            
    else:   
        return render(request,"handlelogin.html")

def handleLogout(request):
    logout(request)
    messages.success(request,"Logout Success")    
    return redirect('/handlelogin')

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')

        myquery=Contact(name=name, email=email, subject=subject, message=message)
        myquery.save()
        messages.info(request,"Thankyou for contacting us we will get back to you soon.")
        return redirect('/contact')
    
    return render(request,'contact.html')

def enroll(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login and Try Again")
        return redirect('/handlelogin')

    Membership=MembershipPlan.objects.all()
    SelectTrainer=Trainer.objects.all()
    context={"Membership":Membership,"SelectTrainer":SelectTrainer}
    if request.method=="POST":
        FullName=request.POST.get('FullName')
        email=request.POST.get('email')
        gender=request.POST.get('gender')
        PhoneNumber=request.POST.get('PhoneNumber')
        DOB=request.POST.get('DOB')
        member=request.POST.get('member')
        trainer=request.POST.get('trainer')
        reference=request.POST.get('reference')
        address=request.POST.get('address')
        query=Enrollment(fullname=FullName, email=email, gender=gender, phonenumber=PhoneNumber, DOB=DOB, selectmembershipplan=member, selecttrainer=trainer, reference=reference, address=address)
        query.save()
        messages.success(request,"Thanks For Enrollment")
        return redirect('/join')
    
    return render(request,'join.html', context)

def services(request):
    return render(request,'services.html')

def about(request):
    return render(request,'about.html')

def profile(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login and Try Again")
        return redirect('/handlelogin')
    user_name=request.user
    posts=Enrollment.objects.filter(phonenumber=user_name)
    attendance=Attendance.objects.filter(phonenumber=user_name)
    context={"posts":posts,"attendance":attendance}
    return render(request,'profile.html',context)

def gallery(request):
    posts=Gallery.objects.all()
    context={"posts":posts}
    return render(request,'gallery.html',context)

def attendance(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login and Try Again")
        return redirect('/handlelogin')
    SelectTrainer=Trainer.objects.all()
    context={"SelectTrainer":SelectTrainer}
    if request.method=="POST":
        phonenumber=request.POST.get('PhoneNumber')
        login=request.POST.get('loginintime')
        logout=request.POST.get('logouttime')
        selectworkout=request.POST.get('workout')
        trainedby=request.POST.get('trainer')
        query=Attendance(phonenumber=phonenumber, login=login, logout=logout,selectworkout=selectworkout, trainedby=trainedby)
        query.save()
        messages.success(request,"Attendance applied sucessfully")
        return redirect('/attendance')

    return render(request,'attendance.html',context)
