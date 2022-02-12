from rest_framework.generics import RetrieveAPIView, DestroyAPIView, CreateAPIView, ListAPIView

from staticpages.api.permissions import IsSuperUser, CreateOnly
from staticpages.api.serializers import MessageSerializer
from staticpages.models import Message


class MessageAPI(CreateAPIView, RetrieveAPIView, DestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [CreateOnly | IsSuperUser]


class MessagesAPI(ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsSuperUser]
    filterset_fields = {
        "name": ['exact', 'contains'],
        "email": ['exact', 'contains'],
        "text": ['exact', 'contains'],
        "created": ['exact'],
    }
    ordering_fields = '__all__'
