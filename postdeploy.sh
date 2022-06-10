python manage.py migrate --noinput

rfbrowser init --skip-browsers; mkdir -p /app/.heroku/python/lib/python3.9/site-packages/Browser/wrapper/node_modules/playwright-core/.local-browsers/chromium-1005/chrome-linux; ln -s /app/.apt/usr/bin/google-chrome /app/.heroku/python/lib/python3.9/site-packages/Browser/wrapper/node_modules/playwright-core/.local-browsers/chromium-1005/chrome-linux/chrome
