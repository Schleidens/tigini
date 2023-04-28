from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class createUserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name']