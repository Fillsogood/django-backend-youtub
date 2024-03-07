from django.urls import path
from . import views
urlpatterns = [
    path('', views.SubscriptionsListView.as_view(), name='subscription_list'),
    path('<int:pk>/', views.SubscriptionsDetailView.as_view(), name='subscription_detail')
]