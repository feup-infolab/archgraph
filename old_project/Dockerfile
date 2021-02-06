FROM ubuntu:18.04 as os_dependencies_ready

RUN apt-get update -qq
RUN apt-get install -y -qq git curl wget build-essential

FROM os_dependencies_ready as backend_dependencies

WORKDIR /archgraph_setup
COPY ./conf /archgraph_setup/conf
COPY ./requirements.txt /archgraph_setup/requirements.txt
COPY ./frontend/package.json /archgraph_setup/frontend/package.json
RUN ./conf/install_backend.sh

FROM backend_dependencies as frontend_dependencies
RUN ./conf/install_frontend.sh

FROM frontend_dependencies as archgraph_installed
COPY . /archgraph
RUN mv /archgraph_setup/frontend/* /archgraph/frontend

FROM archgraph_installed as cleanup_complete
RUN rm -rf /archgraph_setup

WORKDIR /archgraph

ENTRYPOINT [ "./conf/run.sh" ]