from rest_framework import serializers
from .models import UserProfile, ProfileFeedItem

class HelloSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=20)


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model= UserProfile
        fields= ('id', 'name', 'email', 'password')
        extra_kwargs={
            'password': {
                'write_only': True,
                'style': {
                    'input_type' : 'password'
                }
            }
        }

    def create(self, validated_data):
        user= UserProfile.objects.create_user(
            email=validated_data['email'],
            name= validated_data['name'],
            password=validated_data['password']
        )
        return user

class ProfileFeedSerializer(serializers.ModelSerializer):

    class Meta:
        model= ProfileFeedItem
        fields= ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs= {
            'user_profile': {
                'read_only': True
        }
        }