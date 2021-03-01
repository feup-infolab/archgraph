# we will use openjdk 8 with alpine as it is a very small linux distro
FROM adoptopenjdk/openjdk14:jdk-14.0.2_12
 
# copy the packaged jar file into our docker image
COPY ./jarfile/backend.jar /archgraph.jar
 
#EXPOSE 3030
# set the startup command to execute the jar
CMD ["java", "-jar", "/archgraph.jar"]

