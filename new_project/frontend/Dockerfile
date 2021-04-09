FROM node:13.12
# Create app directory
WORKDIR /frontend
COPY . .
RUN npm install
RUN npm install --prefix backendnode


EXPOSE 4200

RUN pwd

RUN chmod a+x script.sh

CMD ./script.sh

#CMD ["npm", "start"]
