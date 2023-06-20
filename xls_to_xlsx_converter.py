import subprocess
import glob

# path to the target directory
target_directory = '/test'

# generate the paths to all .xls file
xls_files = glob.glob(target_directory + '/*.xls')

# iterate through all paths
for xls_file in xls_files:
    # replace the .xls file with the .xlsx file
    output = subprocess.check_output(f'libreoffice --convert-to xlsx --outdir "{target_directory}" "{xls_file}" && rm "{xls_file}"', shell=True)