from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .exceptions import UserAreadyExists
from .serializer.user_profile import UserProfileValidator, AdminProfileValidator
from .repository.user_profile import UserProfileRepository
from .repository.admin_profile import AdminProfile


class UserProfile(APIView):

    def post(self, request):

        serializer = UserProfileValidator(data=request.data)
        if not serializer.is_valid():
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={
                    'message': serializer.errors
                }
            )

        validated_data = serializer.validated_data

        try:

            if UserProfileRepository.check_if_user_exists(validated_data['phoneNumber']):
                raise UserAreadyExists

            user = UserProfileRepository.create_user(validated_data)

            return Response(
                status=status.HTTP_201_CREATED,
                data={
                    "userId": user.id
                }
            )

        except UserAreadyExists as e:

            return Response(
                status=status.HTTP_409_CONFLICT,
                data={
                    'message': 'User already exists'
                }
            )

        except Exception as e:

            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                data={
                    "message": e
                }
            )


class AdminProfile(APIView):

    def post(self, request):

        serializer = AdminProfileValidator(data=request.data)
        if not serializer.is_valid():
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={
                    'message': serializer.errors
                }
            )

        validated_data = serializer.validated_data

        try:

            if UserProfileRepository.check_if_user_exists(validated_data['phoneNumber']):
                raise UserAreadyExists

            user = UserProfileRepository.create_user(validated_data)

            return Response(
                status=status.HTTP_201_CREATED,
                data={
                    "userId": user.id
                }
            )

        except UserAreadyExists as e:

            return Response(
                status=status.HTTP_409_CONFLICT,
                data={
                    'message': 'User already exists'
                }
            )

        except Exception as e:

            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                data={
                    "message": e
                }
            )