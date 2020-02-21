FROM ubuntu:18.04

RUN apt-get update
RUN apt-get install -y git
RUN apt-get install -y curl
RUN apt-get install -y wget
RUN git clone https://github.com/feup-infolab/archgraph.git /archgraph
WORKDIR /archgraph
RUN ./conf/install.sh
CMD [ "./run.sh" ]