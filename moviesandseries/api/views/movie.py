# Response Function
from os import stat
from rest_framework import status
from rest_framework.response import Response

# Class view
from rest_framework.views import APIView

# if has no object return 404 error
from rest_framework.generics import get_object_or_404
from moviesandseries.api import serializers

# Movie Objects
from moviesandseries.api.models import Movie
from moviesandseries.api.serializers import MovieSerializer


class Movies(APIView):
    def get(self, request):
        pass

    def post(self, request):
        pass

    def update(self, request):
        pass


class MovieDetail(APIView):
    def get_object(self, pk):
        movie_instance = get_object_or_404(Movie, pk=pk)
        return movie_instance

    # Porforms return based on the id sent to us
    def get(self, request, pk):
        movie = self.get_object(pk=pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    def post(self, request, pk):
        pass

    # Performs update based on the id sent to us
    def put(self, request, pk):
        movie = self.get_object(pk=pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Performs deletion based on the id sent to us
    def delete(self, response, pk):
        pass
