from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from shorter.serializer import ShorterSerializer
from django.shortcuts import get_object_or_404
from shorter.models import Shorter

# Create your views here.
class ShorterViewSet(APIView):

    queryset = Shorter.objects.all()
    serializer_class = ShorterSerializer
    lookup_field = 'shortened_url'

    def get(self, request, shortened_url, *args, **kwargs):
        instance = get_object_or_404(Shorter, shortened_url=shortened_url)
        return Response(ShorterSerializer(instance, context={'request': request}).data)

    def post(self, request, *args, **kwargs):
        original_url = request.data.get("original_url")

        if not original_url:
            return Response({"error": "original_url is required"}, status=status.HTTP_400_BAD_REQUEST)

        instance = Shorter.objects.filter(original_url=original_url).first()
        if instance:
            serializer = ShorterSerializer(instance, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)

        serializer = ShorterSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

