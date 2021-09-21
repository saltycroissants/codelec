from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#def index(request):
	#return HttpResponse("Hello World")
def index(request):
    return render(request, "hello/index.html")

def helloEunji(request):
    return HttpResponse("Hello Eunji !")

#def greet (request, name):
	#return HttpResponse(f"Hello {name}")

def greet (request, name) :
    	return render(request, 'hello/greet.html', {
		"name" : name.capitalize()
})