from workers.serializers import *
from workers.models import *
from projects.models import *
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q
from django.db.models import Prefetch
import datetime
from teams.serializers import *
from teams.models import *

def excluding_keys(dict, keys):
    return {x: dict[x] for x in dict if x not in keys}

class WorkerViewSet(viewsets.ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
    permission_classes = [permissions.AllowAny]


class WorkerList(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):

        data = request.data
        worker_data = excluding_keys(data, 'team')
        worker_serializer = WorkerSerializer(data = worker_data)
        if worker_serializer.is_valid():
            worker_serializer.save()

            try:
                created_worker = Worker.objects.get(id = worker_serializer.data['id'])
                worker_team = Team.objects.get(id = data['team'])
                new_membership = TeamMembership(worker = created_worker, team = worker_team)
                new_membership.save()
            except:
                return Response(
                    "Something went wrong",
                    status=status.HTTP_400_BAD_REQUEST)
            
            return Response({
					'worker_data': worker_serializer.data,
					'team': data['team']
				})

        else:
            return Response(worker_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WorkerDetail(APIView):
    permission_classes = [permissions.AllowAny]

    def put(self, request, pk):
        editing_data = excluding_keys(request.data, 'team')
        team_id = request.data['team']

        editing_worker = Worker.objects.get(id = pk)
        worker_serializer = WorkerSerializer(editing_worker, editing_data)
        if worker_serializer.is_valid():
            worker_serializer.save()
            try:
                editing_membership = TeamMembership.objects.filter(worker = pk)[0]
                membership_serializer = TeamMembershipSerializer(editing_membership, {
                    'worker': pk, 'team': team_id})
                if membership_serializer.is_valid():
                    membership_serializer.save()
                    return Response({
                        'worker_data': worker_serializer.data,
                        'team_data': membership_serializer.data
                    })
                else:
                    return Response(membership_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                    
            
            except TeamMembership.DoesNotExist:
                return Response(f"Membership from worker {pk} not exist", status=status.HTTP_404_NOT_FOUND)

        else:
            return Response(worker_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WeekViewSet(viewsets.ModelViewSet):
    queryset = Week.objects.all()
    serializer_class = WeekSerializer
    permission_classes = [permissions.AllowAny]


class JobTimeViewSet(viewsets.ModelViewSet):
    queryset = JobTime.objects.all()
    serializer_class = JobTimeSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        data = request.data
        many = isinstance(data, list)
        serializer = self.get_serializer(data=data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers
        )

MONTH_LIST = [
    'Styczeń',
    'Luty',
    'Marzec',
    'Kwiecień',
    'Maj',
    'Czerwiec',
    'Lipiec',
    'Sierpień',
    'Wrzesień',
    'Październik',
    'Listopad',
    'Grudzień']

class JobTimeAvailabilityDetail(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, pk):
        week_id = pk

        try:
            Week.objects.get(id = week_id)

            response_data = []
            workers = Worker.objects.filter(role = 'W')
            for worker in workers:
                worker_id = worker.id
                job_time = JobTime.objects.filter(
                    Q(worker = worker_id) & Q(week = week_id))

                if len(job_time) > 0:
                    availability = job_time[0].availability
                    worker_team = TeamMembership.objects.filter(worker = 5)[0].team

                    response_data.append({
                        'id': worker.id,
                        'name': f"{worker.firstName} {worker.lastName}",
                        'time': availability,
                        'team': {
                            'id': worker_team.id,
                            'name': worker_team.shortcut
                        }
                    })

            return Response(response_data)

        except Week.DoesNotExist:
            return Response(f"Week {week_id} not in db", status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        full_data = request.data["data"]
        week_id = request.data["week_id"]

        response_data = []

        for single_data in full_data:
            worker_id = single_data["id"]
            time = single_data["time"]

            job_list = JobTime.objects.filter(Q(worker = worker_id) & Q(week = week_id))
            for single_job in job_list:
                data_to_put = {
                    "worker": single_job.worker.id,
                    "project": single_job.project.id,
                    "week": single_job.week.id,
                    "availability": time
                }
                editing_jobtime = JobTime.objects.get(id = single_job.id)
                jobtime_serializer = JobTimeSerializer(editing_jobtime, data_to_put)
                if jobtime_serializer.is_valid():
                    jobtime_serializer.save()
                    response_data.append(jobtime_serializer.data)
                else:
                    return Response(jobtime_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({'data': response_data})

class WorkerProjectsDetail(APIView):
    permission_classes = [permissions.AllowAny]

    def put(self, request, pk):
        full_data = request.data["data"]
        week_id = request.data["week_id"]

        response_data = []

        for single_data in full_data:
            worker_id = single_data["worker_id"]
            projects = single_data["projects"]

            for project in projects:
                try:
                    job_time = JobTime.objects.get(
                        Q(worker = worker_id) & Q(week = week_id) & Q(project = project['id']))
                    editing_jobtime = JobTime.objects.get(id = job_time.id)
                    job_time = {
                        'id': job_time.id,
                        'worker': worker_id,
                        'project': project['id'],
                        'workPart': project['time'],
                    }
                    jobtime_serializer = JobTimeSerializer(editing_jobtime, job_time)
                    if jobtime_serializer.is_valid():
                        jobtime_serializer.save()
                        response_data.append(jobtime_serializer.data)
                    else:
                        return Response(jobtime_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

                except JobTime.DoesNotExist:
                    new_job_time = JobTime(
                        worker = Worker.objects.get(id = worker_id),
                        project = Project.objects.get(id = project['id']),
                        week = Week.objects.get(id = week_id),
                        workPart = project['time'])
                    new_job_time.save()
                    response_data.append({
                        'id': new_job_time.id,
                        'worker': worker_id,
                        'project': project['id'],
                        'workPart': project['time'],
                    })

        return Response({'data': response_data})

class WeekList(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, pk):
        weeks = Week.objects.filter(dateEnd__year=pk)
        new_weeks = []
        new_end = datetime.date(1, 1, 1)
        if len(weeks) == 0:
            new_end = datetime.date(pk, 1, 1)
            while new_end.weekday() != 6:
                new_end += datetime.timedelta(days = 1)
        else:
            last_week = weeks[len(weeks) - 1]
            new_end = last_week.dateEnd + datetime.timedelta(days = 7)

        while new_end.year != pk + 1:
            new_start = new_end - datetime.timedelta(days = 6)
            week_name = 'T' + str(new_end.isocalendar().week)
            new_weeks.append({
                'weekName': week_name,
                'dateStart': new_start,
                'dateEnd': new_end,
                'hours': 40
            })
            new_end += datetime.timedelta(days = 7)
        
        if len(new_weeks) > 0:
            serializer = WeekSerializer(data = new_weeks, many = True)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        result = Week.objects.filter(
            (Q(dateStart__year = pk) & ~Q(dateEnd__month = 12)) |
            (Q(dateEnd__year = pk) & ~Q(dateEnd__month = 1)))
        serializer = WeekYearSerializer(result, many=True)

        pre_final = [{'month': i, 'weeks': []} for i in MONTH_LIST]
        for record in serializer.data:
            for i in range(1, 13):
                if i in record['months']:
                    pre_final[i - 1]['weeks'].append(excluding_keys(record, 'months'))

        final = []
        for month in pre_final:
            if len(month['weeks']) != 0:
                final.append(month)

        return Response(final)


class WorkerAvailabilityViewSet(viewsets.ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerAvailabilitySerializer
    permission_classes = [permissions.AllowAny]


class WeekYearViewSet(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, pk):
        result = Week.objects.filter(
            Q(dateStart__year=pk) | Q(dateEnd__year=pk))

        serializer = WeekYearSerializer(result, many=True)

        return Response(serializer.data)

class PlanningViewSet(viewsets.ModelViewSet):
    serializer_class = PlanningSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = Worker.objects.filter(role='W').prefetch_related(Prefetch(
            'JT_worker', queryset=JobTime.objects.filter(week=self.kwargs.get('week_id')), to_attr='filtered_jobtimes'))

        return queryset

