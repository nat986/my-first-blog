from django.shortcuts import render
from django.utils import timezone
from .models import Feedback
# Create your views here.

def feedback_list(request):
    feedbacks = Feedback.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'feedback/feedback_list.html', {'feedbacks':feedbacks})