from django.db import models
from videos.models import Video
from common.models import CommonModel
from users.models import User

class Notification(CommonModel):
    message = models.CharField(max_length=255)
    is_read = models.BooleanField(default=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.SET_NULL, null=True)
