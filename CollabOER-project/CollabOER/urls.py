"""CollabOER URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from . import views
from converter import views as converter_views

urlpatterns = [
	url(r'^$',views.homepage,name="homepage"),
	
	url(r'^createcommunity/',views.create_community,name="createCommunity"),
	url(r'^createcommunityarticles/',views.create_community_resources,name="createCommunityArticle"),
	url(r'^creategroup/',views.create_groups,name="createGroup"),
	url(r'^creategrouparticles/',views.create_group_resources,name="createGroupArticle"),

	url(r'^render/pdf/',converter_views.Pdf.as_view(), name="convert"),
    url(r'^admin/', admin.site.urls),
]
