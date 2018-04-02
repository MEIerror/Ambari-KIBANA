## Logstash And Kibana

Ambari service for install and manageing Logstash and Kibana stack on HDP cluster

Note: there show the version of environment.

- Ambari Version: 2.4.1.0-22
- HDP Stack Version: 2.5
- Elasticsearch Version: 5.2.0
- Logstash Version: 5.2.0
- Kibana Version: 5.2.0
- JDK Version: 1.8.0_111

  [下载地址](https://www.elastic.co/downloads/past-releases)
#### There are some problems to be noted here

 * Logstash unable to specify pid path.
 * Kibana's pid file unable :

    - kibana_pid_file = config\['configurations']\['kibana-site']\['kibana_pid_file']

   I'm defining it this way： "/var/run/kibana.pid"
#### Warning:
- If you have modified the "logstash-site", you should make change on the system(example:add a log file path).
-
