from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from profiles_api import serializers


class HelloApiView(APIView):

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):

        an_apiview =[
            'one','two','three'
        ]
        return(Response({'message':'hello', 'an_apiview': an_apiview}))

    def post(self, request):
        """create a hello message with our name"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name= serializer.validated_data.get('name')
            message = 'hello {}'.format(name)
            return(Response({'message': message}))

    def put(self, request, pk=None):
        """ Handle updating an object"""
        return(Response({'method':'PUT'}))

    def patch(self, request, pk=None):
        """partial update"""
        return(Response({'method':'PATCH'}))


    def delete(self, request, pk=None):
        """partial update"""
        return(Response({'method':'Delete'}))


class HelloViewSet(viewsets.ViewSet):
    """test API View Set"""

    serializer_class = serializers.HelloSerializer
    def list(self, request):

        a_viewset= [
            'one','two','three'
        ]

        return(Response({"a_viewset":a_viewset}))


    def create(self,request):

        serializer =self.serializer_class(data = request.data)

        if serializer.is_valid():
            name= serializer.validated_data.get('name')
            message = 'hello {}'.format(name)
            return(Response({'message': message}))

    def retrieve(self,request, pk =None):
        return(Response({'method':'get'}))

    def update(self,request, pk=None):
        """partial update"""
        return(Response({'method':'put'}))

    def partial_update(self, request, pk=None):
        """partial update"""
        return(Response({'method':'partial_update/patch'}))

    def destroy(self, request, pk=None):
        """partial update"""
        return(Response({'method':'delete'}))