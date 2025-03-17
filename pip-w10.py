import pkg_resources
import subprocess
import os
import sys


subprocess.check_call(['pip', 'install', 'openpyxl'])
subprocess.check_call(['pip', 'install', 'PyPDF2'])
subprocess.check_call(['pip', 'install', 'python-docx'])
subprocess.check_call(['pip', 'install', 'Pillow'])