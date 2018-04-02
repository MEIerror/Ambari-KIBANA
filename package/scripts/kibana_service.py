# coding=utf-8
from resource_management import *
from resource_management.core.resources.system import File


def kibana_service(name=None,pid=None):
    import status_params
    if name == "config":
        File(status_params.kibana_pid_file,
             content=pid + "\n"
             )
