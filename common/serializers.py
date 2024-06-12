from rest_framework import serializers
from .models import Usuario


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ["username", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}