from django import forms


class MemberForm(forms.Form):
    nama = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    alamat = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    no_telp = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    jenis_kelamin = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    pekerjaan = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))