from rest_framework import serializers
from .models import User as user


class UserSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()
    username = serializers.CharField()
    birth = serializers.CharField()
    gender = serializers.CharField()

    class Meta:
        model = user
        fields = '__all__'

    def create(self, validated_data):
        return user.objects.create(**validated_data)

    def update(self, instance, validated_data):
        user.objects.filter(pk=instance.id).update(**validated_data)