from django import  forms


class RegistrationForm(forms.Form):
    username=forms.CharField(max_length=100,
                             widget=forms.TextInput(attrs={'class': 'form-control',
                                                           'placeholder':'USERNAME'}))
    password = forms.CharField(max_length=100,
                             widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                           'placeholder':'PASSWORD'}))
    email = forms.CharField(max_length=100,
                             widget=forms.EmailInput(attrs={'class': 'form-control',
                                                           'placeholder':'EMAIL'}))
    phone = forms.CharField(max_length=100,
                             widget=forms.NumberInput(attrs={'class': 'form-control',
                                                           'placeholder':'PHONE'}))