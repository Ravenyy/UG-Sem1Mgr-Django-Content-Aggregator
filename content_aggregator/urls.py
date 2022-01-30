from django.urls import path
from . import views

urlpatterns = [
    path('', views.subject_index, name='subject_index'),
    path("covidnews/", views.updatecovid, name="updatecovid"),
    path("gaming/", views.updategaming, name="updategaming"),
    path("worldnews/", views.updatenews, name="updatenews"),
    path("programming/", views.updateprogramming, name="updateprogramming"),
    path("science/", views.updatescience, name="updatescience"),
    path("technology/", views.updatetech, name="updatetech"),
    path("polskienewsy/", views.polskie, name="polskie"),
    path("worldnewspl/", views.swiatowe, name="swiatowe")
]
