from django.shortcuts import get_object_or_404

from user_profile.models import UserProfile


class UserProfileRepository():

    @staticmethod
    def create_user(data):
        user = UserProfile.objects.create(name=data['name'], phoneNumber=data['phone'], pinCode=data['pinCode'])

        return user


    @staticmethod
    def check_if_user_exists(phoneNumber):
        return UserProfile.objects.filter(phoneNumber=phoneNumber).exists()

