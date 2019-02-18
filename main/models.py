from django.db import models
from django.core.mail import send_mail
# Create your models here.


class Evaluator(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    date = models.DateTimeField(auto_now_add=True)

    def send_invite(self):
        send_mail(
            'Subject here',
            'Here is the message.',
            'from@example.com',
            [self.email],
            fail_silently=False,
        )
        self.save()

    def __str__(self):
        return self.name


class Measure(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text


class Objective(models.Model):
    evaluator = models.ForeignKey(Evaluator, related_name='evaluator', on_delete=models.CASCADE)
    text = models.TextField()
    measure = models.ForeignKey(Measure, on_delete= models.CASCADE, related_name='measure')

    def __str__(self):
        return self.text

