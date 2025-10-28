# Synology Container Manager Setup Guide

This guide explains how to set up Larasanic on Synology NAS using Container Manager.

## Initial Setup

### Step 1: Start in Setup Mode

In Synology Container Manager, add this environment variable:
```
SETUP_MODE=true
```

Or via command line:
```bash
SETUP_MODE=true docker-compose up -d
```

This keeps the container running without starting the app, allowing you to run the setup wizard.

### Step 2: Run Setup Wizard

Access the container terminal in Synology Container Manager and run:
```bash
python artisan app:setup
```

Or via command line:
```bash
docker exec -it larasanic_app python artisan app:setup
```

Follow the interactive setup wizard to configure:
- Database connection
- JWT keys generation
- CSRF secret
- Application settings

### Step 3: Switch to Normal Mode

After setup is complete:

1. In Synology Container Manager, remove or change the environment variable:
   ```
   SETUP_MODE=false
   ```
   Or simply delete the `SETUP_MODE` variable

2. Restart the container

The app will now start normally.

## Alternative: Manual Configuration

If you can't access the container terminal, you can manually configure:

### 1. Create `.env` file from template
```bash
cp .env.template .env
```

### 2. Generate secrets
```bash
# Generate CSRF secret (64 character hex string)
python -c "import secrets; print(secrets.token_hex(32))"

# Generate JWT keys
mkdir -p storage/keys
# Then manually create RSA key pair or use the setup wizard
```

### 3. Edit `.env` file with your values

### 4. Start container normally
```bash
docker-compose up -d
```

## Checking Container Status

View logs:
```bash
docker logs -f larasanic_app
```

Access container shell:
```bash
docker exec -it larasanic_app /bin/bash
```

## Environment Variables

### Required for first run:
- `SETUP_MODE=true` - Keeps container running for setup

### Optional:
- `REDIS_PASSWORD` - Custom Redis password (default: `changeme`)
- `APP_ENV` - Environment (default: `development`)
- `APP_DEBUG` - Debug mode (default: `true`)

## Troubleshooting

### Container keeps restarting
- Set `SETUP_MODE=true` to keep it running
- Check logs: `docker logs larasanic_app`
- Verify Redis is running: `docker logs larasanic_redis`

### Can't access setup wizard
- Ensure `SETUP_MODE=true` is set
- Container must be running (not restarting)
- Check container status in Synology Container Manager

### Configuration validation failed
- Run `python artisan app:setup` in container
- Or manually create `.env` and generate secrets
