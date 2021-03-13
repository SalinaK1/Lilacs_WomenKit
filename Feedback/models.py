from django.db import models

# Create your models here.
class Feedback(models.Model):
    feedback = models.CharField(max_length=3000)
    sent_on = models.DateField(auto_now_add=True)
    class Meta:
        verbose_name = "Feedback"
 