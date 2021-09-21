from django.shortcuts import render
import datetime

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    #pass variables to template
    return render(request, 'choosuk/index.html', {
        "choosuk" : now.month == 9 and now.day == 21 
    })