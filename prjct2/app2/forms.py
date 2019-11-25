
from django import forms
from app2.models import Details
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


class RegistrationForm(forms.ModelForm):
    alphabetical = RegexValidator(r'^[a-zA-Z_]*$', 'only alphabetical characters are allowed')
    # numeric = RegexValidator(r'^[0-9]*$', 'only numeric characters are alowed')
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder' :'Enter User name'}),required=True, max_length=50)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder' :'Enter Your name'}),required=True, validators=[alphabetical],max_length=50)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder' :'Enter your last name'}),required=True,validators=[alphabetical],max_length=50)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control','placeholder' :'Enter your email'}),required=True,max_length=50)
    phonenumber = forms.CharField(widget=forms.NumberInput(attrs={'class':'form_control','placeholder' :'Enter your phonenumber'}),required=True,max_length=20)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder' :'Enter password'}),required=True,max_length=10)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder' :'confirm password'}),required=True,max_length=10)


    class Meta:
        model = Details
        fields = ['username','first_name', 'last_name', 'email', 'phonenumber', 'gender','city', 'password', 'password1']

    def clean_email(self):
        email_passed = self.cleaned_data['email']
        if Details.objects.filter(email=email_passed).exists():
            raise forms.ValidationError("email already exists ")
        return email_passed
        # try:
        #     mt = Details.objects.get(email=email_passed)
        # except:
        #     return forms.ValidationError("email is not in correct format")
        # raise forms.ValidationError("email already exists ")
        # return email_passed


    def clean_password1(self):
        pas = self.cleaned_data['password']
        pas1 = self.cleaned_data['password1']
        MIN_LENGTH= 8
        if pas and pas1:
            if pas != pas1:
                raise forms.ValidationError("password doesnot matched")
            else:
                if len(pas) < MIN_LENGTH:
                    raise forms.ValidationError("password atleast %d characters" %MIN_LENGTH)
                if pas.isdigit():
                    raise forms.ValidationError("password should not all digits")
        return pas1

