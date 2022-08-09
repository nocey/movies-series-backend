from django.urls import path
from moviesandseries.api import views as api_views


urlpatterns = [
    path("movie/<int:pk>", api_views.MovieDetail.as_view()),
    # path("movies", api_views.movies),
    # path("serie", api_views.serie),
    # path("series", api_views.series),
]
