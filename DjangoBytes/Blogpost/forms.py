from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from.models import comment


class NewUserForm(UserCreationForm):
    username = forms.CharField(
        label="username",
      
        max_length=15,
        help_text="feel free to write a simple username with at least 3 characters",
    )

    email = forms.EmailField(required=True)
    country = forms.CharField(max_length=100)
   

    """def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already taken.")
        return username """

    class Meta:
        model = User
        fields = ("username", "email", "country",  "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
class search_form(forms.Form):
    search1=forms.CharField(max_length=100, label="search", required=False)
   


class commentForm(forms.ModelForm):

    class Meta:
        model=comment
        fields=('name', 'email', 'body')
 