from django.forms import ModelForm
from .models import Room, CustomUser
from django.contrib.auth.forms import UserCreationForm


class RoomForm(ModelForm):
    
    class Meta:
        model = Room
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self.fields['password1'].help_text=''
        self.fields['password2'].help_text=''
        self.fields['username'].help_text=''

    class Meta:
        model = CustomUser
        fields = ['username','email', 'password1', 'password2']
