from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from .serializers import RegistartionSerializer

from django.contrib.auth import get_user_model
User = get_user_model()


class RegistrationAPIView(GenericAPIView):
    """
    signup a user
    """
    # Allow any user (authenticated or not) to hit this endpoint.
    permission_classes = (AllowAny,)
    serializer_class = RegistartionSerializer

    def post(self, request):
        data = request.data

        # The create serializer, validate serializer, save serializer pattern
        # below is common and you will see it a lot throughout this course and
        # your own work later on. Get familiar with it.

        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        message = {
            "user": {
                "email": serializer.data.get('email'),
                "username": serializer.data.get("username")
            },
            "message": "Account created successfully. Check your email."
        }
        return Response(message, status=status.HTTP_201_CREATED)
