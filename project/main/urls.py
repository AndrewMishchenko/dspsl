"""main URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth

from apps.user_profile import views as user_profile

urlpatterns = [
    url(r'^products/', include('apps.product.urls')),
    url(r'^login/$', user_profile.login, name='login'),
    url(r'^signup/$', user_profile.signup, name='singup'),
    url(r'^logout/$', auth.logout, {'next_page': '/products/'},
        name='logout'
        ),
    url(r'^admin/', admin.site.urls),
]
