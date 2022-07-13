from re import T
from django.db import models
# from django.contrib.auth.models import User,AbstractUser,AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import User, AbstractUser, BaseUserManager,AbstractBaseUser,PermissionsMixin
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings

# Create your models here.

class User(AbstractUser):
  is_charity = models.BooleanField(default=False, blank=True, null=True)
  is_donor = models.BooleanField(default=False, blank=True, null=True)
  is_superuser = models.BooleanField(default=False, blank=True, null=True)
  is_staff = models.BooleanField(default=False, blank=True, null=True)
  authtoken_token = "ForeignKey"


# Create your models here.



TARGET_AMOUNT= [
    (100000,'$100,000'),
    (200000,'$200,000'),
    (300000,'$300,000'),
    (400000,'$400,000'),
    (500000,'$500,000'),
    (700000,'$700,000'),
    (600000,'$600,000'),
    (800000,'$800,000'),
    (900000,'$900,000'),
    (1000000,'$1M+'),
]

DONATION_FREQUENCY= [
    ('Once', ('Once')),
    ('Monthly', ('Monthly')),
    ('Annualy', ('Annualy')),
]

class Tokens(models.Model):
    class Meta: 
        abstract = 'rest_framework.authtoken' not in settings.INSTALLED_APPS

class Donor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone_number = models.IntegerField(null=True)
    location = models.CharField(max_length=30)
    # country = models.CharField(choices=COUNTRIES, max_length=50)
    bio = models.TextField(max_length=700)
    image = CloudinaryField('image', null=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def save_donor(self):
        self.save()

    def delete_donor(self):
        self.delete()


class Charity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    # country = models.CharField(choices=COUNTRIES, max_length=50)
    description = models.TextField(max_length=700)
    charity_image = CloudinaryField('charity_image', null=True)
    date_formed = models.DateTimeField(auto_now_add=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    target_amount = models.IntegerField(choices=TARGET_AMOUNT,null=True)
    deadline = models.DateTimeField(auto_now_add=True)
    mission = models.CharField(max_length=100)
    status = models.BooleanField(default=None,null=True)
    donor = models.ManyToManyField(Donor, blank=True)

    def __str__(self):
        return self.name

    def status_true(self):
        self.status = True
        self.save()
        return self.status

    def status_false(self):
        self.status = False
        self.save()
        return self.status


class Donations(models.Model):
    donor_id = models.ManyToManyField(Donor,blank=True )
    target_amount = models.IntegerField(choices=TARGET_AMOUNT,null=True)
    payment_method= models.CharField(default='Paypal',max_length=30)
    comment = models.TextField()
    
    def __str__(self):
        return self.charity.name

    def __str__(self):
        return self.charity.name

class Feedback(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=500)


    def __str__(self):
        return self.name

class Posts(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=500)
    date_posted = models.DateTimeField(auto_now_add=True)
    image = CloudinaryField('image', null=True)
    charity = models.ForeignKey(Charity, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.charity.name

    
# class Beneficiary(models.Model):
#     name = models.CharField(max_length=200)
#     charity = models.ForeignKey(Charity, on_delete=models.CASCADE)
#     contact= models.CharField(max_length=50)
#     location = models.CharField(max_length=50)
#     # country = models.CharField(choices=COUNTRIES, max_length=50)
#     donation_received = models.CharField(max_length=100)
    
#     def __str__(self):
#         return self.name
    
# class AnonymousDonation(models.Model):
#     donation_amount = models.IntegerField()
#     comment = models.TextField(blank=True,null=True)
#     charity = models.ForeignKey(Charity, on_delete=models.CASCADE)
#     payment_method= models.CharField(default='Paypal',max_length=30)
    
#     def __str__(self):
#         return self.charity.name