

import json

from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer

from asgiref.sync import async_to_sync

class EchoWSConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        
        self.roomName = self.scope['url_route']['kwargs']['name']
        self.groupName = f"group{self.roomName}"
        
        # join group
        await self.channel_layer.group_add(
            self.groupName, self.channel_name
        )
        
        await self.accept()
        self.send("Connected.")
    
    async def disconnect(self, code):
    
        await self.channel_layer.group_discard(
            self.groupName, self.channel_name
        )
    
    async def receive(self, text_data=None, bytes_data=None):
        
        data = json.loads(text_data)
        
        message = data['message']
        

        await self.channel_layer.group_send(
            self.groupName, {
                "type":"messageEvent",
                "message":message
            }
        )
        
    async def messageEvent(self, event):
        message = event['message']
        
        await self.send(text_data=json.dumps({
            "message": f"incoming: {message}"
        }))