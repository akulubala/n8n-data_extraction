## build local for mac
change SITE_NAME and VERSION to your site name and version
>    args:
>        - SITE_NAME=${SITE_NAME}
>        - VERSION=${VERSION}
>    image: ghcr.io/geekpii/${SITE_NAME}_caddy:${VERSION}

```bash
docker compose -f docker-compose.build-caddy.yml build
docker tag ghcr.io/geekpii/sunnynex-dev_caddy:1.0.2 ghcr.io/geekpii/sunnynex-dev_caddy:latest
docker push ghcr.io/geekpii/sunnynex-dev_caddy:1.0.2
docker push ghcr.io/geekpii/sunnynex-dev_caddy:latest
```