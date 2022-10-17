from .models import Project, Client
from workers.models import Worker
from rest_framework import serializers


class NameListingField(serializers.RelatedField):
    def to_representation(self, value):
        return '%s ,%s' % (value.worker.firstName, value.worker.lastName)


class LeaderField(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    def get_name(self, obj):
        name = obj.firstName + " " + obj.lastName
        return name

    class Meta:
        model = Worker
        fields = ['id', 'name']

    def to_internal_value(self, data):
        if(isinstance(data, int)):
            if(Worker.objects.get(id=data) != None):
                return Worker.objects.get(id=data)
            else:
                raise serializers.ValidationError("This object does not exist")
        else:
            raise ValueError("Id has to be an int")


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"

    def to_internal_value(self, data):
        if(isinstance(data, int)):
            if(Client.objects.get(id=data) != None):
                return Client.objects.get(id=data)
            else:
                raise serializers.ValidationError("This object does not exist")
        else:
            raise ValueError("Id has to be an int")


class ProjectSerializer(serializers.ModelSerializer):
    client = ClientSerializer()
    members = NameListingField(read_only=True, source='JT_project', many=True)
    leader = LeaderField()

    class Meta:
        model = Project
        fields = ['id', 'shortcut', 'fullName',
                  'client', 'projectNum', 'status', 'members', 'leader']

class ProjectShortSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ['id', 'shortcut']

