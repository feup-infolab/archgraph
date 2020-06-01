FROM ubuntu:18.04 as dependencies_ready

RUN apt-get update -qq
RUN apt-get install -y -qq git curl wget build-essential
FROM dependencies_ready
COPY . /archgraph
WORKDIR /archgraph
RUN ./conf/install.sh
ENTRYPOINT [ "./conf/run.sh" ]