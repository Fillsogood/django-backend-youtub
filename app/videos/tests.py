from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from users.models import User
from .models import Video
from django.core.files.uploadedfile import SimpleUploadedFile
import pdb

class VideoAPITestCase(APITestCase):
    # 테스트 코드가 실행되기 전 (1) 유저 생성 (2) 비디오 생성
    def setUp(self):
        # 유저 생성
        self.user = User.objects.create_user(
            email= 'rudfhr@gmil.com',
            password= '1234'
        )
        self.client.login(email= 'rudfhr@gmil.com', password= '1234')

        # 비디오 생성
        self.video = Video.objects.create(
            title= 'test video',
            link= 'https://test.com',
            user= self.user
        )

    def test_viedo_list_get(self):
        url = reverse('video_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(len(response.data), 1)

    def test_viedo_detail_get(self):
        url = reverse('video_detail', kwargs={'pk': self.video.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_video_list_post(self):
        url = reverse('video_list')
        print("user:", self.user)
        data = {
            'title': 'test video',
            'link': 'https://test.com',
            'category': 'test category',
            'thumbnail': 'https://test.com',
            'video_uploaded_url': 'https://test.com',
            'video_file': SimpleUploadedFile('file.mp4', b'file content', content_type='video/mp4'),
            'user': self.user.pk # 1
        }
        response = self.client.post(url, data)
        # pdb.set_trace()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_video_detail_put(self):
        url = reverse('video_detail', kwargs={'pk': self.video.pk})
        data = {
            'title': 'test video2',
            'link': 'https://test1.com',
            'category': 'test category1',
            'thumbnail': 'https://test1.com',
            'video_uploaded_url': 'https://test1.com',
            'video_file': SimpleUploadedFile('file1.mp4', b'file content', content_type='video/mp4'),
            'user': self.user.pk # 1
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'test video2')

    def test_video_detail_delete(self):
        url = reverse('video_detail', kwargs={'pk': self.video.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        respones = self.client.get(url)
        self.assertEqual(respones.status_code, status.HTTP_404_NOT_FOUND)
