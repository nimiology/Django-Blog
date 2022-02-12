from rest_framework.serializers import ModelSerializer

from staticpages.models import Message


class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

