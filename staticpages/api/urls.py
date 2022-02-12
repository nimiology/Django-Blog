from django.urls import path

from staticpages.api.views import MessageAPI, MessagesAPI
app_name = 'api'

urlpatterns = [
    path('message/', MessageAPI.as_view(), name='create_message'),
    path('message/<int:pk>', MessageAPI.as_view(), name='message'),
    path('message/all/', MessagesAPI.as_view(), name='messages')
]