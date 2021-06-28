from django.urls import path
from haber.api import views as api_views


urlpatterns = [
    path('yazarlar/',api_views.GazeteciListCreateAPIView.as_view(), name='yazar-listesi'),
    path('makaleler/',api_views.MakaleListCreateAPIView.as_view(), name='makale-listesi'),
    path('makaleler/<int:pk>', api_views.MakaleDetailAPIView.as_view(), name='makale-detay'),
]
