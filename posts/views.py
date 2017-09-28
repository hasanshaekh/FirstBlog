from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from posts.forms import PostForm
from posts.models import Post

def post_create(request):

	form=PostForm(request.POST or None)
	if form.is_valid():
		instances=form.save(commit=False)
		instances.save()
		return redirect("/")

	context={
		"form": form,
	}

	return render(request,"post_form.html",context)

	# return HttpResponse("<h1>Create</h1>")
def post_detail(request,id):
	instances= get_object_or_404(Post,id=id)
	context={
	"title": instances.title,
	"instances": instances,
	}
	return render(request,"post_details.html",context)
def post_list(request):
	# if request.user.is_authenticated():
	# 	context={
	# "title": "List"
	# 	}
	# else:
	# 	context={
	# "title": "List Faul"
	# 	}
	queryset=Post.objects.all()
	context={
	"object_list": queryset,
	"title": "List"
	}
	return render(request,"post_list.html",context)
def post_update(request):
	return HttpResponse("<h1>Update</h1>")
def post_delete(request):
	return HttpResponse("<h1>Delete</h1>")