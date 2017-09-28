from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.contrib.auth import(
	authenticate,
	get_user_model,
	login,
	logout,
	)

User =get_user_model()
class UserLoginForm(forms.Form):
	"""docstring for UserLoginForm"""
	username= forms.CharField()
	password= forms.CharField(widget=forms.PasswordInput)

	def clean(self,*args,**kwargs):
		username=self.cleaned_data.get("username")
		password=self.cleaned_data.get("password")

		user=authenticate(username=username,password=password)
		if not user:
			raise forms.ValidationError("This user Does not Exists")
		if not user.check_password(password):
			raise forms.ValidationError("Incorrect Password")
		if not user.is_active:
			raise forms.ValidationError("User No Longer Active")
		return super(UserLoginForm,self).clean(*args,**kwargs)



class UserRegisterForm(forms.ModelForm):
	"""docstring for UserRegisterForm"""
	email=forms.EmailField(label='Email Address')
		# email2=forms.EmailField(label='Confirm Email')
	password= forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model= User
		fields = [
			'email',
			# 'email2',			
			'username',			
			'password'
		]
	def clean_email(self):
		email=self.cleaned_data.get("email")
		# email2=self.cleaned_data.get("email2")
		username=self.cleaned_data.get("username")
		username_qs= User.objects.filter(username=username)
		if username_qs.exists():
			raise forms.ValidationError("Username Already exists")
		email_qs= User.objects.filter(email=email)
		if email_qs.exists():
			raise forms.ValidationError("Emails Already exists")
		return email



				

			
		