from django.urls import re_path,path

from . import consumers


websocket_urlpatterns = [
    
    re_path(r"ws/(?P<partyid>[A-Za-z0-9_\-]+)/(?P<memberid>[A-Za-z0-9_\-]+)/?$", consumers. EchoWSConsumer.as_asgi())
]