from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.conf import settings
from django.contrib.auth.models import User, auth
from django.contrib import messages
from employee.Forms import EmployeeForms, leaveForms, emptimeForms
from employee.models import Employee, leavedetail, emptime
from datetime import datetime, date
# from django.db.models.functions import Now

def homepage(request):
    return render(request, "homepage.html")


def sign(request):
    return render(request, "signup.html")


def signup(request):
    if request.method == 'POST':
        name = request.POST['uname']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        passwd = request.POST['pass']
        user = User.objects.create_user(
            username=name, first_name=fname, last_name=lname, email=email, password=passwd)
        user.save()
        return redirect('/log')
    else:
        return redirect('/')

def log(request):
    return render(request, "login.html")


def login(request):
    if request.method == 'POST':
        username = request.POST['name']
        password = request.POST['pass']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                request.session.set_expiry(86400)
                auth.login(request, user)
                return redirect('/profile')
            else:
                return HttpResponse('<script> alert("LOGGED OUT......!!!) </script> ')
        else:
            messages.error(request,'WRONG INFO')
            return redirect('/log')
    else:
        return HttpResponse('<script> alert("submission error.......!!!)<script>')


def logout(request):
    auth.logout(request)
    return redirect('/')


def profile(request):
    if request.user.is_authenticated:
        emp = Employee.objects.filter(eid_id=request.user.id).first()
        return render(request, "profile.html", {'emp': emp})
    else:
        return HttpResponse('<script> alert("submission error.......!!!)<script>')

def register(request):
    return render(request,"register.html")

def profiledata(request):
    if request.method == 'POST':
        if Employee.objects.filter(eid_id=request.user.id).exists():
            print("already Exists")
            return redirect('/editprofile')
        else:
            phone = request.POST['phone']
            address = request.POST['address']
            dept = request.POST['dept']
            upload_file = request.FILES['pic']
            eid = request.user.id
            emp = Employee(eid_id=eid, dept=dept, phone=phone,
                           address=address, pic=upload_file)
            emp.save()
        return redirect('/profile')
    else:
        return redirect('/edit_profile.html')

def editprofile(request):
     if request.user.is_authenticated:
        emp = Employee.objects.filter(eid_id=request.user.id).first()
        return render(request, "edit_profile.html", {'emp': emp})


def editdata(request):
    if request.method == 'POST':
        if Employee.objects.filter(eid_id=request.user.id).exists():
            phone = request.POST['phone']
            address = request.POST['address']
            dept = request.POST['dept']
            Employee.objects.filter(eid_id=request.user.id).update(phone=phone, address=address, dept=dept)
            return redirect('/profile')
        else:
            error=True;
            return redirect('/register')
    else:
        return HttpResponse('<script> alert("submission error.......!!!)<script>') 

def about(request):
    return render(request, "about.html")

def leave(request):
    if request.user.is_authenticated:
        emp = Employee.objects.filter(eid=request.user.id).get()
        return render(request,"leave.html",{'emp':emp})
    else:
        pass

def leaveapply(request):

    if request.method == 'POST':
        sdate = request.POST['sdate']
        edate = request.POST['edate']
        total_leave = request.POST['total_leave']
        reason = request.POST['reason']
        leave_type = request.POST['leave_type']
        eid = request.user.id
        leaverequest = leavedetail(eid_id=request.user.id, sdate=sdate, edate=edate,
                                   reason=reason, total_leave=total_leave, leave_type=leave_type)
        leaverequest.save()
        print(leaverequest)
        return redirect('/profile')
    else:
        return HttpResponse('<script> alert("SUBMISSION ERROR......!!!) </script> ')


def leaveapproval(request):
    info = leavedetail.objects.filter(status='Pending').all()
    return render(request, "approve.html",{'info':info})

def checkleaves(request):
    if request.user.is_authenticated:
        emp = leavedetail.objects.filter(eid=request.user.id)

        ml= leavedetail.objects.filter(eid=request.user.id,leave_type="medical leave").count()
        cl= leavedetail.objects.filter(eid=request.user.id,leave_type="casual leave").count()
        matl= leavedetail.objects.filter(eid=request.user.id,leave_type="maternity leave").count()
        pl= leavedetail.objects.filter(eid=request.user.id,leave_type="privilege leave").count()
        bl= leavedetail.objects.filter(eid=request.user.id,leave_type="bereavement leave").count()
        context={
            'emp':emp,
            'ml':ml,
            'cl':cl,
            'matl':matl,
            'pl':pl,
            'bl':bl
            }
        return render(request,"check_leaves.html",context)

    
def forgotpass(request):
    return render(request, "forgot_password.html")

def forgotpassword(request):
    if request.method == 'POST':
        email = request.POST['email']
        new_p = request.POST['newpass']
        u = User.objects.get(email=email)
        u.set_password(new_p)
        u.save()
        return redirect('/log')
    else:
        return redirect('/signup')
# def datetimeinput(request):
#     if request.method == 'POST':
#         edate=date.today()
#         emptime(eid_id=request.user.id,edate=edate)
#         entrytime=
#         exittime=


def approve(request):
    return render(request, "approve.html")

def approveleave(request, id):
    if leavedetail.objects.filter(id=id).exists():
        leavedetail.objects.filter(id=id).update(status='Approval')
        return redirect('/leaveapproval')
    else:
        return redirect('/leaveapproval')

def declineleave(request, id):
    if leavedetail.objects.filter(id=id).exists():
        leavedetail.objects.filter(id=id).update(status='Decline')
        return redirect('/leaveapproval')
    else:
        return redirect('/leaveapproval')

def entry(request):
    current_time = datetime.now()
    date = current_time.strftime("%Y/%m/%d")
    entry = current_time.strftime("%H:%M:%S")  
    emptime(eid_id=request.user.id, edate=date, entrytime=entry).save()
    return redirect('/profile')

def exit(request):
    current_time = datetime.now()
    date = current_time.strftime("%Y/%m/%d")
    exit = current_time.strftime("%H:%M:%S")  
    emptime.objects.filter(eid_id=request.user.id, edate=date).update(exittime=exit)
    return redirect('/profile')
