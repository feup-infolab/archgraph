#!/bin/bash
npm install
npm run start
echo "Failed to start my_second_process:"


FROM node:13.12
# Create app directory
WORKDIR /frontend
COPY . /frontend
RUN npm install

EXPOSE 4200
EXPOSE 4200/tcp
EXPOSE 4200/udp

CMD ["npm", "start"]
FROM node:13.12
# Create app directory
COPY ./backendnode /frontend/backendnode
RUN npm install

EXPOSE 8010
EXPOSE 8010/tcp
EXPOSE 8010/udp
COPY ./script.sh /
RUN chmod a+x script.sh
CMD ./script.sh

#CMD ["npm", "run", "start:prod"]





#
# Build stage
#
FROM maven:3.6.0-jdk-11-slim AS build
WORKDIR /backend
COPY src /backend/src
COPY pom.xml /backend
RUN mvn -f /backend/pom.xml clean package
# we will use openjdk 8 with alpine as it is a very small linux distro
FROM adoptopenjdk/openjdk14:jdk-14.0.2_12
# copy the packaged jar file into our docker image
#COPY ./build_java_project.sh /backend/build_java_project.sh
#RUN chmod +x ./backend/build_java_project.sh
#RUN ./backend/build_java_project.sh
COPY ./target/back-end.jar /archgraph.jar

EXPOSE 8080
EXPOSE 8080/tcp
EXPOSE 8080/udp
# set the startup command to execute the jar
CMD ["java", "-jar",  "-Dspring.profiles.active=prod", "/archgraph.jar", "production"]

#remover cache docker builder prune
