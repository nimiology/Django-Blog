from django import forms

from staticpages.models import Message


class HomeMessageForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name',
                                                         'value': ''}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Email',
                                                           'value': ''}))
    text = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Message',
                                                        'row': '4',
                                                        'value': ''}))

    class Meta:
        model = Message
        fields = ['name', 'email', 'text']


class ContactMessageForm(HomeMessageForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Message',
                                                        'row': '4',
                                                        'value': '',
                                                        'style': 'width: 100%;'}))
