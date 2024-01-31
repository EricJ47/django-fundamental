from django import forms
from .models import Article, Category


class CategoryForm(forms.Form):
   nama_category = forms.CharField(max_length=100)
   
# forms.py



class ArticleForm(forms.ModelForm):
    tanggal = forms.DateTimeInput(attrs={'type': 'datetime-local'})
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Pilih Kategori", widget=forms.Select(attrs={'class':'form-control'}))
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = Article
        fields = ['category', 'title', 'deskripsi', 'tanggal', 'image']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['deskripsi'].widget = forms.Textarea(attrs={'id': 'summernote'})
