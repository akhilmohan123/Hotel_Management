from django.contrib import admin
from userauths.models import User,Profile
# Register your models here.
class Useradmin(admin.ModelAdmin):
    search_fields=['full_name','username']
    list_display=['username','full_name','email','phone','gender']
class Profileadmin(admin.ModelAdmin):
    search_fields=['full_name','user_username']
    list_display=['full_name','verified','user']
admin.site.register(User,Useradmin)
admin.site.register(Profile,Profileadmin)
