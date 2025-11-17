# Plugin Artifact Template

This directory contains a template for creating TrueNAS Core 13 plugin artifacts.

## What is a Plugin Artifact?

A plugin artifact is a Git repository that contains all the necessary files and scripts to install and configure a plugin in a TrueNAS Core jail. The plugin index (this repository) references these artifact repositories via the `artifact` field in each plugin's JSON manifest.

## Artifact Repository Structure

```
your-plugin-artifact/
├── README.md           # Plugin documentation
├── post_install.sh     # Post-installation script (required)
├── ui.json            # Admin portal configuration (optional)
├── settings.json      # Plugin settings interface (optional)
└── overlay/           # Files to copy to jail (optional)
    └── usr/
        └── local/
            └── etc/
                └── config_files
```

## Required Files

### post_install.sh

This script runs *inside* the jail after package installation. It should:

- Enable services in `/etc/rc.conf`
- Create necessary directories and set permissions
- Initialize databases or configuration files
- Start required services
- Perform any other setup tasks

**Example:**

```bash
#!/bin/sh

# Enable and configure service
sysrc -f /etc/rc.conf myapp_enable="YES"
sysrc -f /etc/rc.conf myapp_data="/var/db/myapp"

# Create directories
mkdir -p /var/db/myapp
chown myapp:myapp /var/db/myapp

# Initialize database (if needed)
su -m myapp -c "myapp-init --data-dir=/var/db/myapp"

# Start service
service myapp start
```

## Optional Files

### ui.json

Defines the admin portal URL for the plugin. The `%%IP%%` placeholder is replaced with the jail's IP address.

**Example:**

```json
{
    "adminportal": "http://%%IP%%:8080"
}
```

### settings.json

Defines plugin settings that can be configured through the TrueNAS UI or iocage CLI.

**Required Fields:**

- `servicerestart`: Command to restart the service after settings change
- `serviceget`: Script to retrieve current setting values
- `serviceset`: Script to set new values

**Example:**

```json
{
    "servicerestart": "service myapp restart",
    "serviceget": "/usr/local/bin/myapp-get",
    "serviceset": "/usr/local/bin/myapp-set",
    "options": {
        "port": {
            "type": "int",
            "name": "Service Port",
            "description": "Port for incoming connections",
            "range": "1024-65535",
            "default": "8080",
            "requirerestart": true
        },
        "enable_ssl": {
            "type": "bool",
            "name": "Enable SSL",
            "description": "Use SSL/TLS for connections",
            "default": true,
            "requirerestart": true
        }
    }
}
```

### overlay/

Directory structure that will be overlaid onto the jail's filesystem. Files are copied after package installation but before `post_install.sh` runs.

**Example:**

```
overlay/
├── usr/
│   └── local/
│       ├── etc/
│       │   └── myapp.conf
│       └── bin/
│           └── myapp-helper.sh
└── var/
    └── db/
        └── myapp/
            └── config.ini
```

## Plugin Manifest

The plugin manifest (in this repository) references your artifact:

```json
{
    "name": "My Plugin",
    "release": "13.5-RELEASE",
    "artifact": "https://github.com/username/iocage-plugin-myplugin.git",
    "pkgs": [
        "myapp",
        "postgresql17-server",
        "nginx"
    ],
    "properties": {
        "dhcp": 1
    },
    "packagesite": "http://pkg.FreeBSD.org/${ABI}/latest",
    "fingerprints": {
        "plugin-default": [
            {
                "function": "sha256",
                "fingerprint": "b0170035af3acc5f3f3ae1859dc717101b4e6c1d0a794ad554928ca0cbb2f438"
            }
        ]
    },
    "official": false,
    "revision": 1
}
```

## Best Practices

1. **Test Thoroughly**: Test your plugin in a clean TrueNAS Core 13 environment
2. **Minimal Packages**: Only include necessary packages to reduce jail size
3. **Error Handling**: Include proper error checking in scripts
4. **Documentation**: Provide clear README with setup instructions
5. **Security**: Use HTTPS for artifact URLs
6. **Idempotent Scripts**: Scripts should be safe to run multiple times
7. **Clean Shutdown**: Ensure services stop cleanly when jail stops

## Testing Your Plugin

1. Create your artifact repository:
   ```bash
   git init iocage-plugin-myplugin
   cd iocage-plugin-myplugin
   # Add files
   git add .
   git commit -m "Initial plugin"
   git push
   ```

2. Create plugin manifest locally:
   ```bash
   cat > myplugin.json << 'EOF'
   {
       "name": "My Plugin",
       "release": "13.5-RELEASE",
       "artifact": "https://github.com/username/iocage-plugin-myplugin.git",
       ...
   }
   EOF
   ```

3. Test installation:
   ```bash
   iocage fetch -P myplugin.json ip4_addr="em0|192.168.1.100"
   ```

4. Verify:
   ```bash
   iocage list
   iocage console myplugin
   # Check services, logs, configuration
   ```

## Resources

- [TrueNAS Core Documentation](https://www.truenas.com/docs/core/)
- [iocage Documentation](https://iocage.readthedocs.io/)
- [FreeBSD Handbook](https://docs.freebsd.org/en/books/handbook/)
- [FreeBSD Ports](https://www.freshports.org/)

## Example Plugins

Check these examples for reference:

- [Gitea Plugin](https://github.com/damvcoool/iocage-plugin-gitea)
- [Nextcloud Plugin](https://github.com/damvcoool/iocage-plugin-nextcloud)
- [Odoo Plugin](https://github.com/damvcoool/iocage-plugin-odoo)
