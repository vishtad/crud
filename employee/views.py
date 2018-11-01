from django.shortcuts import render, redirect ,HttpResponse
from employee.forms import *  
from employee.models import Employee  
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from crud import settings

# Create your views here.  
def emp(request):  
    if request.method == "POST":  
        form = EmployeeForm(request.POST,request.FILES)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = EmployeeForm()  
    return render(request,'index.html',{'form':form})  
@login_required(login_url='/login')
def show(request):  
    employees = Employee.objects.all()  
    return render(request,"show.html",{'employees':employees})  

@login_required(login_url='/login')
def edit(request, id):  
    employee = Employee.objects.get(id=id)  
    return render(request,'edit.html', {'employee':employee})

@login_required(login_url='/login')  
def update(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST,request.FILES, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'employee': employee})  

@login_required(login_url='/login')
def destroy(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("/show")  

def home(request):
	return render(request,'home.html')
	
def registration(request):
	if request.method=='POST':
		form1=userform(request.POST)
		if form1.is_valid():
			username=form1.cleaned_data['username']
			first_name=form1.cleaned_data['first_name']
			last_name=form1.cleaned_data['last_name']
			email=form1.cleaned_data['email']
			password=form1.cleaned_data['password']
			subject="Confirmation mail"
			msg="dear sir/maam,thank you for more details visit :"
			send_mail(subject,msg,settings.EMAIL_HOST_USER,[email])
			User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
			return redirect("/login")
	else:
		form1=userform()
	return render(request,'regis.html',{'frm':form1})

def login(request):
    return render(request,"login.html")

def check(request):
    username= request.POST['username']
    password=request.POST['password']
    user =authenticate(username= username , password=password)
    print(user)
    if user is not None:
        auth.login(request,user)
        return redirect("/emp")
    else:
        return HttpResponse('<h1> invalid </h1>')

def log_out(request):  # we use log_out like this beacuse we have predefined function logout already
    auth.logout(request)
    return render(request,'login.html')
	
'''
def search(request):
	if request.method=='POST':
		squery= request.POST['search_box']
		if squery is not None:
			s=Employee.objects.filter(ename=squery)
			if s:
				return render(request,'search.html',{'q':s})
			else:
				return HttpResponse('<h1> not found </h1>')
		else:
			return redirect('/show')
	return redirect('/')
'''
def search1(request):
	if request.method=='POST':
		s= request.POST['search_box']
		if (s):
			match=Employee.objects.filter(ename__icontains=s)
			if match:
				return render(request,'search.html',{'q':match})
			else:
				return HttpResponse('<h1> not found </h1>')
		else:
			return redirect('/show')
	return redirect('/')