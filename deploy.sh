#!/bin/sh
# Copy the site to the production host; Caddy serves /opt/purr/site as purrgame.com.
set -e
cd "$(dirname "$0")"
HOST="${1:-root@2.29.45.95}"
ssh "$HOST" 'mkdir -p /opt/purr/site'
rsync -az --delete --exclude '.git' --exclude 'deploy.sh' --exclude 'README.md' ./ "$HOST:/opt/purr/site/"
echo "deployed to $HOST:/opt/purr/site"
curl -s -o /dev/null -w 'purrgame.com -> %{http_code}\n' https://purrgame.com/ || true
