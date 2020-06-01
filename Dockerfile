FROM ubuntu:18.04 as os_dependencies_ready

RUN apt-get update -qq
RUN apt-get install -y -qq git curl wget build-essential

FROM os_dependencies_ready as libraries_and_modules_installed
COPY ./conf /archgraph_setup/conf
COPY ./requirements.txt /archgraph_setup/requirements.txt
COPY ./frontend/package.json /archgraph_setup/frontend/package.json
WORKDIR /archgraph_setup
RUN ./conf/install.sh

FROM libraries_installed as archgraph_installed
COPY . /archgraph
COPY /archgraph_setup/frontend/node_modules /archgraph/frontend

FROM archgraph_installed as cleanup_complete
RUN rm -rf /archgraph_setup

ENTRYPOINT [ "./conf/run.sh" ]