from rest_framework.test import APITestCase
from .models import Subscription
from users.models import User
from django.urls import reverse
from rest_framework import status
import pdb

class subscriptionTestCase(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(
            email= 'rudfhr@gmil.com',
            password= '1234'
        )
        self.user2 = User.objects.create_user(
            email= 'rudfhr1@gmil.com',
            password= '12345'
        )
        self.client.login(email= 'rudfhr@gmil.com', password= '1234')


    
    # api/v1/subscriptions
    # SubscriptionList
    # [POST]: 구독하기 버튼 클릭
    def test_sub_list_post(self):
        url = reverse('subscription_list')
        data ={
            'subscriber': self.user1.pk,
            'subscribed_to': self.user2.pk
        }
        res = self.client.post(url, data)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Subscription.objects.count(), 1)
        self.assertEqual(Subscription.objects.get().subscribed_to, self.user2)

    # api/v1/subscriptions/{user_id}
    # SubscriptionDetail
    # [DELETE]: 구독 취소

    def test_sub_detail_delete(self):
        subs = Subscription.objects.create(subscriber=self.user1, subscribed_to=self.user2)

        url = reverse('subscription_detail', kwargs={'pk': subs.id})
        res = self.client.delete(url)

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Subscription.objects.count(), 0)