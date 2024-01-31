from django import forms

class ProductForm(forms.Form):
    nama = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    deskripsi = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    harga = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))