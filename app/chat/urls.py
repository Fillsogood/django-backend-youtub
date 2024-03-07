from django.urls import path
from .views import ChatRoomList,ChatMessageList,show_html

urlpatterns = [
    path('room/', ChatRoomList.as_view(), name='room_list'),
    path('<int:room_id>/messages/', ChatMessageList.as_view(), name='room_Messagelist'),
    path('chatting',show_html, name="chatting")
]