# from rest_framework.test import APITestCase
# from .models import Reaction
# from users.models import User
# from videos.models import Video
# from django.urls import reverse
# from rest_framework import status

# class CommentAPITestCase(APITestCase):
#     def setup(self):
#         self.user = User.objects.create_user(
#             email= 'rudfhr@gmil.com',
#             password= '1234'
#         )
#         self.client.login(email= 'rudfhr@gmil.com', password= '1234')
#         self.video = Video.objects.create(
#             title= 'test video',
#             link= 'https://test.com',
#             user= self.user
#         )