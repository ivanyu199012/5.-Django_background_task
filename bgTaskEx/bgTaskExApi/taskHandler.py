
from enum import Enum
from django.core.cache import cache
import threading
from typing import Union
from uuid import uuid1

class TaskHandler:

	def start_task(self, method, args):

		taskProgress = TaskProgress()
		t = threading.Thread( target=method, args=[ *args, taskProgress ] )
		t.setDaemon(True)
		t.start()

		return taskProgress.get_task_id()

	@staticmethod
	def get_task_progress( task_id : str ):
		return cache.get( task_id )

class TaskProgress:

	task_id = str

	# default constructor
	def __init__(self):
		self.task_id = str( uuid1() )
		cache.set( self.task_id, self, 3600 )

	def set( self,
		status : Enum,
		progress_message : Union[ str, None ] = None,
		output : Union[ str, None ] = None,
		error_message : Union[ str, None ] = None, ) -> object:

		self.status = status.value
		self.progress_message = progress_message
		self.output = output
		self.error_message = error_message

		cache.set( self.task_id, self, 3600 )
		print( f'{status=}, {progress_message=}, {output=}' )

	def get_task_id( self ):
		return self.task_id

class Status(Enum):
	STARTED = 'STARTED'
	RUNNING = 'RUNNING'
	SUCCESS = 'SUCCESS'
	ERROR = 'ERROR'