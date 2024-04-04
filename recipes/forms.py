from django import forms
from .models import Recipe



class RecipiesForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name',
                  'description',
                  'steps',
                  'cooking_time',
                  'image',
                  'author',
                  ]


class UpdateRecipiesForm(forms.Form):
    id = forms.IntegerField(min_value=1, required=False)
    name = forms.CharField(required=False)
    description = forms.CharField(required=False, widget=forms.Textarea)
    steps = forms.CharField(required=False, widget=forms.Textarea)
    cooking_time = forms.TimeField(required=False)
    image = forms.ImageField(required=False)
    author = forms.CharField(required=False)
    category = forms.IntegerField(min_value=1, required=False)


class UpdateUserForm(forms.Form):
    id = forms.IntegerField(min_value=1, required=True)
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)
