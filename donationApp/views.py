from django.shortcuts import render
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Charity,Donor,Donations,CustomUser,BenefactorsStory,Beneficiaries
from .serializer import CharitySerializer,DonorSerializer,DonationsSerializer,UsersSerializer,BenefactorSerializer,BeneficiarySerializer
from rest_framework import status

from rest_framework.parsers import MultiPartParser, JSONParser

import cloudinary.uploader
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token



# Create your views here.
def home(request):
  return render(request, 'home.html')

# Donors
class DonorList(APIView):
  def get(self, request, format=None):
    all_donors = Donor.objects.all()
    serializers = DonorSerializer(all_donors,many=True)
    return Response(serializers.data)

  def post(self, request, format=None):
    serializers = DonorSerializer(data=request.data)
    if serializers.is_valid():
      serializers.save()
      return Response(serializers.data,status=status.HTTP_201_CREATED)
    return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)


class DonorDescription(APIView):
  def get_donor(self, pk):
        try:
            return Donor.objects.get(pk=pk)
        except Donor.DoesNotExist:
            return Http404

  def get(self, request, pk, format=None):
      donor = self.get_donor(pk)
      serializers = DonorSerializer(donor)
      return Response(serializers.data)

  def put(self, request, pk, format=None):
    donor = self.get_donor(pk)
    serializers = DonorSerializer(donor, request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data)
    else:
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
    donor = self.get_donor(pk)
    donor.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# Donations
class DonationsList(APIView):
  def get(self, request, format=None):
    all_donations = Donations.objects.all()
    serializers = DonationsSerializer(all_donations,many=True)
    return Response(serializers.data)

  def post(self, request, format=None):
    serializers = DonationsSerializer(data=request.data)
    if serializers.is_valid():
      serializers.save()
      return Response(serializers.data,status=status.HTTP_201_CREATED)
    return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

class DonationsDescription(APIView):
  def get_donations(self, pk):
        try:
            return Donations.objects.get(pk=pk)
        except Donations.DoesNotExist:
            return Http404

  def get(self, request, pk, format=None):
      donations = self.get_donations(pk)
      serializers = DonationsSerializer(donations)
      return Response(serializers.data)

  def put(self, request, pk, format=None):
    donations = self.get_donations(pk)
    serializers = DonationsSerializer(donations, request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data)
    else:
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
    donations = self.get_donations(pk)
    donations.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# User
class UsersList(APIView):
  def get(self, request, format=None):
    all_users = CustomUser.objects.all()
    serializers = UsersSerializer(all_users,many=True)
    return Response(serializers.data)

  def post(self, request, format=None):
    # request.data['user'] = user
    serializers = UsersSerializer(data=request.data)
    if serializers.is_valid():
      serializers.save()
      return Response(serializers.data,status=status.HTTP_201_CREATED)
    return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

class UserDescription(APIView):
  def get_user(self, pk):
    try:
        return CustomUser.objects.get(pk=pk)
    except CustomUser.DoesNotExist:
        return Http404

  def get(self, request, pk, format=None):
    user = self.get_user(pk)
    serializers = UsersSerializer(user)
    return Response(serializers.data)

  def put(self, request, pk, format=None):
    user = self.get_user(pk)
    serializers = UsersSerializer(user, request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data)
    else:
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
    user = self.get_user(pk)
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# Charities
class CharityList(APIView):
  def get(self, request, format=None):
    all_charities = Charity.objects.all()
    serializers = CharitySerializer(all_charities,many=True)
    return Response(serializers.data)
  
  def post(self, request, format=None):
    serializers = CharitySerializer(data=request.data)
    if serializers.is_valid():
      serializers.save()
      return Response(serializers.data,status=status.HTTP_201_CREATED)
    return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

class CharityDescription(APIView):
  def get_charity(self, pk):
        try:
            return Charity.objects.get(pk=pk)
        except Charity.DoesNotExist:
            return Http404

  def get(self, request, pk, format=None):
      charity = self.get_charity(pk)
      serializers = CharitySerializer(charity)
      return Response(serializers.data)

  def put(self, request, pk, format=None):
    charity = self.get_charity(pk)
    serializers = CharitySerializer(charity, request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data)
    else:
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
    charity = self.get_charity(pk)
    charity.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# beneficiaries
class BenefactorsList(APIView):

  def get(self, request, format=None):
    all_benefactor = BenefactorsStory.objects.all()
    serializers = BenefactorSerializer(all_benefactor,many=True)
    return Response(serializers.data)
  

  def post(self, request):

    serializers = BenefactorSerializer(data=request.data)
    if serializers.is_valid():
      serializers.save()
      return Response(serializers.data,status=status.HTTP_201_CREATED)
    return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)


class BenefactorDescription(APIView):
  def get_benefactor(self, pk):
        try:
            return BenefactorsStory.objects.get(pk=pk)
        except BenefactorsStory.DoesNotExist:
            return Http404

  def get(self, request, pk, format=None):
      benefactor = self.get_benefactor(pk)
      serializers = BenefactorSerializer(benefactor)
      return Response(serializers.data)

  def put(self, request, pk, format=None):
    benefactor = self.get_benefactor(pk)
    serializers = BenefactorSerializer(benefactor, request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data)
    else:
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
    benefactor = self.get_benefactor(pk)
    benefactor.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# Beneficiary
class BeneficiaryList(APIView):
  # parser_classes = (
  #       MultiPartParser,
  #       JSONParser,
  #   )
  def get(self, request, format=None):
    all_beneficiaries = Beneficiaries.objects.all()
    serializers = BeneficiarySerializer(all_beneficiaries,many=True)
    return Response(serializers.data)

  def post(self, request, format=None):
    # request.data['user'] = user
    serializers = BeneficiarySerializer(data=request.data)
    if serializers.is_valid():
      serializers.save()
      return Response(serializers.data,status=status.HTTP_201_CREATED)
    return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

  # def post(self, request, format=None):
  #    file = request.data.get('picture')
  #    upload_data = cloudinary.uploader.upload(file)
  #    return Response({
  #           'status': 'success',
  #           'data': upload_data,
  #       }, status=201)

class BeneficiaryDescription(APIView):
  def get_beneficiary(self, pk):
    try:
        return Beneficiaries.objects.get(pk=pk)
    except Beneficiaries.DoesNotExist:
        return Http404

  def get(self, request, pk, format=None):
    beneficiary = self.get_beneficiary(pk)
    serializers = BeneficiarySerializer(beneficiary)
    return Response(serializers.data)

  def put(self, request, pk, format=None):
    beneficiary = self.get_beneficiary(pk)
    serializers = BeneficiarySerializer(beneficiary, request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data)
    else:
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
    beneficiary = self.get_beneficiary(pk)
    beneficiary.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

class CustomAuthToken(ObtainAuthToken):
  def post(self, request, *args, **kwargs):
    serializer = self.serializer_class(data=request.data,
                                          context={'request': request})
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    token, created = Token.objects.get_or_create(user=user)
    return Response({
        'token': token.key,
        'username': user.user_name,
        'is_admin':user.is_admin,
        'is_charity':user.is_charity,
        'is_donor':user.is_donor,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'user_id': user.pk,
        'email': user.email
      })     