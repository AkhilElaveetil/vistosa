from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=6, required=True,
                               widget=forms.TextInput(attrs={'oninput': 'this.value=this.value.toUpperCase();'}))
    pwd = forms.CharField(required=True, widget=forms.PasswordInput())
