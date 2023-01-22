from django.urls import re_path,path

from . import consumers


websocket_urlpatterns = [
    
    re_path(r"ws/(?P<partyid>\w+)/(?P<memberid>\w+)/?$", consumers. EchoWSConsumer.as_asgi())
]