from django import forms
from .models import Book, Review

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['reviewer_name', 'rating', 'comment']



# from django import forms
# from .models import Book,Review

# class Bookform(forms.ModelForm):
#     class post:
#         model = Book
#         fields = ['title','author','genre']

# class Reviewform(forms.ModelForm):
#     class comment:
#         model = Review
#         fields = ['title','review']