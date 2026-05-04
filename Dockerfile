# Stage 1: Build the MkDocs static site
FROM python:3.12 AS builder

WORKDIR /app

COPY en/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir "setuptools<80"

COPY en/ .

RUN mkdocs build

# Stage 2: Serve with Nginx
FROM nginx:1.26-alpine

COPY --from=builder /app/site /usr/share/nginx/html

RUN apk upgrade --no-cache libcrypto3 libssl3

RUN adduser -u 10014 -D -H -G nginx appuser \
    && chown -R 10014:nginx /usr/share/nginx/html \
    && chown -R 10014:nginx /var/log/nginx \
    && chown -R 10014:nginx /var/cache/nginx \
    && chown -R 10014:nginx /etc/nginx/conf.d \
    && touch /run/nginx.pid && chown 10014:nginx /run/nginx.pid \
    && sed -i 's/listen\s*80;/listen 8080;/g' /etc/nginx/conf.d/default.conf \
    && sed -i 's/listen\s*\[::\]:80;/listen [::]:8080;/g' /etc/nginx/conf.d/default.conf

USER 10014

EXPOSE 8080

CMD ["nginx", "-g", "daemon off;"]
