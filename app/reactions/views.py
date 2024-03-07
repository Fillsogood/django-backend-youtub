from rest_framework.views import APIView, Response, status
from .models import Reaction
from .serializers import ReactionSerializer
from videos.models import Video
from django.shortcuts import get_object_or_404
class ReactionDetailView(APIView):
    def post(self,requset,video_id):
        user_data =requset.data        
        serializer = ReactionSerializer(data=user_data)
        serializer.is_valid(raise_exception=True)

        reaction_obj, created = Reaction.objects.get_or_create(
            video=get_object_or_404(Video,id=video_id),
            user=requset.user,
            defaults={'reaction': serializer.validated_data['reaction']}
        )
        # created: boolean (True: 새로 생성, False: 기존 객체가 존재한다.)
        if created:
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # -이미 기존 데이터가 존재한다면 => UPDATE
        if not created:
            reaction_obj.reaction = serializer.validated_data['reaction']
            reaction_obj.save()
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        # 좋아요를 클릭했는데
       
        # -이미 기존 데이터가 없다면 => CREATE