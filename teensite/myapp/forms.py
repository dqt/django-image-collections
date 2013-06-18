from django import forms
from django.forms import ModelForm
from teensite.myapp.models import Blog, Category


class ArticleModelAdminForm(forms.ModelForm):
    body = forms.CharField(widget = forms.Textarea)

    class Meta:
        model = Blog



class SearchForm(forms.Form):
    WHERE = (
        ("memes", ("/r/memes")),
        ("funny", ("/r/funny")),
        ("funnypics", ("/r/funnypics")),
        ("fitmeme", ("/r/fitmeme")),
        ("geekporn", ("/r/geekporn")),
        ("fashionporn", ("/r/fashionporn")),
        ("celebs", ("/r/celebs")),
    )
    url = forms.ChoiceField(label='Where To Scrape', choices=WHERE)
    maximum = forms.IntegerField(max_value=20, label='Number of Pics to Scrape')

class FunForm(forms.Form):
    page = forms.IntegerField(max_value=500, label='Page Number To Scrape')

class BlogForm(ModelForm):
    class Meta:
        model = Blog
        category = forms.ModelChoiceField(queryset=Category.objects.all(),required=True,label='Category')
        fields = ['title', 'slug', 'body', 'category']