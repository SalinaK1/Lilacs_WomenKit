from django.forms import ModelForm
from .models import Feedback

# Create the form class.
class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = "__all__"



 