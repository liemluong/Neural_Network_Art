from django import forms
from .models import *

PATTERN_CHOICES = [
    ('cartoon', 'cartoon'),
    ('checkered','checkered'),
    ('cheetah', 'cheetah'),
    ('dots','dots'),
    ('floral','floral'),
    ('leaves', 'leaves'),
    ('solid','solid'),
    ('stripes','stripes'),
    ('zigzag','zigzag')
]

ITEM_CHOICES = [
    ('shirt','shirt'),
    ('pants','pants'),
    ('sweater','sweater'),
    ('dress','dress'),
    ('coat','coat'),
    ('sandals','sandals'),
    ('shoes','shoes'),
    ('boots','boots'),
    ('bag', 'bag')

]

FILE_TYPE_CHOICES = [
    ('PNG', 'PNG'),
    ('JPG', 'JPG')
]

CONTENT = [
    ('pattern', 'pattern'),
    ('item', 'item'),
]

# Download form
# Takes file type, content, width, height
class DownloadForm(forms.Form):
    file_type = forms.ChoiceField(choices = FILE_TYPE_CHOICES, widget=forms.Select(attrs={'class': "form-control"}))
    content = forms.ChoiceField(choices = CONTENT, widget=forms.Select(attrs={'class': "form-control"}))
    width = forms.IntegerField(min_value=1, widget=forms.NumberInput(attrs={'class': "form-control", "placeholder": "Width"}))
    height = forms.IntegerField(min_value=1, widget=forms.NumberInput(attrs={'class': "form-control", "placeholder": "Height"}))

# Pattern generation form
# Takes pattern, item, uploaded image, and whether or not to use the uploaded image
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
