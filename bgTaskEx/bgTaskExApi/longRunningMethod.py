
from datetime import datetime
import time
from .taskHandler import Status


def long_running_method( input : str, taskProgress ):

	taskProgress.set( Status.STARTED, progress_message="The process has been started" )

	for i in range( 100 ):
		time.sleep( 1 )
		taskProgress.set( Status.RUNNING, progress_message=f"{ i+1 }% has been processed" )

	output = f"[{ datetime.now() }] input= { input }, value from Django"
	taskProgress.set( Status.SUCCESS, output=output )