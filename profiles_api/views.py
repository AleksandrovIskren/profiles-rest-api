from rest_framework.views import APIView
from rest_framework.response import Response

"""
APIViews are used when:
 - Need full control over the logic
 - Processing files and rendering a synchronous Response
 - You are calling other APIs/services
 - Accessing local files or data
"""

class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Need full control over the logic',
            'Processing files and rendering a synchronous Response',
            'You are calling other APIs/services',
            'Accessing local files or data',
        ]
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})


    def post(self, request, format=None):
        """Create a new item"""
        return Response({'new': 'item'})

    def put(self, request, format=None):
        """Update an Item"""
        return Response({'updated': 'item'})

    def patch(self, request, format=None):
        """Partially update an item"""
        return Response({'partially_updated': 'item'})

    def delete(self, request, format=None):
        """Delete an item"""
        return Response({'deleted': 'item'})
