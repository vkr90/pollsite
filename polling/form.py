from django import forms

class PollForm(forms.Form):
	text = forms.CharField(widget=forms.Textarea(attrs={'rows': 1,'cols': 85}), max_length=160)
	country = forms.CharField(widget=forms.HiddenInput())

class SearchForm(forms.Form):
	query = forms.CharField(label="Enter Query Search ",widget=forms.TextInput(attrs={'size':32,'class':'form-control'}))
	