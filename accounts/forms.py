from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

User_Model = get_user_model()


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User_Model
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for i in ["first_name", "last_name", "username", "email","password1","password2",]:
            if i == "username":
                placeholder = "Enter Your Username"
                typ = "text"
            elif i == "first_name":
                placeholder = "Enter Your First Name"
                typ = "text"
            elif i == "last_name":
                placeholder = "Enter Your Last Name"
                typ = "text"
            elif i == "email":
                placeholder = "Enter Your Email"
                typ = "email"
            elif i == "password1" or i=="password2":
                placeholder = "Enter Your Password"
                typ = "password"
           
            self.fields[i].widget.attrs.update(
                {
                    "type": typ,
                    "required class": "w-full px-4 py-2.5 text-sm bg-slate-50 border border-slate-300 rounded-xl focus:ring-2 focus:ring-indigo-500 outline-none",
                    "placeholder": placeholder,
                }
            )

        self.fields["password1"].widget.attrs.update(
            {
                "type": "password",
                "required class": "w-full px-4 py-2.5 text-sm bg-slate-50 border border-slate-300 rounded-xl focus:ring-2 focus:ring-indigo-500 outline-none",
                "placeholder": "Enter your Password",
            }
        )


class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].widget.attrs.update(
            {
                "type": "text",
                "required class": "w-full px-4 py-2.5 text-sm bg-slate-50 border border-slate-300 rounded-xl focus:ring-2 focus:ring-indigo-500 outline-none",
                "placeholder": "Enter your username",
            }
        )

        self.fields["password"].widget.attrs.update(
            {
                "type": "password",
                "required class": "w-full px-4 py-2.5 text-sm bg-slate-50 border border-slate-300 rounded-xl focus:ring-2 focus:ring-indigo-500 outline-none",
                "placeholder": "Enter your Password",
            }
        )
