from django.contrib import admin
from userinfo.models import userinfo

# Register your models here.
@admin.register(userinfo)
class userAdmininfo(admin.ModelAdmin):
    list_display = ('id','name','email','password')
