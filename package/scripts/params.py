#!/usr/bin/env python
"""
Elasticsearch Params configurations
"""

from resource_management import *
import os

# server configurations
config = Script.get_config()



kibana_user = config['configurations']['kibana-env']['kibana_user']
kibana_group = config['configurations']['kibana-env']['kibana_group']
work_dir = config['configurations']['kibana-env']['work_dir']
kibana_tar_url = config['configurations']['kibana-env']['kibana_tar_url']


server_port = config['configurations']['kibana-site']['server.port']
server_host = config['configurations']['kibana-site']['server.host']
kibana_index = config['configurations']['kibana-site']['kibana.index']
kibana_pid_dir = config['configurations']['kibana-site']['pid.file']
logging_dest = config['configurations']['kibana-site']['logging.dest']
elasticsearch_url = config['configurations']['kibana-site']['elasticsearch.url']
kibana_conf = format("{work_dir}/kibana-5.2.0-linux-x86_64/config/kibana.yml")

hostname = config['hostname']
java_home = config['hostLevelParams']['java_home']

service_packagedir = os.path.realpath(__file__).split('/scripts')[0]

kibana_server_host = ""
kibana_server_hosts = config['clusterHostInfo']['kibana_master_hosts']
if kibana_server_hosts is not None and len(kibana_server_hosts) > 0:
    kibana_host = kibana_server_hosts[0]

















