from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import Users

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'gender', 
            'birth_date',
            'password'
            ]
        extra_kwargs = {
            'password': {'write_only':True}
        }
    
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        data['token'] = data.pop('access')
        # Add custom response data
        data['user'] = {
            'id': self.user.id,
            'username': self.user.username,
            'email': self.user.email
        }

        return data
    
class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = [
            'id',
            'username',
        ]