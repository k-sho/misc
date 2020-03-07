FROM registry.redhat.io/rhel8/llvm-toolset

USER root
RUN subscription-manager register --username user --password pass --autosubscribe
RUN yum install -y redhat-lsb
