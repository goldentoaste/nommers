from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    
    type = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            "type",
            "id",
            "userName",
            "ppiUrl"
        )

    def get_type(self, obj):
        return "User"


class LoginSerializer(serializers.Serializer):
    displayName = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)
