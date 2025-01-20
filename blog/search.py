from django import forms

class TagSearchForm(forms.Form):
    tag = forms.CharField(required=False, label="Search by Tag")
