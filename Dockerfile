FROM ubuntu:18.04 as dependencies_ready
ARG PRELOAD_GRAPH
ENV PRELOAD_GRAPH "$PRELOAD_GRAPH"

RUN apt-get update -qq
RUN apt-get install -y -qq git curl wget build-essential
FROM dependencies_ready
COPY . /archgraph
WORKDIR /archgraph
RUN ./conf/install.sh
ENTRYPOINT [ "./conf/run.sh" ]