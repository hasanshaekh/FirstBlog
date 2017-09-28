from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import(
	authenticate,
	get_user_model,
	login,
	logout,
	)
# Create your views here.
from accounts.forms import UserLoginForm, UserRegisterForm



def login_view(request):
	title= "Login"
	form=UserLoginForm(request.POST or None)
	if form.is_valid():
		username=form.cleaned_data.get("username")
		password=form.cleaned_data.get("password")
		user=authenticate(username=username,password=password)
		login(request,user)
		return redirect("/")
	return render(request,"form.html",{"form":form, "title":title})

def dologin(request):
	data={}
	if request.method=='POST':
		data['username']=request.POST.get('username')
		data['password']=request.POST.get('password')

		if user is not None:
			if user.is_active:
				login(request,user)
				u=request.user.username
				return redirect(check)
		else:
			return render(request,'post_list.html')

	

def register_view(request):
	title= "Register"
	form=UserRegisterForm(request.POST or None)
	if form.is_valid():
		user=form.save(commit=False)
		username=form.cleaned_data.get("username")
		password=form.cleaned_data.get("password")
		user.set_password(password)
		user.save()
		new_user=authenticate(username=username,password=password)
		login(request,new_user)
		return redirect("/")
	context={
		"form":form,
		"title":title
	}
	# if request.method == 'POST':
	# 	form=SignUpForm(request.POST or None)
	# 	if form.is_valid():
	# 		user=form.save(commit=False)
	# 		username=form.cleaned_data.get("username")
	# 		password=form.cleaned_data.get("password")
	# 		user.set_password(password)
	# 		user.save()
	# 		new_user=authenticate(username=username,password=password)
	# 		# user_auth=User(username=username)
	# 		# user_auth.is_staff= True
	# 		# user_auth.is_superuser= True
	# 		# user_auth.save()

	# 		login(request,new_user)
	# 		return redirect ('/')
	# else:
	# 	form=UserCreationForm()

	# return render(request,"form.html",context)
	return render(request,"form.html",{'form':form, 'title':title})

def logout_view(request):
	logout(request)
	return redirect("/")
	return render(request,"form.html",{})