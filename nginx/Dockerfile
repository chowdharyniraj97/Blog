FROM nginx:alpine

RUN apk update && apk add bash

COPY ./nginx/nginx.conf /etc/nginx/nginx.conf

EXPOSE 80 

ENTRYPOINT ["nginx"]
CMD ["-g", "daemon off;"]