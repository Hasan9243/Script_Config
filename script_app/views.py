from django.shortcuts import render

from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.template.loader import get_template 
from script_app.forms import UserForm, UserInfoForm, portal_info_form, vrf_client_form, bgp_peer_form
from script_app import forms
from django.contrib.auth.hashers import make_password
from script_app.models import User, UserInfo
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

########### Home page ###########
class home(TemplateView):
    template_name = 'script_app/home.html'
    
    
    
########### Register ###########

def Register(request):
    
    registered = False
    
    if request.method=='POST':
        user_form = UserForm(request.POST)
        user_info_form = UserInfoForm(request.POST)
        
        if user_form.is_valid() and user_info_form.is_valid():
            user = user_form.save()
            user.password = make_password(user.password)
            user.save()
            
            user_info = user_info_form.save(commit=False)
            user_info.user = user
            
            if 'profile_pic' in request.FILES:
                user_info.profile_pic = request.FILES['profile_pic']
                
            user_info.save()
            registered = True 
            messages.success(request, 'You have singed up successfully.')

            
        return render(request, "script_app/home.html")
            
            
            
            
    else:
        user_form = UserForm()
        user_info_form = UserInfoForm()
        

        dict = {'user_form':user_form, 'user_info_form':user_info_form, 'registered':registered}
    
        return render(request, 'script_app/register.html', context=dict)



########### Login ###########

def Signin(request):
    
    if request.method=="GET":
        form=forms.LoginForm()
        return render(request, 'script_app/login.html', {'form':form})
    
    elif request.method=="POST":
        form=forms.LoginForm(request.POST)
        
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f'HI!!! {username.title()}, have a nice day!!!')
                return redirect('script_app:home')
            
        # form is not valid or user is not authenticated
        messages.error(request,f'Invalid username or password')
        return render(request,'script_app/login.html', {'form': form})

def Signout(request):
    logout(request)
    messages.success(request,f'You have been logged out.')
    return redirect('script_app:home') 

########### Profile ###########

class profile(LoginRequiredMixin, TemplateView):
    context_object_name = "profile"
    model = UserInfo
    template_name = 'script_app/profile.html'
   
########### Update Profile ###########  

"""
class update_profile(LoginRequiredMixin, UpdateView):
    fields="__all__"
    template_name="script_app/update_profile.html"
    model=UserInfo
    success_url=" "
""" 
@login_required
def update_profile(request):
 
    
    user = User.objects.get(id= request.user.id)
    profile = UserInfo.objects.get(user= user)
    
    if request.method == 'POST':
        data = request.POST
        # if data['password1'] == '':
        # data['password1'] = '123'
        
        form = forms.UpdateProfile(data, instance=user)
        
        if form.is_valid() :
            form.save()
            form2=forms.UpdateProfileMeta(data, instance=profile)
            
            if form2.is_valid():
                form2.save()
                messages.success(request,"Your Profile has been updated successfully")
                return redirect("script_app:profile")
            else:
                form2=form2
            
        else:
            form = forms.UpdateProfile(instance=request.user)
    return render(request,'script_app/update_profile.html')
    
    

def Portal(request):
  
    if request.method == 'POST':
        form = portal_info_form(request.POST)
        if form.is_valid():
            script = form.save()
            # Generate the script based on user input
            # You can use the 'script' object here to generate the script
            # For example, you might generate HTML here
            return render(request, 'script_app/generated_script.html', {'script': script})
    else:
        form = portal_info_form()
    return render(request, 'script_app/portal.html', {'form': form})




def VRF_Client(request):
      if request.method == 'POST':
        form = vrf_client_form(request.POST)
        if form.is_valid():
            script = form.save()
            # Generate the script based on user input
            # You can use the 'script' object here to generate the script
            # For example, you might generate HTML here
            return render(request, 'script_app/generated_script2.html', {'script': script})
      else:
          form = vrf_client_form()
      return render(request, 'script_app/portal2.html', {'form': form})
    


def eBGP_Peer(request):
      if request.method == 'POST':
        form = bgp_peer_form(request.POST)
        if form.is_valid():
            script = form.save()
            # Generate the script based on user input
            # You can use the 'script' object here to generate the script
            # For example, you might generate HTML here
            return render(request, 'script_app/generated_script3.html', {'script': script})
      else:
          form = bgp_peer_form()
      return render(request, 'script_app/portal3.html', {'form': form})
    