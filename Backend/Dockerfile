FROM node:15.4.0

ARG var1=development
ARG var2=mongodb+srv://priebe:ys2pAvp4OxIVJlyX@cluster0.eyermce.mongodb.net/?retryWrites=true&w=majority
ARG var3=sample_mflix
ARG var4=redis://default:5PFZg1X7eLkwz7OjGvMgxty6mG1w1Ky2@redis-19050.c279.us-central1-1.gce.cloud.redislabs.com:19050
ARG var5=3000

ENV NODE_ENV=$var1
ENV MONGO_DB_CONNECTION_STRING=$var2
ENV MONGO_DB_NAME=$var3
ENV REDIS_URI=$var4
ENV PORT=$var5

COPY . /app
WORKDIR /app

EXPOSE 3000

RUN npm install

CMD ["npm", "start"]
