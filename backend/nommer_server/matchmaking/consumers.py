

import json

from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer

from asgiref.sync import async_to_sync
from channels.db import database_sync_to_async
from .models import Member, Party, Vote
from user.models import User
from django.db.models import F
class EchoWSConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        
        self.roomName = self.scope['url_route']['kwargs']['partyid']
        self.memberId = self.scope['url_route']['kwargs']['memberid']
        
        self.groupName = f"group{self.roomName}"
        
        # join group
        await self.channel_layer.group_add(
            self.groupName, self.channel_name
        )
        
        await self.accept()
        await self.channel_layer.group_send(
            self.groupName, {
                "type":"messageEvent",
                "message": "join"
            }
        )
        await self.addMember()

    @database_sync_to_async
    def countMember(self):
        return Member.objects.filter(
            party__id=int(self.groupName)
        ).count()

    @database_sync_to_async
    def addMember(self):
        party= Party.objects.get(id = int(self.roomName))
        member = User.objects.get(id=self.memberId)
        Member.objects.create(party = party, member=member)

    async def disconnect(self, code):
    
        await self.channel_layer.group_discard(
            self.groupName, self.channel_name
        )
    
    async def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        
        message = data['message']

        if message =="echo":
            return await self.send(
                text_data=json.dumps(
                    {
                        "message": "echoing back at you."
                    }
                )
            )
        
        if message =="vote":
            placeid = data['placeid']
            upvote = data['upvote']

            await self.incrementvote(placeid, upvote)

        if message =="start":
            await self.channel_layer.group_send(
                self.groupName,
                {
                    "type":"messageEvent",
                    "message": "start"
                }
            )

        if message == "finish":
            finishcount, fullstop =  await self.finish() 

            if fullstop:
                await self.channel_layer.group_send(
                self.groupName,
                {
                    "type":"messageEvent",
                    "message": "fullstop"
                }
            )
            else:
                await self.channel_layer.group_send(
                self.groupName,
                {
                    "type":"messageEvent",
                    "message": f"finish count:{finishcount}"
                }
            )
        
        if message == "fullstop":
            await self.channel_layer.group_send(
                self.groupName,
                {
                    "type":"messageEvent",
                    "message": "fullstop",
                    "results": await self.fullstop()
                }
            )

    @database_sync_to_async
    def fullstop(self):
        votes  = Vote.objects.filter(party__id=int(self.roomName))

        res = {}
        vote : Vote
        for vote in votes:
            res[vote.placeid] = {
                "upvotes": vote.upvotes,
                "downvotes": vote.downvotes
            }
        return votes

    @database_sync_to_async
    def finish(self):
        count = Member.objects.filter(
            party__id=int(self.groupName)
        ).count()

        finishcount = Member.objects.filter(
            party__id=int(self.groupName),
            finished=True
        ).count()

        return finishcount, finishcount == count
            

        
    
        
    @database_sync_to_async
    def incrementvote(self, placeid, inc = True):
        view = Vote.objects.filter(
            party__id = int(self.roomName),
            placeid=placeid
        )
        if inc:
            view.update(upvotes=F('upvotes')+1)
        else:
            view.update(downvotes=F("downvotes")+1)

    async def messageEvent(self, event):
        message = event['message']
        
        if message == "join":
            return await self.send(text_data=json.dumps({
                "message": f"total count:{await self.countMember()}"
            }))


        if 'finish' in message:
            return await self.send(
                text_data=json.dumps(
                    {
                        "message": message  
                    }
                )
            )

        if "fullstop" in message:
            return await self.send(
                text_data=json.dumps(
                    {
                        "message": message,
                        "result": event["result"]
                    }
                )
            )
        
        if message == "start":
            return await self.send(
                text_data=json.dumps(
                    {
                        "message": "start",
                 
                    }
                )
            )