from django.db import models


class Members(models.Model):
    real_name = models.CharField(max_length=100)
    tz = models.CharField(max_length=100)

    def __str__(self):
        return self.real_name


class ActivityPeriods(models.Model):
    members = models.ForeignKey(Members, related_name='activity_periods', on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()


class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    activityPeriods = models.ForeignKey('ActivityPeriods', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
