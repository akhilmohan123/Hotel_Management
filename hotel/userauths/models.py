from django.db import models
from django.contrib.auth.models import AbstractUser
from shortuuid.django_fields import ShortUUIDField
from django.db.models.signals import post_save
# Create your models here.

def _user_directory_path(instance,filename):
    ext=filename.split(".")[-1]
    filename="%s.%s" % (instance.user.id,filename)
    return "user_{0}/{1}".format(instance.user.id,filename)
GENDER=(("male","male"),("female","female"),("other","other"))
IDENTITY_TYPE=(("National Identification Number","National Identification Number"),("Driving Licenece","Driving Licenece"),("passport","passport"))
class User(AbstractUser):
    full_name=models.CharField(max_length=200,null=True,blank=True)
    user_name=models.CharField(max_length=200)
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=100,null=True,blank=True)
    gender=models.CharField(max_length=20,choices=GENDER,default="other")

    otp=models.CharField(max_length=100,null=True,blank=True)
    USERNAME_FIELD="email"
    REQUIRED_FIELDS=["username"]
    def __str__(self):
        return self.user_name
class Profile(models.Model):
    pid=ShortUUIDField(length=7,max_length=25,alphabet="abcdefghijklmnopqrstuvwxyz1234")
    image=models.FileField(upload_to=_user_directory_path,default="default.jpg",null=True,blank=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    full_name=models.CharField(max_length=200,null=True,blank=True)
    phone=models.CharField(max_length=100,null=True,blank=True)
    gender=models.CharField(max_length=20,choices=GENDER,default="other")
    country=models.CharField(max_length=100,null=True,blank=True)
    city=models.CharField(max_length=100,null=True,blank=True)
    state=models.CharField(max_length=100,null=True,blank=True)
    address=models.CharField(max_length=100,null=True,blank=True)
    identity_type=models.CharField(max_length=200,choices=IDENTITY_TYPE,default="Other")
    identity_image=models.FileField(upload_to=_user_directory_path,default="id.jpg",null=True,blank=True)
    facebook=models.URLField(null=True,blank=True)
    twitter=models.URLField(null=True,blank=True)
    wallet=models.DecimalField(max_digits=12,decimal_places=2,default=0.00)
    verified=models.BooleanField(default=False)
    date=models.DateField(auto_now_add=True)
    class Meta:
        ordering=['-date']
    def __str__(self):
        if self.full_name:
            return f"{self.full_name}"
        else:
            return f"{self.user.user_name}"
def create_user_profile(sender,instance,created,**kwargs):
    if created:
       Profile.objects.create(user=instance)
def save_user_profile(sender,instance,**kwargs):
    instance.profile.save()
post_save.connect(create_user_profile,sender=User)
post_save.connect(save_user_profile,sender=User)
    