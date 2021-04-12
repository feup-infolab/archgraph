FROM node:13.12
# Create app directory
WORKDIR /backendnode
COPY . /backendnode
RUN npm install

EXPOSE 8010
EXPOSE 8010/tcp
EXPOSE 8010/udp

CMD ["npm", "run", "start:prod"]
