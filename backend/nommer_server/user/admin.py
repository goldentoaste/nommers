from django.contrib import admin
from django.forms.models import ModelForm
from .models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.admin import UserAdmin
import django.forms as forms
from django.contrib.auth.models import Group
class UserCreationForm(ModelForm):

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput)

    is_admin = forms.BooleanField(label="Admin", required=False)

    class Meta:
        model = User
        fields = [
            "userName",
            "ppiUrl", 
        ]

    def clean_password2(self):

        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if (not (password1 and password2)) or (password1 != password2):
            raise forms.ValidationError("Passwords don't match")

        return password2

    def save(self, commit=True):

        user = super().save(commit = False)
        user.set_password(self.cleaned_data(['password1']))
        
        if commit:
            user.save()
        return user


class UserChangeForm(ModelForm):

    password = ReadOnlyPasswordHashField()
    class Meta:
        model = User
        fields = [
            "userName",
            "password",
            "ppiUrl",
            "is_admin",
        ]

class CustomUserAdmin(UserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('userName', 'id', 'is_admin')
    list_filter = ("is_admin",)


    fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "userName",
                "password",
                "ppiUrl",
                "is_admin"
            )
        }),
    ) # type: ignore

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "userName",
                "password1",
                "password2",
                "ppiUrl",
                "is_admin"
            )
        }),
    ) # type: ignore


    search_fields = ("userName",)
    ordering = ("userName",)
    filter_horizontal = ()


admin.site.register(User, CustomUserAdmin)
admin.site.unregister(Group)