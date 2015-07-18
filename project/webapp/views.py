from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from models import User
from models import Route
from models import GeoPoint

from serializers import UserSerializer
from serializers import RouteSerializer
from serializers import GeoPointSerializer


@api_view(['GET', 'PUT'])
def user_collection(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data)


@api_view(['GET', 'PUT'])
def routes_collection(request):
    if request.method == 'GET':
        routes = Route.objects.all()
        serializer = RouteSerializer(routes, many=True)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = RouteSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data)


@api_view(['GET', 'PUT'])
def geo_points_collection(request):
    if request.method == 'GET':
        geo_points = GeoPoint.objects.all()
        serializer = GeoPointSerializer(geo_points, many=True)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = GeoPointSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data)
