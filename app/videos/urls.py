from django.urls import path
from . import views
from reactions.views import ReactionDetailView
urlpatterns = [
    path('',views.VideoList.as_view(), name='video_list'),
    path('<int:pk>/',views.VideoDetail.as_view(), name='video_detail'),
    path('<int:video_id>/reaction',ReactionDetailView.as_view(),name='video_reaction'),
]