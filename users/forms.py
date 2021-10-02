from django import forms
from allauth.account.forms import SignupForm

class SignupForm(SignupForm):
    name = forms.CharField(label="이름")
    phnum = forms.CharField(label="휴대폰 번호")

    def save(self, request):
        user = super(SignupForm, self).save(request)
        user.profile.name = self.cleaned_data["name"]
        user.profile.phnum = self.cleaned_data["phnum"]
        user.save()
        return user