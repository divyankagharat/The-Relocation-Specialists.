from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout

# Create your views here.
from .models import *
from datetime import date
from django.db.models import Q

def index(request):
    return render(request, 'index.html')

def admin_login(request):
    error =""
    if request.method == 'POST':
        u=request.POST['username']
        p=request.POST['pwd']
        user = authenticate(username=u,password=p) #to check if username and coressponding  exists in the DB
        try:
            if user.is_staff:
                login(request,user)
                error="no"
            else:
                error="yes"
        except:
            error="yes"
    return render(request,'admin_login.html',locals())

def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    totalservices = Services.objects.all().count #to count total number of services by the user
    totalreservations = SiteUser.objects.all().count
    totalread = Contact.objects.filter(isread="no").count
    totalunread = Contact.objects.filter(isread="yes").count
    return render(request,'admin_home.html',locals())

def add_services(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    if request.method == "POST":
        st = request.POST['servicetitle']
        des = request.POST['description']
        image = request.FILES['image']
        # to Get images as an input from the user we don't use POST but FILES
        try:
            # to store data from user
            Services.objects.create(title=st, decription=des, image=image)
            error = "no"
        except:
            error="yes"
    return render(request,'add_services.html',locals())

def manage_services(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    services = Services.objects.all()  # all
    return render(request,'manage_services.html',locals())

def edit_services(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    service = Services.objects.get(id=pid)
    error = ""
    if request.method == "POST":
        st = request.POST['servicetitle']
        des = request.POST['description']

        service.title = st
        service.description = des
        try:
            service.save()
            error = "no"
        except:
            error = "yes"
        try:
            image = request.FILES['image']
            service.image = image
            service.save()
        except:
            pass
    return render(request, 'edit_services.html', locals())

def delete_services(request,pid):
    service = Services.objects.get(id=pid)
    service.delete()
    return redirect('manage_services')

def services(request):
    services = Services.objects.all()  # all
    return render(request,'services.html',locals())

def about(request):
    return render(request,'about.html')

def request_quote(request):
    error = ""
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        contact = request.POST['contact']
        location = request.POST['location']
        shiftingloc = request.POST['shiftingloc']
        shiftingdate = request.POST['shiftingdate']
        briefitems = request.POST['briefitems']
        items = request.POST['items']
        # to Get images as an input from the user we don't use POST but FILES
        try:
            # to store data from user
            SiteUser.objects.create(name=name, email=email, mobile=contact, location=location, shiftingloc=shiftingloc,shiftingdate=shiftingdate, briefitems=briefitems, items=items, requestdate=date.today)
            error = "no"
        except:
            error="yes"
    return render(request,'request_quote.html',locals())

def new_booking(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    booking =SiteUser.objects.all()
    return render(request,'new_booking.html',locals())



def old_booking(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    if request.method == 'POST':
        fd = request.POST['fromdate']
        td = request.POST['todate']
        booking = SiteUser.objects.filter(Q(requestdate__gte=fd) & Q(requestdate__lte=td)) #Q is used for querying and finding records,it is used when you want to apply conditions to the records
        return render(request,'bookingdate.html',locals())
    return render(request,'old_booking.html',locals())

def contact(request):
    if request.method == 'POST':
        n = request.POST['fullname']
        c = request.POST['contact']
        e = request.POST['email']
        s = request.POST['subject']
        m = request.POST['message']
        try:
            Contact.object.create(name=n,contact=c,emailid=e,subject=s,message=m,mdate=date.today(),isread="no")
            error = "no"

        except:
            error = "yes"

    return render(request,'contact.html',locals())

def unread_queries(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    booking =Contact.objects.filter(isread="no")
    return render(request,'unread_queries.html',locals())


def read_queries(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    booking =Contact.objects.filter(isread="yes")
    return render(request,'read_queries.html',locals())


def Logout(request):
    logout(request)
    return redirect(index)

