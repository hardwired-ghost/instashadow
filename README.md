# instashadow

Instagram OSINT lookup tool built with instagrapi for fast profile reconnaissance by username.

## install

```bash
git clone https://github.com/hardwired-ghost/instashadow.git
cd instashadow
python3 -m venv .venv
source .venv/bin/activate
pip install -U instagrapi python-dotenv
```

## setup

Copy the example env file and fill in your sock puppet credentials:

```bash
cp .env.example .env
```

```env
IG_USER=your_instagram_email
IG_PASS=your_instagram_password
```

`.env` and `ig_session.json` are gitignored, credentials and session tokens never touch git.

## usage

```bash
python3 instashadow.py <@instagram_username>
```

## note

instagrapi recommends reusing sessions via `.dump_settings()` / `.load_settings()` rather than fresh logins each time — stable session reuse makes Instagram trust the device more. Treat `ig_session.json` like a secret: it contains cookies, device UUIDs, and auth tokens.
