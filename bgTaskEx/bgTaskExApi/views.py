from datetime import datetime
import time
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

class bgTaskViewSet(viewsets.ViewSet):
    # Create your views here.
    @action(methods=['GET'],  detail=False, name='Put the task to background' )
    def put_task_to_background( self, request ):

        input = request.GET[ 'input' ]

        return Response( status=status.HTTP_200_OK,
                data=f"[{ datetime.now() }] input= { input }, value from Django" )

def long_running_method( input ):

	for i in range( 100 ):
		time.sleep( 1 )

	return f"[{ datetime.now() }] input= { input }, value from Django"