from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import action

from .longRunningMethod import long_running_method

from .taskHandler import TaskHandler, TaskProgress

class bgTaskViewSet(viewsets.ViewSet):
	# Create your views here.
	@action(methods=['GET'],  detail=False, name='Start the task to background' )
	def start_long_running_task( self, request ):

		input = request.GET[ 'input' ]

		task_id = TaskHandler().start_task( long_running_method, [ input ] )

		return JsonResponse({'task_id':task_id})

	@action(methods=['GET'],  detail=False, name='Get Task Progress' )
	def get_task_progress( self, request ):

		task_id = request.GET[ 'task_id' ]

		task_progress : TaskProgress = TaskHandler.get_task_progress( task_id )

		return JsonResponse( vars(task_progress) )





