from rest_framework import serializers
from teams.models import *
from .models import JobTime, Week, Worker


class TeamListingField(serializers.RelatedField):
    def to_representation(self, value):
        return {
            "id": value.team.id,
            "name": value.team.shortcut
        }

class NameListingField(serializers.RelatedField):
    def to_representation(self, value):
        return '%s %s' % (value.firstName, value.lastName)


class JobProjectSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super(JobProjectSerializer, self).__init__(*args, **kwargs)
        self.fields['shortcut'].required = False

    id = serializers.CharField(source='project.id')
    shortcut = serializers.CharField(source='project.shortcut')
    time = serializers.FloatField(source='workPart')

    class Meta:
        model = JobTime
        fields = ['id', 'shortcut', 'time']

class WorkerSerializer(serializers.ModelSerializer):
    team = TeamListingField(read_only=True, many=True, source='T_worker')

    class Meta:
        model = Worker
        fields = ['id', 'firstName', 'lastName', 'email',
                  'role', 'status', 'workHours', 'team']

class JobTimeSerializer(serializers.ModelSerializer):

    class Meta:
        model = JobTime
        fields = '__all__'

class WeekSerializer(serializers.ModelSerializer):

    class Meta:
        model = Week
        fields = '__all__'

class WeekYearSerializer(serializers.ModelSerializer):
    months = serializers.SerializerMethodField()

    def get_months(self, obj):
        x = obj.dateStart.month
        y = obj.dateEnd.month

        if x == y or x > y:
            return [x]
        else:
            return [x, y]

    class Meta:
        model = Week
        fields = '__all__'

class WorkerAvailabilitySerializer(serializers.ModelSerializer):
    team = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    availability = serializers.SerializerMethodField()
    week = serializers.SerializerMethodField()

    def get_team(self, obj):
        try:
            team = TeamMembership.objects.get(id=obj.id).team
            return {
                "id": team.id,
                "name": team.shortcut
            }
        #TODO: Remove in future
        except:
            return {
                "id": 0,
                "name": "UDF"
            }

    def get_availability(self,obj):
        try:
            availability = JobTime.objects.filter(worker=obj.id)[0].availability
            return availability            
        except:
            pass

    def get_name(self, obj):
        return f"{obj.firstName} {obj.lastName}"
    
    def get_week(self,obj):
        try:
            weeks = []
            for week in Week.objects.filter():
                weeks.append({'weekName': week.weekName, 'id': week.id})
            return weeks      
        except:
            pass

    class Meta:
        model = Worker
        fields = ['id', 'name', 'week', 'team','availability']

class PlanningSerializer(serializers.ModelSerializer):
    team = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    time = serializers.SerializerMethodField()
    projects = JobProjectSerializer(
        source='filtered_jobtimes', many=True)

    def get_team(self, obj):
        try:
            team = TeamMembership.objects.get(worker=obj.id).team
            return {
                "id": team.id,
                "name": team.shortcut
            }
        except:
            return {
                "id": 0,
                "name": "UDF"
            }

    def get_name(self, obj):
        return f"{obj.firstName} {obj.lastName}"

    def get_time(self, obj):
        return obj.workHours

    class Meta:
        model = Worker
        fields = ['id', 'name', 'time', 'team', 'projects']

