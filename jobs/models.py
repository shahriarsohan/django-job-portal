from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    f_name = models.CharField(max_length=10, blank=True, null=True)
    l_name = models.CharField(max_length=10, blank=True, null=True)
    is_company = models.BooleanField(default=False)
    is_intern = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
        ordering = ['-id']

    def __str__(self):
        return self.f_name

    def fullname(srlf):
        fill_name = self.f_name + ' ' + self.l_name
        return fill_name


class Jobs(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    position = models.CharField(max_length=15)
    posted_in = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='media/jobs/%Y/%m/%d/')
    intern_allowed = models.BooleanField(default=False)
    salary = models.IntegerField(blank=True, null=True)
    experience_needed = models.FloatField(blank=True, null=True)
