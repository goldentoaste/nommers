from models import User

from rest_framework import authentication
from rest_framework import exceptions
from rest_framework.request import Request

class IdAuthtication(authentication.BaseAuthentication):
    
    
    def authenticate(self, request : Request):
        print("auth", request)
        data = request.data
        
        try:
            user: User = User.objects.get(id=data['id'])
            return (user, user.id)
        except KeyError:
            raise exceptions.AuthenticationFailed("id not included in the request query param")
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed("User with id not found")
        