
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
        """Handel a partial update of an object"""
        return Response({'method':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    def get(self,request):
        """Return Hello Message"""

        a_viewset =['Uses actions (list, create, retrieve, update, partial_update)',
                    'Automatically maps to URLS using Routers',
                    'Provides more functionality with less code',]
        
        return Response({'message':'Hello!','a_viewset':a_viewset})