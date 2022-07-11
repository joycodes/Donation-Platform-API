from rest_framework import serializers
from .models import *

class CharitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Charity
        fields = '__all__'


class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donor
        fields = '__all__'

class DonationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donations
        fields = '__all__'

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'

class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = '__all__'