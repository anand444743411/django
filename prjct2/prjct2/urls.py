"""prjct2 URL Configuration

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
from django.urls import path,include,re_path
from app2.views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee/', include('app2.urls')),
    path('signup/', register, name='user_signup'),
    path('login/',user_login, name='user_login'),
    path('success/',success, name='user_success'),
    path('logout/',user_logout, name='user_logout'),
    path('change_password/',change_password,name='change_password'),

    re_path(r'^password_reset/$', auth_views.PasswordResetView.as_view(template_name="registration/password_reset_form.html"),
            name='password_reset'),
    re_path(r'^password_reset/done/$',
            auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_done.html"),
            name='password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"),
            name='password_reset_confirm'),
    re_path(r'^reset/done/$',
            auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_complete.html"),
            name='password_reset_complete'),
]