from django.contrib import admin
from script_app.models import UserInfo, info_portal, VRF, eBGP_Peer
# Register your models here.
admin.site.register(UserInfo)
admin.site.register(info_portal)
admin.site.register(VRF)
admin.site.register(eBGP_Peer)

