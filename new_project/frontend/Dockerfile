FROM node:13.12
# Create app directory
WORKDIR /frontend
COPY . /frontend
RUN npm install

EXPOSE 4200
EXPOSE 4200/tcp
EXPOSE 4200/udp

CMD ["npm", "start"]
