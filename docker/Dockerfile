FROM centos:7

LABEL description="A simple Test Runner"
LABEL maintainer="Ashish"
LABEL version="0.0.1"

ENV PYTHONUNBUFFERED=1
ENV USER=docker
ENV UID=1000
ENV GID=1000

RUN yum -y update && \
    yum -y install yum-utils && \
    yum -y groupinstall development && \
    yum -y install https://centos7.iuscommunity.org/ius-release.rpm

# Install Oracle instant client

RUN yum -y install wget && \
    wget http://yum.oracle.com/public-yum-ol7.repo -P /etc/yum.repos.d/ && \
    wget http://yum.oracle.com/RPM-GPG-KEY-oracle-ol7 && \
    rpm --import RPM-GPG-KEY-oracle-ol7 && \
    yum-config-manager --enable ol7_oracle_instantclient && \
    yum -y install oracle-instantclient18.3-basic.x86_64 \
    oracle-instantclient18.3-jdbc.x86_64 \
    oracle-instantclient18.3-sqlplus.x86_64 && \
    sh -c "echo /usr/lib/oracle/18.3/client64/lib/ > /etc/ld.so.conf.d/oracle-instantclient.conf" && \
    ldconfig

ENV LD_LIBRARY_PATH=/usr/lib/oracle/18.3/client64/lib/:$LD_LIBRARY_PATH
ENV ORACLE_HOME=/usr/lib/oracle/18.3/client64

RUN yum -y install python36u python36u-pip && \
    yum clean all

# Create the non-root user
RUN set -Eeuxo pipefail \
    && groupadd --gid ${GID} ${USER} \
    && adduser \
    --gid ${USER} \
    --home-dir /home/${USER} \
    --create-home \
    --uid ${UID} \
    ${USER}

USER docker

ENV PATH /home/${USER}/.local/bin:${PATH}

COPY requirements.txt .

RUN pip3.6 install --user --no-cache-dir -r requirements.txt

# Application will be bind mounted at runtime for this image to be useful
VOLUME [ "/opt/dbconnect" ]
WORKDIR /opt/dbconnect

COPY run_tests.sh /run_tests.sh
CMD ["/run_tests.sh"]