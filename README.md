# purrgame.com

Static site for Purr: Cozy Cat Home — landing page, privacy policy and support, in English (`/`) and Spanish (`/es/`). No build step: plain HTML and one stylesheet.

## Deploy

The site is served by the same Caddy that fronts `api.purrgame.com` on the game's Hetzner host (see `server/prod/Caddyfile` in the game repo). `deploy.sh` copies the files to `/opt/purr/site` over SSH:

```sh
./deploy.sh            # rsync to root@2.29.45.95:/opt/purr/site
```

DNS for `purrgame.com` and `www` is at Cloudflare (proxied) and points at the host; Caddy obtains the certificate itself. Cloudflare's SSL mode must be **Full** (not Flexible).

## Edit

- `index.html`, `privacy.html`, `support.html` and their `es/` twins. Keep both languages in step.
- `assets/`: icon (from the game's iOS app icon), splash and store screenshots (`tools/store_shot.tscn` in the game repo, downscaled to 900 px high).
- Contact address in the pages: `hello@purrgame.com`.
