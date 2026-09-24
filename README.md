# purrgame.com

Static site for Purr: Cozy Cat Home — landing page, privacy policy and support, in English (`/`) and Spanish (`/es/`). No build step: plain HTML and one stylesheet, published with **GitHub Pages** from the `main` branch (root). Pushing to `main` deploys.

## Hosting

- GitHub → repo Settings → Pages: Source "Deploy from a branch", branch `main`, folder `/ (root)`; Custom domain `purrgame.com`; "Enforce HTTPS" once the certificate is issued.
- `CNAME` in the repo holds the custom domain; `.nojekyll` keeps Pages from processing the files.
- DNS (Cloudflare, DNS only / grey cloud): `purrgame.com` A records → `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`; `www` CNAME → `busyninja.github.io`.

## Edit

- `index.html`, `privacy.html`, `support.html` and their `es/` twins. Keep both languages in step.
- `assets/`: icon (from the game's iOS app icon), splash and store screenshots (`tools/store_shot.tscn` in the game repo, downscaled to 900 px high).
- Contact address in the pages: `hello@purrgame.com`.
