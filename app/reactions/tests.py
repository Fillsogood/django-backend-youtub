from rest_framework.test import APITestCase
from .models import Reaction
from users.models import User
from videos.models import Video
from django.urls import reverse
from rest_framework import status
import pdb
# ReactionDetail


class ReactionAPITestCase(APITestCase):
    # 테스트 코드 실행 전에 필요한 더미 데이터 생성
    def setUp(self):
        self.user = User.objects.create_user(
            email= 'rudfhr@gmil.com',
            password= '1234'
        )
        self.client.login(email= 'rudfhr@gmil.com', password= '1234')
        self.video = Video.objects.create(
            title= 'test video',
            link= 'https://test.com',
            user= self.user
        )
    # POST - 좋아요, 싫어요 생성 및 업데이트
    def test_reaction_detail_post(self):
        url = reverse('video_reaction', kwargs={'video_id': self.video.id})
        data ={
        'reaction': Reaction.LIKE
        }
        res = self.client.post(url, data)
        # pdb.set_trace()
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Reaction.objects.count(), 1)
        self.assertEqual(Reaction.objects.get().reaction, Reaction.LIKE)



    # DELETE - 좋아요, 삻어요 삭제
    def test_reaction_detail_delete(self):
        pass        
