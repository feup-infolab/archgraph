#
# Build stage
#
FROM maven:3.6.0-jdk-11-slim AS build
WORKDIR /backend
COPY . .
#RUN mvn -f /backend/pom.xml clean package
# we will use openjdk 8 with alpine as it is a very small linux distro
#FROM adoptopenjdk/openjdk14:jdk-14.0.2_12
# copy the packaged jar file into our docker image
RUN chmod a+x script.sh

RUN pwd
CMD ./script.sh
#COPY ./target/back-end.jar /archgraph.jar
EXPOSE 8080
EXPOSE 8080/tcp
EXPOSE 8080/udp
RUN dir
# set the startup command to execute the jar
#CMD ["java", "-jar",  "-Dspring.profiles.active=prod", "./target/back-end.jar", "production"]

#remover cache docker builder prune
