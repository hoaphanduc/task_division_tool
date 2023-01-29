from rest_framework import serializers
from AddtaskApp.models import tasks, users

class AddtaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=tasks
        fields=('title','start_date','end_date','status','numberofrequest')

class AssigntaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=tasks
        fields=('id','teamPic')
    
class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model=tasks
        fields=('id', 'title','teamPic')

class PicsSerializer(serializers.ModelSerializer):
    class Meta:
        model=users
        fields=('id', 'account', 'name', 'role', 'team', 'request')