FROM caddy:2.8.4-builder AS builder


RUN xcaddy build --with github.com/shift72/caddy-geo-ip

FROM caddy:2.8.4
COPY --from=builder /usr/bin/caddy /usr/bin/caddy

WORKDIR /srv

COPY config/data_extraction.conf /etc/caddy/sites/
COPY config/Caddyfile /etc/caddy/Caddyfile