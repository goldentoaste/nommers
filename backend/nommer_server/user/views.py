
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer, LoginSerializer
from rest_framework import status
from django.contrib.auth import authenticate
from django.db.utils import IntegrityError 
from .auth import IdAuthtication


@api_view(["POST"])
@authentication_classes([IdAuthtication(bypass=True)])
def signUp(request: Request):
    data : dict = request.data # type: ignore
    try:
        user = User.objects.create_user(
            data['userName'],
            data['password'],
            data['ppiUrl']
        )
        serial = UserSerializer(user)
        return Response(serial.data, status=status.HTTP_201_CREATED)
    except (ValueError, AttributeError) as error:
        # missing params
        return Response(str(error), status=status.HTTP_400_BAD_REQUEST)
    except IntegrityError as error:
        return Response(str(error), status=status.HTTP_409_CONFLICT)

@api_view(["POST"])
@authentication_classes([IdAuthtication(bypass=True)])
def signIn(request:Request):
    data :dict = request.data # type: ignore

    serial = LoginSerializer(data=data) # type: ignore
    if not serial.is_valid():
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    user = authenticate(username=serial.data['userName'], password=serial.data["password"])
    if not user:
        return Response(
            "Invalid login info.",
            status=status.HTTP_401_UNAUTHORIZED
        )
    return Response(UserSerializer(user).data, status=200)

    


@api_view(["GET"])
@authentication_classes([IdAuthtication(bypass=True)])
def health_check(reqeust):
    return Response(status=200)