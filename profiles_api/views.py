from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test Api View"""
    def get(self, request, format=None):
        """Retun a list of APIViews features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar a traditional a Django view',
            'Gives you the most control over you aplicattion logic',
            'is mapped manually to Urls',
        ]

        return Response({'message':'Hello World', 'an_apiview':an_apiview})
