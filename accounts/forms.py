from django import forms

class LoginForm(forms.Form):
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control form-control-lg form-control-solid",
                "autocomplete": "off",
                "id": "floatingInput",
                "placeholder": "email"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "off",
                "class": "form-control form-control-lg form-control-solid",
                "id": "floatingPassword",
                "placeholder": "password"
            }
        ))