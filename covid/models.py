from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ManageUser(models.Manager):
    def get_queryset(self):
        return super(ManageUser, self).get_queryset()


class Gender(models.Model):
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.gender


class Result(models.Model):
    result = models.CharField(max_length=10)

    def __str__(self):
        return self.result


class ProfileUser(models.Model):

    # La liaison OneToOne vers le models User

    # add covidtest = models.ForienkeyFiel (autocrete)

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user.is_staff=False

    name = models.CharField(max_length=255, unique=True, null=False)
    surname = models.CharField(max_length=255, verbose_name='surname',
                               null=False, unique=True)
    email = models.EmailField()
    address = models.CharField(max_length=30, verbose_name='Address')
    phone = models.IntegerField(verbose_name='Telephone', serialize=False, auto_created=False)
    gender = models.OneToOneField(Gender, on_delete=models.CASCADE)
    age = models.IntegerField(null=False)
    idtestnumber = models.CharField(max_length=15, unique=True, null=False,
                               primary_key=True, help_text='Enter your id covid test number')
    user_create = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='static/img', default= 'static/img/default.jpg')

    def __str__(self):
        return "Profile de {0}".format(self.user.username)


class TestCovid(models.Model):
    idtestnumber = models.CharField(null=False, max_length=20, unique=True, primary_key=True)
    test_center = models.CharField(max_length=20, null=False)
    locate = models.CharField(max_length=20)
    result_test = models.OneToOneField(Result, on_delete=models.CASCADE)

    def __str__(self):
        return "{0} has done in {1}, {2} and the result is {3}".format(self.idtestnumber,
                                            self.test_center, self.locate, self.result_test)


class Color(models.Model):
    name =  models.CharField(max_length=50)

    def __str__(self):
        return self.name


class OtherUser(models.Model):
    locate = models.CharField(max_length=50)
    latitude = models.DecimalField(max_digits=50, decimal_places=2)
    longitude = models.DecimalField(max_digits=50, decimal_places=2)
    result =  models.CharField(max_length=50)
    color =  models.CharField(max_length=50)

    def __str__(self):
        return '{} {} {}'.format(self.locate, self.latitude, self.longitude)


