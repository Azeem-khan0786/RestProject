from rest_framework import serializers
from .models import Student
from django.contrib.auth.models import User

class Student_serializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields=['id','name','age','address']

    def validate(self, data):
        if data['age']<18:
            raise serializers.ValidationError({'error':"Age is not valid fo votes"})
        if data['name']:
            for n in data['name']:
                if not n.isalpha():
                    raise serializers.ValidationError({'error':"Name should contain only alphabets"})

        return data
            
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=['id','username','email']