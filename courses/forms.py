from django import forms
from .models import Category, CourseReview


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'description')
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Add a category name...'}),
        }


class ReviewAdd(forms.ModelForm):
    class Meta:
        model = CourseReview
        fields = ('review_text', 'review_rating')