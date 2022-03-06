from django import forms

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
    ('JPG', 'JPG'),
    ('SVG', 'SVG'),
]

RESOLUTION_CHOICES = [
    (1080, '1080p'),
    (720, '720p'),
]

class PatternGeneratorForm(forms.Form):
    pattern = forms.ChoiceField(choices = PATTERN_CHOICES, widget=forms.RadioSelect)
    item = forms.ChoiceField(choices = ITEM_CHOICES, widget=forms.RadioSelect)

class DownloadForm(forms.Form):
    file_type = forms.ChoiceField(choices = FILE_TYPE_CHOICES, widget=forms.Select(attrs={'class': "form-control"}))
    resolution = forms.ChoiceField(choices = RESOLUTION_CHOICES, widget=forms.Select(attrs={'class': "form-control"}))
    width = forms.IntegerField(min_value=1, widget=forms.NumberInput(attrs={'class': "form-control", "placeholder": "250px"}))
    height = forms.IntegerField(min_value=1, widget=forms.NumberInput(attrs={'class': "form-control", "placeholder": "250px"}))