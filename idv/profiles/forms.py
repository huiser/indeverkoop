from django import forms
from django.core.urlresolvers import reverse
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (
    Layout,
    Div,
    Submit,
    HTML,
    Button,
    Row,
    Field,
)
from crispy_forms.bootstrap import (
    AppendedText,
    PrependedText,
    FormActions,
    StrictButton
)
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import IdvUser

class CustomUserCreationForm(UserCreationForm):
    """
    A form that creates a user, with no privileges, from the given email and
    password.
    """

    def __init__(self, *args, **kargs):
        super(IdvUserCreationForm, self).__init__(*args, **kargs)
        del self.fields['username']

    class Meta:
        model = IdvUser
        fields = (
            "email",
            "voorletters",
            "tussenvoegsel"
        }


class IdvUserChangeForm(UserChangeForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    def __init__(self, *args, **kargs):
        super(IdvUserChangeForm, self).__init__(*args, **kargs)
        del self.fields['username']

    class Meta:
        model = IdvUser

#class LoginForm(forms.Form):
#    email = forms.EmailField(
#        label='Email adres',
#        max_length=50,
#        required=True,
#    )
#    password = forms.CharField(
#        label='Wachtwoord',
#        max_length=50,
#        required=True,
#        widget=forms.PasswordInput(),
#    )
#    remember = forms.BooleanField(
#        label='Onthou mij',
#        required=False,
#    )
#
#    def __init__(self, *args, **kwargs):
#        super(LoginForm, self).__init__(*args, **kwargs)
#        self.helper = FormHelper()
#        self.helper.form_class = 'form-horizontal'
#        self.helper.form_id = 'login-form'
#        self.helper.label_class = 'col-lg-2'
#        self.helper.field_class = 'col-lg-4'
#        self.helper.form_action = reverse('home')
#        self.helper.layout = Layout(
#            'email',
#            'password',
#            'remember',
#            #StrictButton('Sign in', css_class='btn-default'),
#            FormActions(
#                Div(css_class='col-lg-2'),
#                Submit('submit', 'Inloggen', css_class='btn-primary col-lg-2'),
#                #Button('cancel', 'Afbreken', onclick='history.go(-1);'),
#            ),
#        )
