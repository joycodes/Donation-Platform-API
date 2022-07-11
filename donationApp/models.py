from re import T
from django.db import models
from django.contrib.auth.models import User,AbstractUser
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
# Create your models here.

class User(AbstractUser):
  is_charity = models.BooleanField(default=False)
  is_donor = models.BooleanField(default=False)
  is_superuser = models.BooleanField(default=False)
  is_staff = models.BooleanField(default=False)


# Create your models here.

COUNTRIES = [ 
    ('Afganistan', ('Afghanistan')),
    ('Albania', ('Albania')),
    ('Algeria', ('Algeria')),
    ('American Samoa', ('American Samoa')),
    ('Andorra', ('Andorra')),
    ('Angola', ('Angola')),
    ('Anguilla', ('Anguilla')),
    ('Antigua & Barbuda', ('Antigua & Barbuda')),
    ('Argentina', ('Argentina')),
    ('Armenia', ('Armenia')),
    ('Aruba', ('Aruba')),
    ('Australia', ('Australia')),
    ('Austria', ('Austria')),
    ('Azerbaijan', ('Azerbaijan')),
    ('Bahamas', ('Bahamas')),
    ('Bahrain', ('Bahrain')),
    ('Bangladesh', ('Bangladesh')),
    ('Barbados', ('Barbados')),
    ('Belarus', ('Belarus')),
    ('Belgium', ('Belgium')),
    ('Belize', ('Belize')),
    ('Benin', ('Benin')),
    ('Bermuda', ('Bermuda')),
    ('Bhutan', ('Bhutan')),
    ('Bolivia', ('Bolivia')),
    ('Bonaire', ('Bonaire')),
    ('Bosnia & Herzegovina', ('Bosnia & Herzegovina')),
    ('Botswana', ('Botswana')),
    ('Brazil', ('Brazil')),
    ('British Indian Ocean Ter', ('British Indian Ocean Ter')),
    ('Brunei', ('Brunei')),
    ('Bulgaria', ('Bulgaria')),
    ('Burkina Faso', ('Burkina Faso')),
    ('Burundi', ('Burundi')),
    ('Cambodia', ('Cambodia')),
    ('Cameroon', ('Cameroon')),
    ('Canada', ('Canada')),
    ('Canary Islands', ('Canary Islands')),
    ('Cape Verde', ('Cape Verde')),
    ('Cayman Islands', ('Cayman Islands')),
    ('Central African Republic', ('Central African Republic')),
    ('Chad', ('Chad')),
    ('Channel Islands', ('Channel Islands')),
    ('Chile', ('Chile')),
    ('China', ('China')),
    ('Christmas Island', ('Christmas Island')),
    ('Cocos Island', ('Cocos Island')),
    ('Colombia', ('Colombia')),
    ('Comoros', ('Comoros')),
    ('Congo', ('Congo')),
    ('Cook Islands', ('Cook Islands')),
    ('Costa Rica', ('Costa Rica')),
    ('Cote DIvoire', ('Cote DIvoire')),
    ('Croatia', ('Croatia')),
    ('Cuba', ('Cuba')),
    ('Curaco', ('Curacao')),
    ('Cyprus', ('Cyprus')),
    ('Czech Republic', ('Czech Republic')),
    ('Denmark', ('Denmark')),
    ('Djibouti', ('Djibouti')),
    ('Dominica', ('Dominica')),
    ('Dominican Republic', ('Dominican Republic')),
    ('East Timor', ('East Timor')),
    ('Ecuador', ('Ecuador')),
    ('Egypt', ('Egypt')),
    ('El Salvador', ('El Salvador')),
    ('Equatorial Guinea', ('Equatorial Guinea')),
    ('Eritrea', ('Eritrea')),
    ('Estonia', ('Estonia')),
    ('Ethiopia', ('Ethiopia')),
    ('Falkland Islands', ('Falkland Islands')),
    ('Faroe Islands', ('Faroe Islands')),
    ('Fiji', ('Fiji')),
    ('Finland', ('Finland')),
    ('France', ('France')),
    ('French Guiana', ('French Guiana')),
    ('French Polynesia', ('French Polynesia')),
    ('French Southern Ter', ('French Southern Ter')),
    ('Gabon', ('Gabon')),
    ('Gambia', ('Gambia')),
    ('Georgia', ('Georgia')),
    ('Germany', ('Germany')),
    ('Ghana', ('Ghana')),
    ('Gibraltar', ('Gibraltar')),
    ('Great Britain', ('Great Britain')),
    ('Greece', ('Greece')),
    ('Greenland', ('Greenland')),
    ('Grenada', ('Grenada')),
    ('Guadeloupe', ('Guadeloupe')),
    ('Guam', ('Guam')),
    ('Guatemala', ('Guatemala')),
    ('Guinea', ('Guinea')),
    ('Guyana', ('Guyana')),
    ('Haiti', ('Haiti')),
    ('Hawaii', ('Hawaii')),
    ('Honduras', ('Honduras')),
    ('Hong Kong', ('Hong Kong')),
    ('Hungary', ('Hungary')),
    ('Iceland', ('Iceland')),
    ('Indonesia', ('Indonesia')),
    ('India', ('India')),
    ('Iran', ('Iran')),
    ('Iraq', ('Iraq')),
    ('Ireland', ('Ireland')),
    ('Isle of Man', ('Isle of Man')),
    ('Israel', ('Israel')),
    ('Italy', ('Italy')),
    ('Jamaica', ('Jamaica')),
    ('Japan', ('Japan')),
    ('Jordan', ('Jordan')),
    ('Kazakhstan', ('Kazakhstan')),
    ('Kenya', ('Kenya')),
    ('Kiribati', ('Kiribati')),
    ('Korea North', ('Korea North')),
    ('Korea Sout', ('Korea South')),
    ('Kuwait', ('Kuwait')),
    ('Kyrgyzstan', ('Kyrgyzstan')),
    ('Laos', ('Laos')),
    ('Latvia', ('Latvia')),
    ('Lebanon', ('Lebanon')),
    ('Lesotho', ('Lesotho')),
    ('Liberia', ('Liberia')),
    ('Libya', ('Libya')),
    ('Liechtenstein', ('Liechtenstein')),
    ('Lithuania', ('Lithuania')),
    ('Luxembourg', ('Luxembourg')),
    ('Macau', ('Macau')),
    ('Macedonia', ('Macedonia')),
    ('Madagascar', ('Madagascar')),
    ('Malaysia', ('Malaysia')),
    ('Malawi', ('Malawi')),
    ('Maldives', ('Maldives')),
    ('Mali', ('Mali')),
    ('Malta', ('Malta')),
    ('Marshall Islands', ('Marshall Islands')),
    ('Martinique', ('Martinique')),
    ('Mauritania', ('Mauritania')),
    ('Mauritius', ('Mauritius')),
    ('Mayotte', ('Mayotte')),
    ('Mexico', ('Mexico')),
    ('Midway Islands', ('Midway Islands')),
    ('Moldova', ('Moldova')),
    ('Monaco', ('Monaco')),
    ('Mongolia', ('Mongolia')),
    ('Montserrat', ('Montserrat')),
    ('Morocco', ('Morocco')),
    ('Mozambique', ('Mozambique')),
    ('Myanmar', ('Myanmar')),
    ('Nambia', ('Nambia')),
    ('Nauru', ('Nauru')),
    ('Nepal', ('Nepal')),
    ('Netherland Antilles', ('Netherland Antilles')),
    ('Netherlands', ('Netherlands (Holland, Europe)')),
    ('Nevis', ('Nevis')),
    ('New Caledonia', ('New Caledonia')),
    ('New Zealand', ('New Zealand')),
    ('Nicaragua', ('Nicaragua')),
    ('Niger', ('Niger')),
    ('Nigeria', ('Nigeria')),
    ('Niue', ('Niue')),
    ('Norfolk Island', ('Norfolk Island')),
    ('Norway', ('Norway')),
    ('Oman', ('Oman')),
    ('Pakistan', ('Pakistan')),
    ('Palau Island', ('Palau Island')),
    ('Palestine', ('Palestine')),
    ('Panama', ('Panama')),
    ('Papua New Guinea', ('Papua New Guinea')),
    ('Paraguay', ('Paraguay')),
    ('Peru', ('Peru')),
    ('Phillipines', ('Philippines')),
    ('Pitcairn Island', ('Pitcairn Island')),
    ('Poland', ('Poland')),
    ('Portugal', ('Portugal')),
    ('Puerto Rico', ('Puerto Rico')),
    ('Qatar', ('Qatar')),
    ('Republic of Montenegro', ('Republic of Montenegro')),
    ('Republic of Serbia', ('Republic of Serbia')),
    ('Reunion', ('Reunion')),
    ('Romania', ('Romania')),
    ('Russia', ('Russia')),
    ('Rwanda', ('Rwanda')),
    ('St Barthelemy', ('St Barthelemy')),
    ('St Eustatius', ('St Eustatius')),
    ('St Helena', ('St Helena')),
    ('St Kitts-Nevis', ('St Kitts-Nevis')),
    ('St Lucia', ('St Lucia')),
    ('St Maarten', ('St Maarten')),
    ('St Pierre & Miquelon', ('St Pierre & Miquelon')),
    ('St Vincent & Grenadines', ('St Vincent & Grenadines')),
    ('Saipan', ('Saipan')),
    ('Samoa', ('Samoa')),
    ('Samoa American', ('Samoa American')),
    ('San Marino', ('San Marino')),
    ('Sao Tome & Principe', ('Sao Tome & Principe')),
    ('Saudi Arabia', ('Saudi Arabia')),
    ('Senegal', ('Senegal')),
    ('Seychelles', ('Seychelles')),
    ('Sierra Leone', ('Sierra Leone')),
    ('Singapore', ('Singapore')),
    ('Slovakia', ('Slovakia')),
    ('Slovenia', ('Slovenia')),
    ('Solomon Islands', ('Solomon Islands')),
    ('Somalia', ('Somalia')),
    ('South Africa', ('South Africa')),
    ('Spain', ('Spain')),
    ('Sri Lanka', ('Sri Lanka')),
    ('Sudan', ('Sudan')),
    ('Suriname', ('Suriname')),
    ('Swaziland', ('Swaziland')),
    ('Sweden', ('Sweden')),
    ('Switzerland', ('Switzerland')),
    ('Syria', ('Syria')),
    ('Tahiti', ('Tahiti')),
    ('Taiwan', ('Taiwan')),
    ('Tajikistan', ('Tajikistan')),
    ('Tanzania', ('Tanzania')),
    ('Thailand', ('Thailand')),
    ('Togo', ('Togo')),
    ('Tokelau', ('Tokelau')),
    ('Tonga', ('Tonga')),
    ('Trinidad & Tobago', ('Trinidad & Tobago')),
    ('Tunisia', ('Tunisia')),
    ('Turkey', ('Turkey')),
    ('Turkmenistan', ('Turkmenistan')),
    ('Turks & Caicos Is', ('Turks & Caicos Is')),
    ('Tuvalu', ('Tuvalu')),
    ('Uganda', ('Uganda')),
    ('United Kingdom', ('United Kingdom')),
    ('Ukraine', ('Ukraine')),
    ('United Arab Erimates', ('United Arab Emirates')),
    ('United States of America', ('United States of America')),
    ('Uraguay', ('Uruguay')),
    ('Uzbekistan', ('Uzbekistan')),
    ('Vanuatu', ('Vanuatu')),
    ('Vatican City State', ('Vatican City State')),
    ('Venezuela', ('Venezuela')),
    ('Vietnam', ('Vietnam')),
    ('Virgin Islands (Brit)', ('Virgin Islands (Brit)')),
    ('Virgin Islands (USA)', ('Virgin Islands (USA)')),
    ('Wake Island', ('Wake Island')),
    ('Wallis & Futana Is', ('Wallis & Futana Is')),
    ('Yemen', ('Yemen')),
    ('Zaire', ('Zaire')),
    ('Zambia', ('Zambia')),
    ('Zimbabwe', ('Zimbabwe')), 
]



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


class Donor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone_number = models.IntegerField(null=True)
    location = models.CharField(max_length=30)
    country = models.CharField(choices=COUNTRIES, max_length=50)
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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    country = models.CharField(choices=COUNTRIES, max_length=50)
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
    amount_raised = models.IntegerField()
    date_donated = models.DateTimeField(auto_now_add=True)
    payment_method= models.CharField(default='Paypal',max_length=30)
    charity = models.ForeignKey(Charity, on_delete=models.CASCADE,)
    donation_frequency = models.CharField(choices=DONATION_FREQUENCY,max_length=30)
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

    
class Beneficiary(models.Model):
    name = models.CharField(max_length=200)
    charity = models.ForeignKey(Charity, on_delete=models.CASCADE)
    contact= models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    country = models.CharField(choices=COUNTRIES, max_length=50)
    donation_received = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class AnonymousDonation(models.Model):
    donation_amount = models.IntegerField()
    comment = models.TextField(blank=True,null=True)
    charity = models.ForeignKey(Charity, on_delete=models.CASCADE)
    payment_method= models.CharField(default='Paypal',max_length=30)
    
    def __str__(self):
        return self.charity.name