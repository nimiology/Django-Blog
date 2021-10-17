from django import forms

from StaticPages.models import Message


class MessageForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name', 'class': 'col-6',
                                                         'value': ''}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'col-6',
                                                           'value': ''}))
    text = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Message', 'class': 'col-12',
                                                        'row': '8', 'cols': '30',
                                                        'value': ''}))

    class Meta:
        model = Message
        fields = ['name', 'email', 'text']
