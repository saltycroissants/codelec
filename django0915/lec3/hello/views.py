from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


#request 이용해서 정보 가져오거나 하기
def index(request):
	return render(request, "hello/index.html")

def greet (request, name) :
    	return render(request, 'hello/greet.html', {
		"name" : name.capitalize()
})