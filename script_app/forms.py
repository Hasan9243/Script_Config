from django import forms
from django.contrib.auth.models import User
from script_app.models import UserInfo, info_portal, VRF, eBGP_Peer



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','email', 'password')
    

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ('emp_id', 'designation', 'department', 'profile_pic')
        
class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)

class UpdateProfile(forms.ModelForm):
    username = forms.CharField(max_length=250,help_text="The Username field is required.")
    email = forms.EmailField(max_length=250,help_text="The Email field is required.")
    first_name = forms.CharField(max_length=250,help_text="The First Name field is required.")
    last_name = forms.CharField(max_length=250,help_text="The Last Name field is required.")
    current_password = forms.CharField(max_length=250)

    
    class Meta:
        model = User
        fields = ('email', 'username','first_name', 'last_name')
    
    
    def clean_username(self):
        username=self.cleaned_data['username']
        try:
            user=User.objects.exclude(id=self.cleaned_data['id'].get(username=username))
        
        except Exception as e:
            return username
        raise forms.ValidationError(f"The {user.username} has already taken")


class UpdateProfileMeta(forms.ModelForm):
    designation= forms.CharField(max_length=250,help_text="The Contact field is required.")
    department = forms.CharField(max_length=250,help_text="The Contact field is required.")
    

    class Meta:
        model = UserInfo
        fields = ('designation', 'department')
   
class portal_info_form(forms.ModelForm):
    class Meta:
        model = info_portal
        fields = "__all__"



class vrf_client_form(forms.ModelForm):
    class Meta:
        model=VRF
        fields = '__all__'

class bgp_peer_form(forms.ModelForm):
    class Meta:
        model=eBGP_Peer
        fields = '__all__'

