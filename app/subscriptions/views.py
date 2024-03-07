from rest_framework.views import APIView, Response, status
from .serializers import SubscriptionSerializer
from .models import Subscription
from django.shortcuts import get_object_or_404

class SubscriptionsListView(APIView):
    def post(self, request):
        user_data = request.data
        serializer = SubscriptionSerializer(data=user_data)
        serializer.is_valid(raise_exception=True)
        serializer.save(subscriber=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class SubscriptionsDetailView(APIView):
    def delete(self, request, pk):
        subs = get_object_or_404(Subscription, id=pk, subscriber=request.user)
        subs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
