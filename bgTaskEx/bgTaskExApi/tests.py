import re
import time
from django.test import SimpleTestCase

# Create your tests here.

class MyTests(SimpleTestCase):

	def test_long_running_task(self):

		input = 'aaaaaa'
		print( f'{ input= }' )

		task_id = self.__start_task( input )
		print( f'{ task_id= }' )

		while True:

			time.sleep( 1 )
			result_dict = self.__get_task_progress_response( task_id )

			if result_dict[ 'status' ] == "SUCCESS":
				self.print_output(result_dict)
				break

			self.print_progress_message(result_dict)

	def print_output(self, result_dict):
		status = result_dict[ 'status' ]
		output = result_dict[ "output" ]
		print( f'{status=}, { output= }' )

	def print_progress_message(self, result_dict):
		status = result_dict[ 'status' ]
		progress_message = result_dict[ 'progress_message' ]
		print( f'{ status= },{ progress_message= }' )

	def __start_task( self, input ):
		res = self.client.get( f'/bgTaskExAPI/start_long_running_task/?input={ input }' )
		self.assertEqual( res.status_code, 200 )

		task_id = res.json()[ 'task_id' ]
		UUID_V1_PATTERN = re.compile( '[a-f0-9]{8}-[a-f0-9]{4}-1[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}$', re.IGNORECASE)
		self.assertEqual( UUID_V1_PATTERN.match( task_id ) is not None, True )

		return task_id

	def __get_task_progress_response( self, task_id : str ):
		res = self.client.get( f'/bgTaskExAPI/get_task_progress/?task_id={ task_id }' )
		self.assertEqual( res.status_code, 200 )

		return res.json()
