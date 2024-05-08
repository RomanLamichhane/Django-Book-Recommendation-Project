from rest_framework import serializers
from .models import User
from django.contrib.auth.models import Group
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields= ['username','password','email','seller']

    def create(self,validated_data):
        user=User.objects.create_user(**validated_data)
        seller=validated_data.get('seller')
        
        try:
            seller_group=Group.objects.get(name='seller')
            buyer_group=Group.objects.get(name='buyer')
        except Group.DoesNotExist:
            raise serializers.ValidationError('Group not Found')
        
        if seller:
            user.groups.add(seller_group)
        else:
            user.groups.add(buyer_group)
        user.save()
        return user
    

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields= ['username','email','seller']

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=128, write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'), username=username, password=password)

            if not user:
                msg = 'Unable to log in with provided credentials.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Must include "username" and "password".'
            raise serializers.ValidationError(msg, code='authorization')

        refresh = RefreshToken.for_user(user)
        attrs['refresh'] = str(refresh)
        attrs['access'] = str(refresh.access_token)
        attrs['user'] = user
        return attrs
    
class UserLogoutSerializer(serializers.Serializer):
    token = serializers.CharField(required=True)
        
        

    
