# coding=utf-8
from resource_management import *
from resource_management.core import shell
from resource_management.core.resources.system import Execute, File
from resource_management.libraries.functions import format
from resource_management.libraries.functions.check_process_status import check_process_status
import kibana_service


class Kibana(Script):
    def install(self, env):
        import params
        env.set_params(params)
        Execute(format(
            "sh {service_packagedir}/files/downfiles.sh {kibana_tar_url} {work_dir} {kibana_user}"),
            logoutput=True
            )

    def configure(self, env):
        import params
        import kibana_manager
        env.set_params(params)
        kibana_manager.conf()


    def stop(self, env):
        import params
        import status_params
        env.set_params(params)
        cmd = format("lsof -i :{server_port}|grep -v 'PID' ") + "| awk 'NR==1 {print $2}'"
        code, output = shell.call(cmd)
        if output:
            Execute("kill -9 " + output + " >/dev/null 2>&1", logoutput=True)

        File(status_params.kibana_pid_file,
             action="delete"
            )

    def start(self, env):
        import params
        import kibana_service
        env.set_params(params)
        self.configure(env)
        start_cmd = format("{work_dir}/kibana-5.2.0-linux-x86_64/bin/kibana &")
        Execute(start_cmd,
                logoutput=True,
                environment={
                    'JAVA_HOME': params.java_home,
                    'PATH': '$PATH:$JAVA_HOME/bin'
                }
                )
        import time
        time.sleep(20)

        cmd = format("lsof -i:{server_port}|grep -v 'PID'")+ "| awk 'NR==1 {print $2}'"
        code, output = shell.call(cmd)

        kibana_service.kibana_service("config", output)

    def status(self, env):
        import status_params
        env.set_params(status_params)
        check_process_status(status_params.kibana_pid_file)


if __name__ == "__main__":
    Kibana().execute()
