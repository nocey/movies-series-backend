from datetime import datetime
from rest_framework import serializers
from moviesandseries.api.models import Movie
from django.utils.timesince import timesince


class MovieSerializer(serializers.ModelSerializer):
    time_since_publication = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        # fields = "__all__" # what we see in the api
        exclude = ["id"]  # what we dont see in the api
        read_only_fields = ["id", "updated_at", "created_at"]
        managed = True
        verbose_name = "Movie"
        verbose_name_plural = "Movies"

    def get_time_since_publication(self, object):
        now = datetime.now()
        publicaton_date = object.publicaton_date
        time_delta = timesince(publicaton_date, now.replace(tzinfo=None))
        return time_delta


# # Default Movie Serializer
# class MovieDefaultSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     author = serializers.CharField()
#     publicaton_date = serializers.DateTimeField()
#     updated_at = serializers.DateTimeField(read_only=True)
#     created_at = serializers.DateTimeField(read_only=True)

#     def create(self, validated_data):
#         return super().create(validated_data)

#     def update(self, instance, validated_data):
#         return super().update(instance, validated_data)
