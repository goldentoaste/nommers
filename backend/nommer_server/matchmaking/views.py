
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from user.models import User
from rest_framework import status
from django.contrib.auth import authenticate
from django.db.utils import IntegrityError 
import urllib.parse
import requests
import json
from .serializers import PartySerial
from .models import Party, Member, Vote
@api_view(["POST"])
def makeParty(request: Request) :

    data = request.data

    try:
        hostid = data['id']
        address = data['address']
        radius = data['radius']
        sortby = data['sortby']
        cost = data['cost']
        keywords  = data['keywords']
        rating = data['rating']
        opennow = data['opennow']
        
        res = requests.get(
            f'https://maps.googleapis.com/maps/api/geocode/json?key=AIzaSyBL_LkbEw80SHtaRjlV3t3KyPqJv_lsgtQ&address={urllib.parse.quote(address)}'
        ).json()
        if res['status'] != "OK":
            return Response(f"address {address} not found", status=404)
        res = res['results'][0]
        
        

        coords = res['geometry']['location']
        long = coords['lng']
        lat = coords['lat']

        radstr = f"&radius={radius}" if sortby=="prominence" else ""
        openstr = f"&opennow={str(opennow).lower()}" if opennow else ""


        req = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?key=AIzaSyBL_LkbEw80SHtaRjlV3t3KyPqJv_lsgtQ&type=restaurant&location={lat}%2C{long}&maxprice={cost}&keyword={' '.join(keywords)}&rankby={sortby.lower()}{radstr}{openstr}"
        
        res = requests.get(req).json()
        print("check" , req)
        results = []

        host =User.objects.get(id=hostid)
        party = Party.objects.create(host=host, response =results)

        for item in res['results']:
            if item["rating"] >= rating and item["price_level"] <= cost:
                results.append(
                    {
                        "id":item['place_id'],
                        "type": item['types'][0],
                        "name":item["name"],
                        "rating": item["rating"],
                        "price": item["price_level"],
                        "address": item['vicinity'],
                        "photoId": item["photos"][0]["photo_reference"],
                        "lat": item['geometry']['location']['lat'],
                        "long": item['geometry']['location']['lng'],
                        
                    }
                )
                Vote.objects.create(
                    party = party,
                    placeid = item['place_id']
                )

        
        serial = PartySerial(party)
        return Response(serial.data, status=200)

    except (KeyError, IndexError) as e:
        return Response(f"bad input: {str(e)}", status=status.HTTP_400_BAD_REQUEST)       