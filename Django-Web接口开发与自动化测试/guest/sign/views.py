from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.
def index(request):
	return render(request,'index.html')

def login_action(request):
	if request.method == 'POST':
		username = request.POST.get('username','')
		password = request.POST.get('password','')
		if username == 'admin' and password == 'admin123':
			return HttpResponseRedirect('/event_manager/')
		else:
			return render(request,'index.html',{'error':'username or password erroe!'})

def event_manager(request):
	return render(request,"event_manager.html")
