#!/usr/bin/env bash
#time: 11/2/17



KIBANA_URL=$1
WORK_DIR=$2  #安装目录
KIBANA_USER=$3
#WORK_DIR=/usr/local/lib/ambari-service
#CLUSTERNAME='es-81'
#NODENAME='adm'
#NETWORKHOST='192.168.1.81'
#HTTPPORT='9200'
if [ ! -d ${WORK_DIR} ]; then
    mkdir -p ${WORK_DIR}
fi

if [ ! -d ${WORK_DIR}/kibana-5.2.0-linux-x86_64 ];then
wget -O ${WORK_DIR}/kibana-5.2.0-linux-x86_64.tar.gz  ${KIBANA_URL}
tar -zxf ${WORK_DIR}/kibana-5.2.0-linux-x86_64.tar.gz -C ${WORK_DIR}
fi

id ${KIBANA_USER} &> /dev/null
if [ $? -ne 0 ]; then
    useradd ${KIBANA_USER}
fi
