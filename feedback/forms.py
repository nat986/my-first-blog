from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        fields = ('mentor_name', 'text', 'notes','current_session',)
        
