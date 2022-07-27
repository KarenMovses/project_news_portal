from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

        for field in ['username', 'password1', 'password2']:
            self.fields[field].help_text = None
            if self.fields[field].label == "Username":
                   self.fields[field].label = "Մուտքանուն"
            if self.fields[field].label == "Password":
                self.fields[field].label = "Ծածկագիր"
            if self.fields[field].label == "Password confirmation":
                self.fields[field].label = "Ծածկագրի հաստատում"            
