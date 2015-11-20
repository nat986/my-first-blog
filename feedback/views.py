from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Feedback
from .forms import FeedbackForm
# Create your views here.

def feedback_list(request):
    feedbacks = Feedback.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'feedback/feedback_list.html', {'feedbacks':feedbacks})

def feedback_detail(request, pk):
    feedback = get_object_or_404(Feedback, pk=pk)
    return render(request, 'feedback/feedback_detail.html', {'feedback': feedback})

def feedback_new(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.author = request.user
            feedback.published_date = timezone.now()
            feedback.save()
            return redirect('feedback.views.feedback_detail', pk=feedback.pk)
    else:
        form = FeedbackForm()
    return render(request, 'feedback/feedback_edit.html', {'form': form})

def feedback_edit(request, pk):
    feedback = get_object_or_404(Feedback, pk=pk)
    if request.method == "POST":
        form = FeedbackForm(request.POST, instance=feedback)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.author = request.user
            feedback.published_date = timezone.now()
            feedback.save()
            return redirect('feedback.views.feedback_detail', pk=feedback.pk)
    else:
        form = FeedbackForm(instance=feedback)
    return render(request, 'feedback/feedback_edit.html', {'form': form})