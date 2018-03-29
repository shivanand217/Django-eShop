from django import forms

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
                            "placeholder": "your password"
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

    # using clean() method for some validation
    def clean(self):
        # self.cleaned_data.get() is a method used for getting required data
        data = self.cleaned_data
        #print(data)
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        email = self.cleaned_data.get('email')
        
        # passwords must match
        if password != password_confirm:
            raise forms.ValidationError("passwords don't matched")
        
        return data
        