"""
URL configuration for Generator project.

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
from django.urls import path
from script_app import views as v1
from django.contrib.auth import views as auth

app_name = "script_app"
urlpatterns = [
    
    path('home/', v1.home.as_view(), name='home'),
    path('login/', v1.Signin, name='login'),
    path('logout/', v1.Signout, name='logout'),
    path('register/', v1.Register, name='register'),
 
    path('profile/', v1.profile.as_view(), name='profile'),
    path('update_profile/', v1.update_profile, name='update_profile'),

    path('portal/', v1.Portal, name='portal'),
    path('vrf_client/', v1.VRF_Client, name='vrf_client'),
    path('bgp_peer/', v1.eBGP_Peer, name='bgp_peer'),
    
]