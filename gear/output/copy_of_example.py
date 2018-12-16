#!/usr/bin/env python

import os, json
from shutil import copyfile
import gearlib

# initialize gear library and load config.json into gear.data
gear = gearlib.Gear()

# you gear logic starts here
gear.log('This is an example python script for a gear.')
gear.log('Modify as desired, or set the manifest "command" key to something else entirely.')

# print the working directory and config.json contents (gear.data)
gear.log_all()


gear.log('reference gear.data[\'inputs\'] to find your gear inputs.')
gear.log('reference gear.data[\'config\'] to find your gear configuration options.')

gear.log('input \"dicom\" is a ' + gear.data['inputs']['dicom']['base'])
gear.log('you can find your file at ' + gear.data['inputs']['dicom']['location']['path'])

# as an example a file processing we rename and copy the input file to ./output for upload to Flywheel
copyfile(gear.data['inputs']['dicom']['location']['path'], './output/copy_of_' + gear.data['inputs']['dicom']['location']['name'])


# Check if the flywheel SDK is installed
try:
	import flywheel

	# Make some simple calls to the API
	fw = flywheel.Flywheel(gear.data['inputs']['api-key']['key'])
	user = fw.get_current_user()
	config = fw.get_config()

	gear.log('You are logged in as ' + user.firstname + ' ' + user.lastname + ' at ' + config.site.api_url[:-4])

except ImportError:
	gear.log('\nFlywheel SDK is not installed, try "fw gear modify" and then "pip install flywheel-sdk".\n')



#place output files in the gear output_folder
gear.log('Make sure to move any result files you want to preserve to the output folder')
gear.log('you can write files to output/ ...')
gear.log('you can write metadata to output/ ...')

gear.result_metadata(gear.data['inputs']['dicom']['hierarchy'], {"test":"my val"})

gear.log_output()

gear.log('Gear completed successfully!')
exit(0)


