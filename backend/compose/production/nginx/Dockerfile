FROM node:alpine as BUILD_IMAGE

WORKDIR /app
# Dont name root folder=frontend
COPY ./front/package.json ./
# install dependencies
RUN npm install
COPY ./front/. .
# build
RUN npm run build
# remove dev dependencies
RUN npm prune --production

FROM nginx:1.23.1

COPY --from=BUILD_IMAGE /app/.next /var/www/front/.next
COPY ./compose/production/nginx/nginx.conf /etc/nginx
