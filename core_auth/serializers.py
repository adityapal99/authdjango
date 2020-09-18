from rest_framework import serializers
from .models import User

class UserDetailsSerializers(serializers.ModelSerializer):
    class Meta:
        models = User
        fields = ['email', 'first_name', 'last_name', 'username', 'age', 'profile_pic']
