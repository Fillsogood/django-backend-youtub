# VideoList
# api/v1/videos
# - GET: 전체 비디오 목록 조회
# - POST: 새로운 비디오 생성
from rest_framework.exceptions import NotFound
from .models import Video
from rest_framework.views import APIView, Response, status
from .serializers import VideoSerializer
# from reactions.models import Reaction
class VideoList(APIView):
    def get(self, request):
        videos = Video.objects.all()
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        try:
            user_data = request.data
            serializer = VideoSerializer(data=user_data)
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'msg':str(e)}, status=status.HTTP_400_BAD_REQUEST)




# VideoDetail
# api/v1/video/{video_id}
# - GET: 특정 비디오 상세 조회
# - PUT: 특정 비디오 정보 수정
# - DELETE: 특정 비디오 삭제

class VideoDetail(APIView):
    def get_object(self, pk):
        try:
            return Video.objects.get(id=pk)
        except Video.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        video = self.get_object(pk)
        serializer = VideoSerializer(video)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        video = self.get_object(pk)
        serializer =VideoSerializer(video,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)

    def delete(self, request, pk):
        try:
            video = self.get_object(pk)
            video.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'msg':str(e)}, status=status.HTTP_400_BAD_REQUEST)
    

        