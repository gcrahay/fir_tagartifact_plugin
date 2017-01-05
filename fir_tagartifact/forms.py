from django import forms
from fir_tagartifact.models import ValidTag


class TagForm(forms.Form):
    name = forms.ModelChoiceField(queryset=ValidTag.objects.all(), required=True)
    value = forms.CharField(min_length=3, required=True)

    def __init__(self, category, *args, **kwargs):
        self.base_fields['name'].queryset = category.valid_tags.all()
        super(TagForm, self).__init__(*args, **kwargs)
