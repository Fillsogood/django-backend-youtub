from django.db import models
from common.models import CommonModel
from users.models import User
from videos.models import Video


class Reaction(CommonModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)

    LIKE = 1
    DISLIKE = -1
    NO_REACTION = 0

    REACTION_CHOICES = (
        (LIKE,'LIKE'),
        (DISLIKE,'DISLIKE'),
        (NO_REACTION,'NO_REACTION'),
    )
    
    reaction = models.IntegerField(
        choices=REACTION_CHOICES,
        default=NO_REACTION
    )

    @staticmethod
    def get_video_reaction(video):
        reactions = Reaction.objects.filter(video=video).aggregate(
            likes_count = models.Count('pk', filter=models.Q(reaction=Reaction.LIKE)),
            dislikes_count = models.Count('pk', filter=models.Q(reaction=Reaction.DISLIKE))
        )
        return reactions