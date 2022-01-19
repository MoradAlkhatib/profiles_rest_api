from os import name
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import HelloSerializer
from rest_framework import status

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