from django.db import models

class Master(models.Model):
    Email = models.EmailField(max_length=40)
    Password = models.CharField(max_length=12)
    IsActive = models.BooleanField(default=False)

    class Meta:
        db_table = 'master'

    def __str__(self):
        return self.Email

class User(models.Model):
    Master = models.ForeignKey(Master, on_delete=models.CASCADE)
    FullName = models.CharField(max_length=30, default='')
    Mobile = models.CharField(max_length=10, default='')
    Country = models.CharField(max_length=20, default='')
    State = models.CharField(max_length=20, default='')
    Pin = models.CharField(max_length=6, default='')
    Address = models.TextField(max_length=200, default='')

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.FullName

class Note(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Title = models.CharField(max_length=20)
    Content = models.TextField(max_length=500)
    DateCreated = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'note'

    def __str__(self):
        return self.Title