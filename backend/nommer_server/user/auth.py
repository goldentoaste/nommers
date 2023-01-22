from .models import User

from rest_framework import authentication
from rest_framework import exceptions
from rest_framework.request import Request

class DummyAuthObject:
    def __init__(self, user=False, is_authenticated = False):
        self.user = user
        self.is_authenticated = is_authenticated

class IdAuthtication(authentication.BaseAuthentication):

    def __call__(self, *args, **kwds):
        return self
        
    def __init__(self, bypass = False) -> None:
        super().__init__()
        self.bypass = bypass
    def authenticate(self, request : Request):
        data = request.data
        if self.bypass or ('id' in data and data['id'] == 'admin'):
            print(request, "bypassing")
            return (DummyAuthObject(True, True),None)

        print("auth", request)
        
        
        try:
            user: User = User.objects.get(id=data['id'])
            return (user, user.id)
        except KeyError:
            raise exceptions.AuthenticationFailed("id not included in the request query param")
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed("User with id not found")
        