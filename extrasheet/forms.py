from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import login,authenticate
from django.contrib.auth import get_user_model
from .models import Club_fo,Club_in

class RegisterForm(UserCreationForm):
    pass
    class Meta:
        model = get_user_model()
        fields = ('first_name','last_name','email', 'username','date_of_birth','mobile_number','password1', 'password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email / Username')
#from django.contrib.auth import get_user_model
#from django import forms


class ForumForm (forms.ModelForm) :
    
    class Meta :
        model = Club_fo
        fields=('text',)
        
class InsightForm (forms.ModelForm) :
    
    class Meta :
        model = Club_in
        fields=('text','upload_file',)