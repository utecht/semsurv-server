from django.shortcuts import render
from rest_framework import viewsets
from survey.serializers import *
from survey.models import *

# Create your views here.
class SurveyViewSet(viewsets.ModelViewSet):
    serializer_class = SurveySerializer
    queryset = Survey.objects.all()

class GroupingViewSet(viewsets.ModelViewSet):
    serializer_class = GroupingSerializer
    queryset = Grouping.objects.all()

class OptionViewSet(viewsets.ModelViewSet):
    serializer_class = OptionSerializer
    queryset = Option.objects.all()

class OptionGroupViewSet(viewsets.ModelViewSet):
    serializer_class = OptionGroupSerializer
    queryset = OptionGroup.objects.all()

class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
