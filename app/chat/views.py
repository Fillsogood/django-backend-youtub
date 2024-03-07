from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Response, status
from .models import ChatRoom,CahtMessage
from .serializers import CahtRoomSerializer, ChatMessageSerializer
from django.shortcuts import render

def show_html(request):
    return render(request,'index.html')

# ChatRoom
# [GET]전체 채팅방을 조회
# [POST] 채팅방 생성
class ChatRoomList(APIView):
    def get(self, request):
        chatrooms = ChatRoom.objects.all()
        serializer = CahtRoomSerializer(chatrooms, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        user_data = request.data
        serializer = CahtRoomSerializer(data=user_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# Chatmessage
# [GET] 특정 채팅방의 채팅 내역 -> 카카오 채팅 서버(채팅 내역을 로컬에 저장)
# [POST] 채팅 메세지 생성
class ChatMessageList(APIView):
    def get(self, request, room_id):
        chatroom = get_object_or_404(ChatRoom, id=room_id) 
        messages = CahtMessage.objects.filter(room=chatroom)
        serializer = ChatMessageSerializer(messages, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)
        
    def post(self, request, room_id):
        chatroom = get_object_or_404(ChatRoom, id=room_id) 
        user_data = request.data 
        serializer = ChatMessageSerializer(data = user_data)
        serializer.is_valid(raise_exception=True)
        serializer.save(room = chatroom, sender = request.user)
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    
