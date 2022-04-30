import re
import time
from django.test import SimpleTestCase

# Create your tests here.

class MyTests(SimpleTestCase):

	def test_long_running_task(self):

		input = 'aaaaaa'
		print( f'{ input= }' )

		res = self.client.get( f'/bgTaskExAPI/start_long_running_task/?input={ input }' )

		self.assertEqual( res.status_code, 200 )

		task_id = res.json()[ 'task_id' ]
		UUID_V1_PATTERN = re.compile( '[a-f0-9]{8}-[a-f0-9]{4}-1[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}$', re.IGNORECASE)
		self.assertEqual( UUID_V1_PATTERN.match( task_id ) is not None, True )

		status_code, res = self.__get_task_progress_response( task_id )
		self.assertEqual( status_code, 200 )

		status = res.json()[ "status" ]
		self.assertEqual( status == "RUNNING" or status == "STARTED" , True )

		while True:

			time.sleep( 1 )
			status_code, res = self.__get_task_progress_response( task_id )

			self.assertEqual( status_code, 200 )

			result = res.json()
			if result[ 'status' ] == "SUCCESS":
				output = result[ "output" ]
				# check if it is non-empty string
				self.assertEqual( bool( output and output.strip() ), True )
				print( f'{ output= }' )
				break

			progress_message = result[ 'progress_message' ]
			print( f'{ progress_message= }' )

	def __get_task_progress_response( self, task_id : str ):
		res = self.client.get( f'/bgTaskExAPI/get_task_progress/?task_id={ task_id }' )
		return res.status_code, res
