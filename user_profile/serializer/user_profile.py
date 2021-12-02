from rest_framework import serializers
from user_profile.models import UserProfile


class UserProfileValidator(serializers.Serializer):

    name = serializers.CharField(max_length=255, allow_null=False, allow_blank=False)
    phoneNumber = serializers.CharField(max_length=10, allow_null=False, allow_blank=False)
    pinCode = serializers.CharField(max_length=10, allow_null=False, allow_blank=False)


class AdminProfileValidator(serializers.Serializer):

    name = serializers.CharField(max_length=255, allow_null=False, allow_blank=False)
    phoneNumber = serializers.CharField(max_length=10, allow_null=False, allow_blank=False)
    pinCode = serializers.CharField(max_length=10, allow_null=False, allow_blank=False)
