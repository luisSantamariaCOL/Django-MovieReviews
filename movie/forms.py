from django.forms import ModelForm, Textarea
from .models import Review

class ReviewForm(ModelForm): # inherit from ModelForm
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)

        # add bootstrap classes to the form
        self.fields['text'].widget.attrs.update({'class': 'form-control'})
        self.fields['watchAgain'].widget.attrs.update({'class': 'form-check-input'})

        # date does not appear because is auto-populated, and user and movie are already provided. 

    # specify the model and fields to use
    class Meta:
        model = Review
        fields = ['text', 'watchAgain']
        labels = {
            'watchAgain': ('Watch Again?')
        }
        widgets = {
            'text': Textarea(attrs={'rows':4}),
        }