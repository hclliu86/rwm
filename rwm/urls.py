"""rwm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from learn import views as learn_views
from rwm.views import hello2
from calc import views as calc_views

urlpatterns = [
    url(r'^hello/$', hello2),
    url(r'^calc_test/$', calc_views.get_testdb, name="calc_test"),
    url(r'^$', learn_views.home, name='home'),
    url(r'^home.html', learn_views.home, name='home'),
    url(r'^definition_home.html', learn_views.definition_home, name='definition_home'),
    url(r'^search/$', calc_views.search),
    url(r'^search-form/$', calc_views.search_form),
    url(r'^search-post/$', calc_views.search_post),
    url(r'^post2/$', calc_views.post2),
    url(r'^add/$', calc_views.add),
    url(r'^admin/', admin.site.urls),
]
