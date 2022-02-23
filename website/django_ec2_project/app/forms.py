from django import forms

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
    width = forms.IntegerField(min_value=1, widget=forms.NumberInput(attrs={'class': "form-control", "placeholder": "Width"}))
    height = forms.IntegerField(min_value=1, widget=forms.NumberInput(attrs={'class': "form-control", "placeholder": "Height"}))