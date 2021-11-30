from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User

class RegistartionSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message='User already exists'
            )
        ]
    )

    password = serializers.CharField(
        write_only=True,
        required=True
    )

    username = serializers.RegexField(
        regex='^(?!.*\ )[A-Za-z\d\-\_]+$',
        required=True,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message='user with this username already exists',
            )
        ],
        error_messages={
            'invalid': 'Username can only contain letters, numbers, underscores, and hyphens',
            'required': 'Username is a required field'
        }
    )


    class Meta:
        model = User
        # List all of the fields that could possibly be included in a request
        # or response, including fields specified explicitly above.
        fields = ['email', 'username', 'password']

    def create(self, validated_data):
        # Use the `create_user` method we wrote earlier to create a new user.
        return User.objects.create_user(**validated_data)
