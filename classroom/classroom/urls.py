"""classroom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from users import views as user_views
from resource import views as res_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_views.home , name = 'home'),
    path('userfp/', res_views.userhome , name = 'userhome'),
    path('search/', res_views.search , name = 'search'),
    path('addtopic/', res_views.newTopic , name = 'addtopic'),
    path('<int:topic_id>/addmaterial/', res_views.newMaterial, name='addmaterial'),
    path('github/', res_views.github , name = 'git'),
    path('cf/', res_views.codef , name = 'cf'),
    path('<int:topic_id>/detail/', res_views.detail, name='detail'),
    path('accounts/', include('allauth.urls')),
    path('register/', user_views.register , name = 'register'),
    path('profile/', user_views.profile, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),name="reset_password"),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),name="password_reset_done"),

    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name="password_reset_confirm"),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),name="password_reset_complete"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)