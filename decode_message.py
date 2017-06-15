"""
Take message in coded_message and decode it.
"""

import os
import shutil

cwd = os.getcwd()
output_folder = ''.join((cwd, '/', 'decoded_message'))
source_folder = ''.join((cwd, '/', 'coded_message', '/'))

# Clear old decoded messages
if os.path.exists(output_folder):
    shutil.rmtree(output_folder)
os.makedirs(output_folder)

# Get list of files in coded_message directory and decode them.
files = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]
for file in files:
    tmp = file.split('_')  # Splits filename into 2 parts.
    tmp2 = tmp[1].split('.')
    filename = tmp2[0] + '_' + tmp[0] + '.' + tmp[1].split('.')[1]
    source_file = source_folder + '/' + file
    destination_file = output_folder + '/' + filename
    shutil.copy2(source_file, destination_file)
