from django.shortcuts import render, redirect
from django.http.response import HttpResponse, Http404
from .serializers import *
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from rest_framework import generics

# donor serializer dependencies

from rest_framework.decorators import api_view
from django.http.response import JsonResponse

from rest_framework.parsers import JSONParser 
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializer import *

from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from django.http import HttpResponseForbidden

from rest_framework.exceptions import AuthenticationFailed
import jwt,datetime
from .models import User
# Create your views here.

def home(request):
  return render(request, 'home.html')

class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user=User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('user not found')

        if not user.check_password(password):
            raise AuthenticationFailed('incorrect password')


        payload = {
            'id': user.id,
            'exp': datetime.datetime.now() + datetime.timedelta(minutes=120),
            'iat': datetime.datetime.now()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')
        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)

        response.data ={
            'jwt': token
        }

        return response

class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('unauthenticated')

        try:
            payload = jwt.decode(token, 'secret', algorithms='HS256')
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('unauthenticated')




        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)



 
        return Response(serializer.data)

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class UserList(APIView):
    def get(self, request, format=None):
        all_user = User.objects.all()
        serializers = UserSerializer(all_user, many=True)
        return Response(serializers.data)
    def post(self, request, format=None):
        serializers = UserSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class CharityList(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        charities = Charity.objects.all()
        serializer = CharitySerializer(charities, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CharitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #apply as a charity
    def post(self, request, format=None):
        serializer = CharitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class CharityDetails(APIView):
    permission_classes = (AllowAny,)

    def get_object(self, pk):
        try:
            return Charity.objects.get(pk=pk)
        except Charity.DoesNotExist:
            raise Http404

    #To get a particular charity
    def get(self, request, pk, format=None):
        charity = self.get_object(pk)
        serializer = CharitySerializer(charity)
        return Response(serializer.data)

    #To update a particular charity
    def put(self, request, pk, format=None):
        charity = self.get_object(pk)
        serializer = CharitySerializer(charity, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #To delete a particular charity
    def delete(self, request, pk, format=None):
        charity = self.get_object(pk)
        charity.delete()
        return JsonResponse({"message":"deleted"})


class DonorList(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        donors = Donor.objects.all()
        serializer = DonorSerializer(donors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DonorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DonorDetails(APIView):
    permission_classes = (AllowAny,)

    def get_object(self, pk):
        try:
            return Donor.objects.get(pk=pk)
        except Donor.DoesNotExist:
            raise Http404

    #To get a particular donor
    def get(self, request, pk, format=None):
        donor = self.get_object(pk)
        serializer = DonorSerializer(donor)
        return Response(serializer.data)
    #To update a particular donor
    def put(self, request, pk, format=None):
        donor = self.get_object(pk)
        serializer = DonorSerializer(donor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #To delete a particular donor
    def delete(self, request, pk, format=None):
        donor = self.get_object(pk)
        donor.delete()
        return JsonResponse({"message":"deleted"})

    
class FeedbackList(APIView):
    def get(self, request):
        feedbacks = Feedback.objects.all()
        serializer = FeedbackSerializer(feedbacks, many=True)
        return Response(serializer.data)
    
    permission_classes = []
    authentication_classes = []
    def post(self, request):
        serializer = FeedbackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FeedbackDetails(APIView):
    permission_classes = (AllowAny,)
    
    def get_object(self, pk):
        try:
            return Feedback.objects.get(pk=pk)
        except Feedback.DoesNotExist:
            raise Http404

    #To get a particular feedback
    def get(self, request, pk, format=None):
        feedback = self.get_object(pk)
        serializer = FeedbackSerializer(feedback)
        return Response(serializer.data)

    #To update a particular feedback
    def put(self, request, pk, format=None):
        feedback = self.get_object(pk)
        serializer = FeedbackSerializer(feedback, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #To delete a particular feedback
    def delete(self, request, pk, format=None):
        feedback = self.get_object(pk)
        feedback.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DonationsList(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        donations = Donations.objects.all()
        serializer = DonationsSerializer(donations, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DonationsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DonationsDetails(APIView):
    permission_classes = (AllowAny,)

    #To update a particular donations
    def get_object(self, pk):
        try:
            return Donations.objects.get(pk=pk)
        except Donations.DoesNotExist:
            raise Http404

    #To get a particular donation
    def get(self, request, pk, format=None):
        donation = self.get_object(pk)
        serializer = DonationsSerializer(donation)
        return Response(serializer.data)

    #To update a particular donation
    def put(self, request, pk, format=None):
        donation = self.get_object(pk)
        serializer = DonationsSerializer(donation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #To delete a particular donation
    def delete(self, request, pk, format=None):
        donation = self.get_object(pk)
        donation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CharityDonationsList(APIView):
    permission_classes = (AllowAny,)

    def get_object(self, pk):
        try:
            charity = Charity.objects.get(pk=pk)
            donation = Donations.objects.filter(charity=charity)
            print(donation)
        except Donations.DoesNotExist:
            raise Http404

    #To get a particular charity donations
    def get(self, request, pk, format=None):
        charity = Charity.objects.get(pk=pk)
        donation = Donations.objects.filter(charity=charity)
        serializer = DonationsSerializer(donation)
        return Response(serializer.data)


class PostsList(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        posts = Posts.objects.all()
        serializer = PostsSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostsDetails(APIView):
    permission_classes = (AllowAny,)

    def get_object(self, pk):
        try:
            return Posts.objects.get(pk=pk)
        except Posts.DoesNotExist:
            raise Http404

    #To get a particular post
    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostsSerializer(post)
        return Response(serializer.data)

    #To update a particular post
    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostsSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #To delete a particular post
    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Get token/login
class GetTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = GetTokenPairSerializer
    
# Register donor view
class RegisterDonorView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterDonorSerializer
    
# Register charity view 
class RegisterCharityView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterCharitySerializer
    
# Register adminview 
class RegisterAdminView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterAdminSerializer
    
class DonorsView(generics.CreateAPIView):
    queryset = Donor.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = DonorSerializer
    
# donor list
@api_view(['GET', 'POST'])
def donor_list(request):
    if request.method == 'GET':
        donors = Donor.objects.all()
        donors_serializer = DonorSerializer(donors, many=True,context={'request': request})
        return Response(donors_serializer.data)
    elif request.method == 'POST':
        donors_data = JSONParser().parse(request)
        donors_serializer = DonorSerializer(data=donors_data)
        if donors_serializer.is_valid():
            donors_serializer.save()
            return Response(donors_serializer.data, status=status.HTTP_201_CREATED) 
        return Response(donors_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# single donor view   
@api_view(['GET', 'PUT'])
def donor_details(request, donor_id):
    try: 
        donor = Donor.objects.get(id=donor_id) 
    except Donor.DoesNotExist: 
        return JsonResponse({'message': 'Not found'}, status=status.HTTP_404_NOT_FOUND)  
    if request.method == 'GET': 
        donor_serializer = DonorSerializer(donor,many=True) 
        return Response(donor_serializer.data) 
    elif request.method == 'PUT': 
        donor_data = JSONParser().parse(request) 
        donor_serializer = DonorSerializer(donor, data=donor_data) 
        if donor_serializer.is_valid(): 
            donor_serializer.save() 
            return JsonResponse(donor_serializer.data) 
        return JsonResponse(donor_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#beneficiaries list 
@api_view(['GET','DELETE','POST'])
@permission_classes((AllowAny,))
def beneficiaries_list(request):
    if request.method == 'GET':
        beneficiaries = Beneficiary.objects.all()
        beneficiaries_serializer = BeneficiariesSerializer(beneficiaries, many=True,context={'request': request})
        return Response(beneficiaries_serializer.data)
    elif request.method == 'POST':
        # beneficiaries_data = JSONParser().parse(request)
        beneficiaries_serializer = BeneficiariesSerializer(data=request.data)
        if beneficiaries_serializer.is_valid():
            beneficiaries_serializer.save()
            return Response(beneficiaries_serializer.data, status=status.HTTP_201_CREATED) 
        return Response(beneficiaries_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = Beneficiary.objects.all().delete()
        return JsonResponse({'message': '{} All Beneficiaries successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
    
# single beneficiary view   
@api_view(['GET', 'PUT','DELETE','POST'])
@permission_classes((IsAuthenticated,))
def beneficiary_details(request, beneficiary_id):
    try: 
        beneficiary = Beneficiary.objects.get(id=beneficiary_id) 
    except Beneficiary.DoesNotExist: 
        return JsonResponse({'message': 'Not found'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        beneficiary_serializer = BeneficiariesSerializer(beneficiary,many=True) 
        return Response(beneficiary_serializer.data) 
    elif request.method == 'PUT': 
        beneficiary_data = JSONParser().parse(request) 
        beneficiary_serializer = BeneficiariesSerializer(beneficiary, data=beneficiary_data) 
        if beneficiary_serializer.is_valid(): 
            beneficiary_serializer.save() 
            return JsonResponse(beneficiary_serializer.data) 
        return JsonResponse(beneficiary_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE': 
        beneficiary.delete() 
        # return redirect('http://127.0.0.1:8000/beneficiaries/')
        return JsonResponse({'message': 'Beneficiary deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    

# each charity beneficiary list  
@api_view(['GET', 'PUT','DELETE','POST'])
@permission_classes((AllowAny,))
def charitybeneficiaries_list(request, charity_id):
    try:
        charities = Charity.objects.get(id=charity_id)
        beneficiary = Beneficiary.objects.filter(charity=charities)
    except Beneficiary.DoesNotExist: 
        return JsonResponse({'message': 'Not found'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        beneficiary_serializer = BeneficiariesSerializer(beneficiary, many=True) 
        return Response(beneficiary_serializer.data) 
    elif request.method == 'POST':
        beneficiary_serializer = BeneficiariesSerializer(data=request.POST)
        if beneficiary_serializer.is_valid():
            beneficiary_serializer.save(charity_id=charity_id)
            return Response(beneficiary_serializer.data, status=status.HTTP_201_CREATED) 
        return Response(beneficiary_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE': 
        beneficiary.delete() 
        return JsonResponse({'message': 'Beneficiary deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    

# single charity beneficiary view   
@api_view(['GET', 'PUT','DELETE','POST'])
@permission_classes((AllowAny,))
def charitybeneficiary_details(request, charity_id, beneficiary_id):
    try: 
        beneficiary = Beneficiary.objects.get(id=beneficiary_id)
        charities = Charity.objects.get(id=charity_id) 
    except Beneficiary.DoesNotExist: 
        return Response({'message': 'Not found'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        beneficiary_serializer = BeneficiariesSerializer(beneficiary) 
        return Response(beneficiary_serializer.data) 
    elif request.method == 'PUT': 
        beneficiary_serializer = BeneficiariesSerializer(beneficiary, data=request.data) 
        if beneficiary_serializer.is_valid(): 
            beneficiary_serializer.save() 
            return JsonResponse(beneficiary_serializer.data, status=status.HTTP_200_OK) 
        return JsonResponse(beneficiary_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE': 
        beneficiary.delete() 
        return Response({'message': 'Beneficiary deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


# each charity's donations view
@api_view(['GET'])
@permission_classes((AllowAny,))
def CharitiesDonationsList(request, charity_id):
    try:
        charities = Charity.objects.get(id=charity_id)
        donations = Donations.objects.filter(charity=charities)
    except:
        if Donations.DoesNotExist:
            return Response({'message': 'No Donations for Charity {}'.format(charity_id)}, status=status.HTTP_404_NOT_FOUND)
        elif Charity.DoesNotExist: 
            return Response({'message': 'Charity Not found'}, status=status.HTTP_404_NOT_FOUND)   
    if request.method == 'GET': 
        donations_serializer = DonationsSerializer(donations, many=True) 
        return Response(donations_serializer.data) 
    
# each charity's single donation view
@api_view(['GET'])
# @permission_classes((AllowAny,))
@permission_classes((IsAuthenticated,))
def CharitiesDonationsdetails(request, charity_id, donation_id):
    try: 
        charities = Charity.objects.get(id=charity_id)
        donation = Donations.objects.get(charity=charities) 
        donation = Donations.objects.get(id=donation_id)        
    except: 
        if Donations.DoesNotExist:
            return Response({'message': 'Donation Not found'}, status=status.HTTP_404_NOT_FOUND)
        elif Charity.DoesNotExist: 
            return Response({'message': 'Charity Not found'}, status=status.HTTP_404_NOT_FOUND) 
    if request.method == 'GET': 
        donation_serializer = DonationsSerializer(donation) 
        return Response(donation_serializer.data) 
    
@api_view(['GET','POST','DELETE'])
@permission_classes((AllowAny,))
def anonnymous_donation(request):
    if request.method == 'GET':
        annonymous_donations = AnonymousDonation.objects.all()
        annonymous_serializer = AnonymousDonationSerializer(annonymous_donations, many=True,context={'request': request})
        return Response(annonymous_serializer.data)
    
    elif request.method == 'POST':
        # annonymous_data = JSONParser().parse(request)
        annonymous_serializer = AnonymousDonationSerializer(data=request.data)
        if annonymous_serializer.is_valid():
            annonymous_serializer.save()
            return Response(annonymous_serializer.data, status=status.HTTP_201_CREATED) 
        return Response(annonymous_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# each charity anonymous donations list  
@api_view(['GET', 'PUT','DELETE','POST'])
@permission_classes((AllowAny,))
def anonnymous_donation_list(request, charity_id):
    try: 
        charity = Charity.objects.get(id=charity_id)
        anonnymous_donations = AnonymousDonation.objects.filter(charity=charity) 
    except AnonymousDonation.DoesNotExist: 
        return Response({'message': 'Not found'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        beneficiary_serializer = AnonymousDonationSerializer(anonnymous_donations, many=True) 
        return Response(beneficiary_serializer.data)