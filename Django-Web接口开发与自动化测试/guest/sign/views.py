from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
# Create your views here.
def index(request):
	return render(request,'index.html')

def login_action(request):
	if request.method == 'POST':
		username = request.POST.get('username','')
		password = request.POST.get('password','')
		user = auth.authenticate(username=username,password=password)
		if user is not None:
			auth.login(request,user)
			response = HttpResponseRedirect('/event_manager/')
			#response.set_cookie('user',username,3600)
			request.session['user']=username
			return response
		else:
			return render(request,'index.html',{'error':'username or password erroe!'})

@login_required
def event_manager(request):
	#username = request.COOKIES.get('user','')
	username = request.session.get('user','')
	return render(request,"event_manager.html",{'user':username})
