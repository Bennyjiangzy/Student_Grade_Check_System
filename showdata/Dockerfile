FROM node:current-slim
RUN apt update

# Copy source code to /src in container
COPY . /src

# Install app and dependencies into /src in container
RUN cd /src; npm install

EXPOSE 3000

# Run this command (starts the app) when the container starts
CMD cd /src && npm start
