FROM ubuntu:18.04 as dependencies_ready
ENV SOURCE_BRANCH "master"
ENV NEO4J_ADDRESS "bolt://neo4j:password@neo4j:7687"

RUN apt-get update -qq
RUN apt-get install -y -qq git curl wget python2.7 python-pip

FROM dependencies_ready
COPY . /archgraph
WORKDIR /archgraph
RUN git checkout "$SOURCE_BRANCH"
RUN ./conf/install.sh
ENTRYPOINT [ "./conf/run.sh" ]