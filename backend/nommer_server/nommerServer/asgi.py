"""
ASGI config for nommerServer project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from channels.auth import AuthMiddlewareStack


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nommerServer.settings")

http_app =  get_asgi_application()
import  matchmaking.routing 
application = ProtocolTypeRouter(
    {

        "http":http_app,
        "websocket": AllowedHostsOriginValidator(
          
                URLRouter(
                    matchmaking.routing.websocket_urlpatterns
                )
            
        )
    }
)