"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from employee import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage),
    path('sign', views.sign),
    path('signup', views.signup),
    path('log', views.log),
    path('login', views.login),
    path('logout', views.logout),
    path('about', views.about),
    path('profile', views.profile),
    path('register', views.register),
    path('profiledata', views.profiledata),
    path('editprofile', views.editprofile),
    path('editdata', views.editdata),
    path('leave', views.leave),
    path('leaveapply', views.leaveapply),
    path('leaveapproval', views.leaveapproval),
    path('checkleaves', views.checkleaves),
    path('forgotpass', views.forgotpass),
    path('forgotpassword', views.forgotpassword),
    path('approveleave/<id>',views.approveleave),
    path('declineleave/<id>',views.declineleave),
    path('approve',views.approve),
    path('entry',views.entry),
    path('exit',views.exit)
]
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
