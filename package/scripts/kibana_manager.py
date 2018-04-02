#!/use/bin/env python
# coding = utf-8

from resource_management import *
from resource_management.core.resources.system import File

def conf():
    import params

    File(params.kibana_conf,
         owner=params.kibana_user,
         group=params.kibana_group,
         content=Template("kibana.yml.j2")
         )


    # File(format("{pid_dir}/es.pid"),
    #      owner=params.elastic_user,
    #      group=params.elastic_group
    #      )
