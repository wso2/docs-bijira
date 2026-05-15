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
COPY nginx.conf /etc/nginx/conf.d/default.conf

RUN apk upgrade --no-cache libcrypto3 libssl3

RUN adduser -u 10014 -D -H -G nginx appuser \
    && chown -R 10014:nginx /usr/share/nginx/html \
    && chown -R 10014:nginx /var/log/nginx \
    && chown -R 10014:nginx /var/cache/nginx \
    && chown -R 10014:nginx /etc/nginx/conf.d \
    && sed -i 's|/var/run/nginx.pid|/tmp/nginx.pid|g' /etc/nginx/nginx.conf

USER 10014

EXPOSE 8080

CMD ["nginx", "-g", "daemon off;"]
