#!/usr/bin/env python

from resource_management import *


class ServiceCheck(Script):
    def service_check(self, env):
        import params
        env.set_params(params)

        Execute(format("curl -s -o /dev/null -w '%{{http_code}}' http://{kibana_host}:{server_port} | grep 200"),
                tries=3,
                try_sleep=10,
                logoutput=True
                )

if __name__ == "__main__":
    ServiceCheck().execute()
