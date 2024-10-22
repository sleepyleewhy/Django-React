from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {"password" : {"write_only": True}} # we dont want to give out the password when we need info about the user
        
    def create(self, validated_data):
        print("asdf")
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        return user
    
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'created_at']
        extra_kwargs = {'author' : {'read_only': True}} # we just want to show who the author is, not change it
        
        