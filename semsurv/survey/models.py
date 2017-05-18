from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Survey(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Grouping(models.Model):
    order = models.IntegerField()
    name = models.CharField(max_length=50, blank=True)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    def __str__(self):
        return "{}:{}-{}".format(self.survey.title[:10], self.order, self.name)

class OptionGroup(models.Model):
    name = models.CharField(max_length=50, blank=True)
    randomize = models.BooleanField()
    def __str__(self):
        return self.name

class Option(models.Model):
    text = models.CharField(max_length=200)
    str_value = models.CharField(max_length=200, blank=True)
    int_value = models.IntegerField(null=True, blank=True)
    float_value = models.FloatField(null=True, blank=True)
    bool_value = models.BooleanField()
    order = models.IntegerField(blank=True)
    grouping = models.ForeignKey(OptionGroup, on_delete=models.CASCADE)
    def __str__(self):
        return self.text

QUESTION_TYPES = (('combo', 'Combo Box'),
                  ('check', 'Check Boxes'),
                  ('radio', 'Radio Buttons'),
                  ('text', 'Text Field'),
                  ('int', 'Integer Field'),
                  ('scale', 'Scale'),
                  ('nscale', 'Named Scale'),
                  ('unit', 'Unit Int Field'),
                  ('bool', 'Yes or No'))

class Question(models.Model):
    order = models.IntegerField()
    grouping = models.ForeignKey(Grouping, on_delete=models.CASCADE)
    text = models.TextField()
    q_type = models.CharField(max_length=10, choices=QUESTION_TYPES)
    options = models.ForeignKey(OptionGroup, blank=True, null=True,
                                on_delete=models.CASCADE)
    depends_string = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return "{}.{}".format(self.order, self.text)

class Respondent(models.Model):
    email = models.EmailField(blank=True)
    name = models.TextField(max_length=200, blank=True)

class Response(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    respondent = models.ForeignKey(Respondent, on_delete=models.CASCADE)
    str_value = models.CharField(max_length=200, blank=True)
    int_value = models.IntegerField(null=True, blank=True)
    float_value = models.FloatField(null=True, blank=True)
    bool_value = models.BooleanField()
    option = models.ForeignKey(Option, blank=True, null=True,
                               on_delete=models.CASCADE)

class Triple(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    predicate = models.CharField(max_length=255)
    obj = models.CharField(max_length=255)
    choice = models.ForeignKey(Option, on_delete=models.CASCADE,
                               null=True, blank=True)
    value = models.BooleanField()
    def __str__(self):
        return "{} - {} {} {}".format(self.question, self.subject,
                                      self.predicate, self.obj)
