from rest_framework import serializers
from teams.models import *

class MemberListField(serializers.RelatedField):
	def to_representation(self, obj):
		return f"{obj.worker.firstName} {obj.worker.lastName}"

class MemberIdListField(serializers.RelatedField):
	def to_representation(self, obj):
		return {
			"id": obj.worker.id,
			"name": f"{obj.worker.firstName} {obj.worker.lastName}"
		}

class TeamSerializer(serializers.ModelSerializer):
	class Meta:
		model = Team
		fields = '__all__'

class TeamListSerializer(serializers.ModelSerializer):

	leader = serializers.SerializerMethodField()
	members = MemberListField(read_only=True, source='T_team', many=True)

	def get_leader(self, obj):
		return f"{obj.leader.firstName} {obj.leader.lastName}"

	class Meta:
		model = Team
		fields = ['id', 'shortcut', 'fullName', 'leader', 'members']

class TeamMembersSerializer(serializers.ModelSerializer):

	members = MemberIdListField(read_only=True, source='T_team', many=True)

	class Meta:
		model = Team
		fields = ['shortcut', 'members']

class TeamWorkerSerializer(serializers.ModelSerializer):

	name = serializers.SerializerMethodField()

	def get_name(self, obj):
		return f"{obj.lastName} {obj.firstName}"

	class Meta:
		model = Worker
		fields = ['id', 'name']

#TeamMembership
class TeamMembershipSerializer(serializers.ModelSerializer):
	class Meta:
		model = TeamMembership
		fields = '__all__'

