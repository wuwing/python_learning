1.
django-admin startproject mysite

2.
cd mysite
python manage.py startapp learn

3.
vim mysite/mysite/settings.py
	INSTALLED_APPS = (
		'django.contrib.admin',
		...,
		'learn',
	)

4.
vim mysite/learn/views.py
	#coding:utf-8
	from django.http import HttpResponse

	def index(request):
		return HttpResponse(r"***")

5.
vim mysite/mysite/urls.py
	from django.conf.urls import patterns,include,url
	from django.contrib import admin
	admin.autodiscover()

	urlpatterns = patterns('',
		url(r'^$', 'learn.views.index',name = 'home'),
		url('^admin/',include(admin.site.urls)),
	)

6.
python manage.py runserver
