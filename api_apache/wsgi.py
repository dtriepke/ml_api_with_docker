#! /usr/bin/python
import sys
sys.path.insert(0, '/var/www/flask_api_predict')
sys.path.insert(0, '/opt/conda/lib/python3.7/site-packages')
sys.path.insert(0, '/opt/conda/bin/')

import os
os.environ['PYTHONPATH'] = '/opt/conda/bin/python'

from flask_api_predict import app as application