from django import forms
from django.contrib.auth import get_user_model

# for getting data from queryset so that we can query from User Model
User = get_user_model()

# all the Django forms must inherit forms.Form
class ContactForm(forms.Form):
    # using fullname, email, content in request.POST.get()
    fullname = forms.CharField (
                    widget=forms.TextInput(
                        attrs = {
                            "class": "form-control",
                            "placeholder": "You Full Name",
                        }
                    )
                )
    email =   forms.EmailField (
                    widget=forms.TextInput(
                        attrs = {
                            "class": "form-control",
                            "placeholder": "Your Email",
                        }
                    )
                )
    content = forms.CharField (
                    widget=forms.Textarea(
                        attrs = {
                            "class": "form-control",
                            "placeholder": "Your Content",
                        }
                    )
                )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("Email has to be gmail.com")
        return email

class LoginForm(forms.Form):
    username = forms.CharField (
                    widget=forms.TextInput (
                        attrs= {
                            "class": "form-control",
                            "placeholder": "give username"
                        }
                    )
                )
    password = forms.CharField (
                    widget=forms.PasswordInput (
                        attrs= {
                            "class": "form-control",
                            "placeholder": "give password"
                        }
                    )
                )

class RegisterForm(forms.Form):
    firstname = forms.CharField (
                    widget=forms.TextInput (
                        attrs= {
                            "class": "form-control",
                            "placeholder": "your firstname"
                        }
                    )
                )
    lastname =  forms.CharField (
                    widget=forms.TextInput (
                        attrs= {
                            "class": "form-control",
                            "placeholder": "your lastname"
                        }
                    )
                )
    username =  forms.CharField (
                    widget=forms.TextInput (
                        attrs= {
                            "class": "form-control",
                            "placeholder": "your username"
                        }
                    )
                )
    password =  forms.CharField (
                    widget=forms.PasswordInput (
                        attrs= {
                            "class": "form-control",
                            "placeholder": "your password"
                        }
                    )
                )
    password_confirm = forms.CharField (
                    label= 'Confirm Password',
                    widget=forms.PasswordInput (
                        attrs= {
                            "class": "form-control",
                            "placeholder": "password again"
                        }
                    )
                )
    email =     forms.EmailField (
                    widget=forms.TextInput (
                        attrs= {
                            "class": "form-control",
                            "placeholder": "your email"
                        }
                    )
                )
    phone_number = forms.IntegerField (
                    widget=forms.NumberInput (
                        attrs= {
                            "class": "form-control",
                            "placeholder": "phone number"
                        }
                    )
                )
    
    # no duplicate username allowed
    def clean_username(self):
        username= self.cleaned_data.get('username')
        # check with filtering into queryset that if this exists
        queryset = User.objects.filter(username= username)
        if queryset.exists():
            raise forms.ValidationError("Username is already taken.")
        return username

    # no duplicate email allowed
    def clean_email(self):
        email = self.cleaned_data.get('email')
        # check with filtering into queryset that if this exists
        queryset = User.objects.filter(email= email)
        if queryset.exists():
            raise forms.ValidationError("Email is already taken.")
        return email

    # using clean() method for some validation
    def clean_password(self):
        # self.cleaned_data.get() is a method used for getting required data
        data = self.cleaned_data
        #print(data)
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        
        # passwords must match
        '''
        if password != password_confirm:
            raise forms.ValidationError("passwords don't matched")
        '''
        return password