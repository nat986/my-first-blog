from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Feedback
# Create your views here.

def feedback_list(request):
    feedbacks = Feedback.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'feedback/feedback_list.html', {'feedbacks':feedbacks})

def feedback_detail(request, pk):
    feedback = get_object_or_404(Feedback, pk=pk)
    return render(request, 'feedback/feedback_detail.html', {'feedback': feedback})