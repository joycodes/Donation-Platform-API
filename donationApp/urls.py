from django.urls import path,re_path as url
from . import views
from .views import *
from django.contrib.auth import views as auth_views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.home, name='home'),

    path('api/register/',views.RegisterView.as_view()),
    path('api/login/',views.LoginView.as_view()),
    path('api/users/',views.UserList.as_view()),


    #charities API endpoints
    path('api/charities/', views.CharityList.as_view()),
    path('api/charities/<int:pk>/', views.CharityDetails.as_view()),

    #donors API endpoints
    path('api/donors/', views.DonorList.as_view()),
    path('api/donors/<int:pk>/', views.DonorDetails.as_view()),

    #donations API endpoints
    path('api/donations/', views.DonationsList.as_view()),
    path('api/donations/<int:pk>/', views.DonationsDetails.as_view()),

    #feedback API endpoints
    # path('api/feedback/', views.FeedbackList.as_view()),
    # path('api/feedback/<int:pk>/', views.FeedbackDetails.as_view()),

    #posts API endpoints
    # path('api/posts/', views.PostsList.as_view()),
    # path('api/posts/<int:pk>/', views.PostsDetails.as_view()),

    #Charity Donations API endpoints
    path('api/charity/(<charity_id>\d+)/donations/', views.CharitiesDonationsList),
    path('api/charity/(<charity_id>\d+)/donations/(<donation_id>\d+)/', views.CharitiesDonationsdetails),   

    path('signin/', GetTokenPairView.as_view(), name='token_obtain_pair'),
    path('signup/', RegisterDonorView.as_view(), name='signup'),
    path('signup-charity/', RegisterCharityView.as_view(), name='signup-charity'),
    path('signup-admin/', RegisterAdminView.as_view(), name='signup-admin'),
    # donor endpoints
    path('donors/', views.donor_list),
    path('donors/(<donor_id>\d+)/', views.donor_details),
    # beneficiaries endpoints
    path('charity/beneficiaries/', views.beneficiaries_list),
    path('charity/beneficiaries/(<beneficiary_id>\d+)/', views.beneficiary_details),
    
    path('charity/(<charity_id>\d+)/beneficiaries/', views.charitybeneficiaries_list),
    path('charity/(<charity_id>\d+)/beneficiary/(<beneficiary_id>\d+)/', views.charitybeneficiary_details),
    
    # all anonymous donations view
    path('api/anon/', views.anonnymous_donation),
    # charity's anonymous donations
    path('api/charity/(<charity_id>\d+)/anon_donations/', views.anonnymous_donation_list),
    
]
