from django.shortcuts import render

# Create your views here.

def feedback_list(request):
    return render(request, 'feedback/feedback_list.html', {})