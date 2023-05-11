from django import forms

class ResaForm(forms.Form):

    your_Date = forms.DateField(widget=forms.SelectDateWidget(years=['2023']))
    your_time = forms.TimeField(label="Your time")
    your_NbreHeure = forms.DurationField(label="Your time window")
    your_Pin = forms.CharField(label="Your PIN", max_length=100)

    

class Pincheck(forms.Form):
    your_Pin = forms.CharField(label="Your PIN", max_length=100)

