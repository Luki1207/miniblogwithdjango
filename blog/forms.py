from django import forms 
from blog.models import Post, Comment

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('author','category','title','text',)
        

        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'text' : forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'}),
        }

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('name','comment')

        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'comment' : forms.Textarea(attrs={'class':'editable medium-editor-textarea'}),
        }



