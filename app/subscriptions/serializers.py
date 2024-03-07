from rest_framework.serializers import ModelSerializer, ValidationError
from .models import Subscription


class SubscriptionSerializer(ModelSerializer):
    class Meta:
        model = Subscription
        fields = ("__all__")

    def validate(self, data):
        if data['subscriber'] == data['subscribed_to']:
            raise ValidationError("You can't subscribe to yourself.")
        return data
