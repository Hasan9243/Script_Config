from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    emp_id = models.CharField(max_length = 1000)
    designation = models.CharField(max_length = 1000)
    department = models.CharField(max_length = 1000)
    profile_pic = models.ImageField(upload_to = 'pp', blank = True)
    
    
    def __str__(self):
        return self.user.username



class info_portal(models.Model):
    
    Interface_Number= models.CharField(max_length=1000)
    VLAN = models.CharField(max_length=1000)
    Description = models.CharField(max_length=1000)
    IP_Address = models.CharField(max_length=1000)
    Subnet_Mask = models.CharField(max_length=1000)
    Network_Address = models.CharField(max_length=1000)
    Network_Mask = models.CharField(max_length=1000)
    
    
    def __str__(self):
        return self.Interface_Number


vrf_name = (
    ('ABBL_Intra_Br', 'ABBL_Intra_Br'),
    ('IBBL_Intra', 'IBBL_Intra'),
    ('PUBALI_Intra', 'PUBALI_Intra'),
    
)



class VRF(models.Model):
    VRF_Name=models.CharField(max_length=100, choices=vrf_name, default='ABBL_Intra_Br')
    Interface_Number = models.CharField(max_length=1000)
    VLAN_Number= models.CharField(max_length=1000)
    Description = models.CharField(max_length=1000)
    IP_Address= models.CharField(max_length=1000)
    Subnet_Mask= models.CharField(max_length=1000)
    Network_Address = models.CharField(max_length=1000)
    Network_Mask = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.VRF_Name

class eBGP_Peer(models.Model):
    Remote_Peer_IP = models.CharField(max_length=1000)
    Remote_As = models.CharField(max_length=1000)
    BGP_Description = models.CharField(max_length=1000)
    In_Prefix_Name = models.CharField(max_length=1000)
    Out_Prefix_Name = models.CharField(max_length=1000)
    Client_Public_IP = models.CharField(max_length=1000)
    Mask_Length = models.CharField(max_length=1000)
    
    
    def __str__(self):
        return self.Remote_As