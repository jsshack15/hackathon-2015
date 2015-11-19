"""hackathon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
	1. Add an import:  from other_app.views import Home
	2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
	1. Add an import:  from blog import urls as blog_urls
	2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from hacks.views import HackathonView, CodeManiaView, problems, sendRSVP

urlpatterns = [
	url(r'^hackadmin/', include(admin.site.urls)),
	url(r'^RSVP$', sendRSVP.as_view(), name='sendRSVP'),
	url(r'^$', HackathonView.as_view(), name='hackathon'),
	url(r'^codemania/$', CodeManiaView.as_view(), name='codemania'),
	url(r'^codemania/problems$',problems, name='home'),
]

from django.conf.urls import (
	handler404, handler500
	)

# handler400 = 'my_app.views.bad_request'
# handler403 = 'my_app.views.permission_denied'
handler404 = 'hacks.views.handler404'
handler500 = 'hacks.views.handler500'

