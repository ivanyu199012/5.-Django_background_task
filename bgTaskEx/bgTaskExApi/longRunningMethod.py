
from datetime import datetime
import time
from .taskHandler import Status


def long_running_method( input : str, task_progress ):

	task_progress.set( Status.STARTED, progress_message="The process has been started" )

	for i in range( 20 ):
		time.sleep( 0.5 )
		task_progress.set( Status.RUNNING, progress_message=f"{ 5 * i + 1 }% has been processed" )

	output = f"[{ datetime.now() }] input= { input }, value from Django"
	task_progress.set( Status.SUCCESS, output=output )