FROM maven:3.6.0-jdk-11-slim AS build
WORKDIR /backend
COPY . .
#FROM adoptopenjdk/openjdk14:jdk-14.0.2_12

EXPOSE 8080
EXPOSE 8080/tcp
EXPOSE 8080/udp

RUN chmod a+x run_script.sh
CMD ./run_script.sh
# set the startup command to execute the jar
#CMD ["java", "-jar",  "-Dspring.profiles.active=prod", "./target/back-end.jar", "production"]

