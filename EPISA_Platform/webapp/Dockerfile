FROM node:13.12
# Create app directory
WORKDIR /webapp
COPY . .
RUN npm install
RUN npm install --prefix backendnode

EXPOSE 4200

RUN chmod a+x script.sh

CMD ./script.sh

