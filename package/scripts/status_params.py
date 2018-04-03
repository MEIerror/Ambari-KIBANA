#!/usr/bin/env python

from resource_management import *
from resource_management.libraries.functions import format
from resource_management.libraries.script.script import Script

config = Script.get_config()

# kibana_pid_file = config['configurations']['kibana-site']['pid.file']
# kibana_pid_file = format("{kibana_pid_dir}/kibana.pid")
kibana_pid_file = '/var/run/kibana.pid'
