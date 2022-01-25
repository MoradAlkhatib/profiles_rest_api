
from email import message
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import HelloSerializer
from rest_framework import status
from rest_framework import viewsets


class HelloApiView(APIView):
    """Test API View"""
    
    serializer_class = HelloSerializer

    def get (self , request , format=None):
        """Resturns a list of APIViews features"""
        an_apiview = [
            'User HTTP method as function(get,post,patch,put,delete)',
            'Is similar to a traditional Django View',
            'Give you the most control over your application logic',
            'Is mapped manually to URLs',
        ] 
        return Response({'message':'Hello','an_apiview':an_apiview})
    
    def post(self,request):
        """Create a hello message with our name"""

        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else :
            return Response(serializer.errors,
            status = status.HTTP_400_BAD_REQUEST)

    def put(self , request , pk=None):
        """Handel update an object"""
        return Response({'method':'PUT'})
    
    def patch(self,request, pk=None):
        """Handel a partial update of an object"""
        return Response({'method':'PATCH'})

    def delete(self,request, pk=None):
        """Delete an object"""
        return Response({'method':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    serializer_class = HelloSerializer

    def list(self,request):
        """Return Hello Message"""

        a_viewset =['Uses actions (list, create, retrieve, update, partial_update)',
                    'Automatically maps to URLS using Routers',
                    'Provides more functionality with less code',]
        
        return Response({'message':'Hello!','a_viewset':a_viewset})
    
    def create(self,request):
        """Create a new Hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message':message})

        else :
            return Response(serializer.errors ,status.HTTP_400_BAD_REQUEST)

    def retrieve(self , request , pk=None):
        """Handel getting an object by its id"""
        return Response({'http_method':'GET'})

    def update(self , request , pk=None):
        """Handel update an object"""
        return Response({'http_method':'PUT'})

    def partial_update(self , request , pk=None):
        """Handel update part of an object"""
        return Response({'http_method':'PATCH'})

    def destroy(self , request , pk=None):
        """Handel remove an object"""
        return Response({'http_method':'DELETE'})
