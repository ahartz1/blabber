from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Status(models.Model):

    class Meta:
        verbose_name_plural = 'statuses'
    # Note parentheses after; instances of classes
    # id is automatic
    text = models.CharField(max_length=141)
    posted_at = models.DateTimeField()
    user = models.ForeignKey(User)
    # this is how the relations are made within db

    def favorite_count(self):
        return self.favorite_set.count()

    def __str__(self):
        return '@{}: {}'.format(self.user, self.text)


class Favorite(models.Model):
    user = models.ForeignKey(User)
    status = models.ForeignKey(Status)

    def __str__(self):
        return '{} <3 {}'.format(self.user, self.status)

def load_fake_data():
    '''Create some fake users and statuses'''

    # It is encouraged to import only where needed!
    from faker import Faker
    import random

    fake = Faker()

    # Need to clear existing data!
    Favorite.objects.all().delete()
    Status.objects.all().delete()
    User.objects.exclude(username='admin').delete()

    users = []
    for _ in range(50):
        new_user = User(username=fake.user_name(),
                        email=fake.email(),
                        password=fake.password())
        new_user.save()
        users.append(new_user)

    statuses = []
    for _ in range(1000):
        new_status = Status(user=random.choice(users),
                            posted_at=fake.date_time_this_year(),
                            text=fake.text(max_nb_chars=141))
        new_status.save()
        statuses.append(new_status)

    for _ in range(4000):
        favorite = Favorite(user=random.choice(users),
                              status=random.choice(statuses))
        favorite.save()
