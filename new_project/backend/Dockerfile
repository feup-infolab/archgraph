# we will use openjdk 8 with alpine as it is a very small linux distro
FROM adoptopenjdk/openjdk14:jdk-14.0.2_12
 
# copy the packaged jar file into our docker image
COPY ./jarfile/back-end.jar /archgraph.jar
 
EXPOSE 8080
EXPOSE 8080/tcp
EXPOSE 8080/udp
# set the startup command to execute the jar
CMD ["java", "-jar", "/archgraph.jar"]

