#!/usr/bin/python
import logging
import sys

from run_app import app as application

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, "./")

application.secret_key = "Add your secret key"
