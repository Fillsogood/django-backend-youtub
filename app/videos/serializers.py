from rest_framework import serializers
from videos.models import Video
from users.serializers import UserSerializer
from comments.serializers import CommentSerializer
from reactions.models import Reaction

class VideoSerializer(serializers.ModelSerializer,):
    user = UserSerializer(read_only=True)
    # reaction_set = ReactionSerializer(many=True,read_only=True)
    # reverse accessor 역참조
    comment_set = CommentSerializer(many=True, read_only=True)

    # likes_count = serializers.IntegerField(read_only=True)
    # dislikes_count = serializers.IntegerField(read_only=True)
    reactions = serializers.SerializerMethodField()
   
    class Meta:
        model = Video
        fields = '__all__' # video모델의 전체 필드를 보여줌
        depth = 1
    
    def get_reactions(self, video):
        return Reaction.get_video_reaction(video)