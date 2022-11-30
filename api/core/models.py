from django.db import models

class raizen_gasoline_fraud(models.Model):
    user_id = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)
    outlier_prob = models.FloatField()