from django.urls import path
from . import views

# located in same directory

urlpatterns = [
    #view에서 정의해준 index함수
	path("", views.index, name = "index"),
    path("eunji", views.helloEunji, name = "helloEunji"),
    path("<str:name>", views.greet, name = "greet")
	
]