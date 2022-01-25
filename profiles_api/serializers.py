from rest_framework import serializers
from .models import *
class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length = 10)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = UserProfile
        fields = ('id','email','name','password')
        extra_kwargs = {
            'password':{
                'write_only':True,
                'style':{'input_type':'password'}
            }
        }
    
    def create(self , vaildated_data):
        """Create and return a new user"""
        user = UserProfile.objects.create_user(
            email = vaildated_data['email'],
            name = vaildated_data['name'],
            password = vaildated_data['password']
            
        )
        return user


class ProfileFeedSerializer(serializers.ModelSerializer):
    """Create serializes for profile feed items"""

    class Meta:
        model  = ProfileFeedItem
        fields = ('id','user_profile','status_text','created_on')
        extra_kwargs = {
            'user_profile':{'read_only':True}
        }
