from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Serie, Sermon
from .serializers import SermonSerializer, SerieSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions

class SerieList(APIView):
    """
    List all code series, or create a new serie.
    """
    def get(self, request, format=None):
        series = Serie.objects.all()
        serializer = SerieSerializer(series, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SerieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class SerieDetail(APIView):
    """
    Retrieve, update or delete a code serie.
    """
    def get_object(self, pk):
        try:
            return Serie.objects.get(pk=pk)
        except Serie.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        serie = self.get_object(pk)
        serializer = SerieSerializer(serie)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        serie = self.get_object(pk)
        serializer = SerieSerializer(serie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer