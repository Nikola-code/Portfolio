from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from teams.serializers import *
from teams.models import *
from workers.models import *

class TeamViewSet(viewsets.ModelViewSet):
	queryset = Team.objects.all()
	serializer_class = TeamSerializer
	permission_classes = [permissions.AllowAny]

class TeamListViewSet(viewsets.ModelViewSet):
	queryset = Team.objects.all()
	serializer_class = TeamListSerializer
	permission_classes = [permissions.AllowAny]

class TeamMembersViewSet(viewsets.ModelViewSet):
	queryset = Team.objects.all()
	serializer_class = TeamMembersSerializer
	permission_classes = [permissions.AllowAny]

class TeamWorkerViewSet(viewsets.ModelViewSet):
	queryset = Worker.objects.filter(role='W').order_by('-lastName')
	serializer_class = TeamWorkerSerializer
	permission_classes = [permissions.AllowAny]

class TeamLeaderViewSet(viewsets.ModelViewSet):
	queryset = Worker.objects.filter(role='L').order_by('-lastName')
	serializer_class = TeamWorkerSerializer
	permission_classes = [permissions.AllowAny]

class TeamMembershipViewSet(viewsets.ModelViewSet):
	queryset = TeamMembership.objects.all()
	serializer_class = TeamMembershipSerializer
	permission_classes = [permissions.AllowAny]

	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data = request.data, many = isinstance(request.data, list))
		serializer.is_valid(raise_exception = True)
		self.perform_create(serializer)
		headers = self.get_success_headers(serializer.data)
		return Response(serializer.data, status = status.HTTP_201_CREATED, headers = headers)


def excluding_keys(dict, keys):
	return {x: dict[x] for x in dict if x not in keys}

class TeamList(APIView):

	permission_classes = [permissions.AllowAny]

	def post(self, request):

		team_data = excluding_keys(request.data, 'members')
		team_members = request.data['members']

		team_serializer = TeamSerializer(data = team_data)
		if team_serializer.is_valid():
			team_serializer.save()
			team_obj = Team.objects.filter(shortcut = team_data['shortcut'])
			new_team = team_obj[len(team_obj) - 1]

			members = []
			old_members = []

			for member in team_members:
				records = TeamMembership.objects.filter(worker = member)
				for i in range(0, len(records)):
					old_members.append(records[i])

				members.append({
					'worker': member,
					'team': new_team.id
				})
			
			team_mem_serializer = TeamMembershipSerializer(data = members, many = True)
			if team_mem_serializer.is_valid():
				for old in old_members:
					old.delete()

				team_mem_serializer.save()
				return Response({
					'team_data': team_serializer.data,
					'membership_data': team_mem_serializer.data
				})

			else:
				team_obj.delete()
				return Response(team_mem_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

		else:
			return Response(team_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TeamDetail(APIView):

	permission_classes = [permissions.AllowAny]

	def put(self, request, pk):

		team_data = excluding_keys(request.data, 'members')
		new_members = request.data['members']

		team = Team.objects.get(id = pk)
		team_serializer = TeamSerializer(team, data = team_data)

		if team_serializer.is_valid():
			team_serializer.save()

			editing_team = Team.objects.get(id = team_data['id'])
			old_members = TeamMembership.objects.filter(team = team_data['id'])
			membership_to_delete = []

			members = []

			for member in new_members:
				records = TeamMembership.objects.filter(worker = member)

				members.append({
					'id': records[0].id,
					'worker': member,
					'team': editing_team.id
				})

				for i in range(1, len(records)):
					membership_to_delete.append(records[i])


			for old in old_members:
				old.worker.status = False
				old.worker.save()

			for member in members:
				worker = Worker.objects.get(id = member['worker'])
				worker.status = True
				worker.save()

			for to_delete in membership_to_delete:
				to_delete.delete()

			response_data = []

			for member in members:
				editing_member = TeamMembership.objects.get(id = member['id'])
				team_mem_serializer = TeamMembershipSerializer(editing_member, member)
				if team_mem_serializer.is_valid():
					response_data.append(team_mem_serializer.data)
					team_mem_serializer.save()
				else:
					return Response(team_mem_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

			return Response({
				'team_data': team_serializer.data,
				'membership_data': response_data.data
			})

		else:
			return Response(team_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

