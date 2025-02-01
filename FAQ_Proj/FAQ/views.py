from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FAQ
from .serializers import FAQSerializer

class FAQListView(APIView):
    """Fetch all FAQs, with language support via ?lang= query parameter"""

    def get(self, request):
        faqs = FAQ.objects.all()
        serializer = FAQSerializer(faqs, many=True, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)
