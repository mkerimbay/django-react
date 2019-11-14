FROM node:13

WORKDIR '/app'

# Install dependencies
COPY package.json /app/
COPY yarn.lock /app/
RUN npm install

# Add rest of the client code
COPY . /app/

EXPOSE 3000

CMD npm start