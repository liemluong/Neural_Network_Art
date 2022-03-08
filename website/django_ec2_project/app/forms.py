from django import forms
from .models import *

PATTERN_CHOICES = [
    ('checkered','checkered'), 
    ('dots','dots'),
    ('floral','floral'),
    ('solid','solid'),
    ('stripes','stripes'),
    ('zigzag','zigzag')
]

ITEM_CHOICES = [
    ('top','top'), 
    ('trouser','trouser'),
    ('pullover','pullover'),
    ('dress','dress'),
    ('coat','coat'),
    ('sandal','sandal'),
    ('shirt','shirt'),
    ('sneaker','sneaker'),
    ('bag','bag'),
    ('ankle boot','ankle boot')
]

FILE_TYPE_CHOICES = [
    ('PNG', 'PNG'),
    ('JPG', 'JPG')
]

CONTENT = [
    ('pattern', 'pattern'),
    ('item', 'item'),
]

# class PatternGeneratorForm(forms.Form):
#     pattern = forms.ChoiceField(choices = PATTERN_CHOICES, widget=forms.RadioSelect)
#     item = forms.ChoiceField(choices = ITEM_CHOICES, widget=forms.RadioSelect)
#     use_upload = forms.BooleanField()

class DownloadForm(forms.Form):
    file_type = forms.ChoiceField(choices = FILE_TYPE_CHOICES, widget=forms.Select(attrs={'class': "form-control"}))
    content = forms.ChoiceField(choices = CONTENT, widget=forms.Select(attrs={'class': "form-control"}))
    width = forms.IntegerField(min_value=1, widget=forms.NumberInput(attrs={'class': "form-control", "placeholder": "Width"}))
    height = forms.IntegerField(min_value=1, widget=forms.NumberInput(attrs={'class': "form-control", "placeholder": "Height"}))
    # pattern = forms.ChoiceField(choices = PATTERN_CHOICES)

class PatternGeneratorForm(forms.ModelForm):
    pattern = forms.ChoiceField(choices = PATTERN_CHOICES, widget=forms.RadioSelect)
    item = forms.ChoiceField(choices = ITEM_CHOICES, widget=forms.RadioSelect, required=False)
    use_upload = forms.BooleanField(required=False)
    def __init__(self, *args, **kwargs):
        super(PatternGeneratorForm, self).__init__(*args, **kwargs)
        self.fields['item_image'].required = False
        self.fields['item_image'].label = ""
    class Meta:
        model = Item
        fields = ['item_image']