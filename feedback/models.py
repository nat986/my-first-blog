from django.db import models
from django.utils import timezone
# Create your models here.
class Feedback(models.Model):
    now = timezone.now()  
    SESSION1 = 'S1'
    SESSION2 = 'S2'
    SESSION3 = 'S3'
    SESSION4 = 'S4'
    RAMP = 'RP'
    CURRENT_SESSION_CHOICES = (
        (SESSION1, 'Session 1'),
        (SESSION2, 'Session 2'),
        (SESSION3, 'Session 3'),
        (SESSION4, 'Session 4'),
        (RAMP, 'Ramp'),
    )
    author = models.ForeignKey('auth.User')
    mentor_name = models.CharField(max_length=200)
    current_session = models.CharField(max_length=2,
                                      choices=CURRENT_SESSION_CHOICES,
                                      default=SESSION1,
                                      blank=False)
    text = models.TextField()
    notes = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    isOutstanding = models.BooleanField(default=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.mentor_name
    def checked(self):
        self.isOutstanding = False
        self.save()
  