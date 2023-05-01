"""
URL configuration for tigini project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static

from blog import views
from authentication.views import user_creation_view, user_login_view, user_logout_view
from user_profile.views import user_profile, edit_user_profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page.as_view(), name='home-page'),
    path('signup', user_creation_view.as_view(), name='signup'),
    #user login view url
    path('login', user_login_view.as_view(), name='login'),
    #user logout view url
    path('logout', user_logout_view.as_view(), name='logout'),
    #user profile view url
    path('profile', user_profile.as_view(), name='profile'),
    #edit user profile url
    path('edit/profile', edit_user_profile.as_view(), name='edit-profile')
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)