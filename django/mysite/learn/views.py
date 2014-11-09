# Create your views here.
#coding:utf-8
from django.http import HttpResponse

def index(request):
	return HttpResponse(u"双十一烧烧烧")
