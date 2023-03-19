from django.db import models

# Create your models here.


class ayyaam(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    title = models.CharField(max_length=200)
    details = models.CharField(max_length=1200)
    mydate = models.IntegerField(default=00)
    month = models.CharField(max_length=2)
    month_islamic_title = models.CharField(max_length=22)
    details_page_link = models.CharField(max_length=112)

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        verbose_name_plural = 'Title_Info'


class suggestons(models.Model):
    added_date = models.DateTimeField()
    text = models.CharField(max_length=1200)

    def __str__(self):
        return '{}'.format(self.text)

    class Meta:
        verbose_name_plural = 'Suggestions'


class subscriptions(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    added_date = models.DateTimeField()
    text = models.EmailField(max_length=1200)

    def __str__(self):
        return '{}'.format(self.text)

    class Meta:
        verbose_name_plural = 'Subscriptions'
        

class dateStore(models.Model):
    startDate = models.IntegerField(default=00)
    startMonth = models.IntegerField(default=00)
    startYear = models.IntegerField(default=00)
    IslamicMonth = models.IntegerField(default=00)
    IslamicYear = models.IntegerField(default=00)

    def __str__(self):
        return '{}'.format(self.IslamicMonth)

    class Meta:
        verbose_name_plural = 'IslamicMonth'
