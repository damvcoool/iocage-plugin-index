# Quick Reference Guide for Plugin Development

## Quick Commands

### Validate Your Plugin
```bash
python3 validate.py
```

### Install Plugin Locally
```bash
iocage fetch -P /path/to/plugin.json ip4_addr="em0|192.168.1.100"
```

### Install from This Index
```bash
iocage fetch -P plugin-name -g https://github.com/damvcoool/iocage-plugin-index ip4_addr="em0|192.168.1.100"
```

### Check Jail Status
```bash
iocage list
iocage console plugin-name
```

### Stop/Start Plugin
```bash
iocage stop plugin-name
iocage start plugin-name
```

### Delete Plugin
```bash
iocage destroy plugin-name
```

## Plugin Manifest Template

```json
{
    "name": "MyPlugin",
    "release": "13.5-RELEASE",
    "artifact": "https://github.com/username/iocage-plugin-myplugin.git",
    "pkgs": [
        "main-package",
        "dependency-package"
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

## INDEX Entry Template

```json
"myplugin": {
    "MANIFEST": "myplugin.json",
    "name": "MyPlugin",
    "icon": "https://raw.githubusercontent.com/username/repo/main/icons/myplugin.png",
    "description": "Brief description of your plugin.",
    "official": false,
    "primary_pkg": "main-package-name"
}
```

## Post Install Script Template

```bash
#!/bin/sh

# Enable service
sysrc -f /etc/rc.conf myservice_enable="YES"
sysrc -f /etc/rc.conf myservice_flags="--config /usr/local/etc/myservice.conf"

# Create directories
mkdir -p /var/db/myservice
chown myservice:myservice /var/db/myservice

# Initialize if needed
if [ ! -f /var/db/myservice/initialized ]; then
    echo "Initializing myservice..."
    su -m myservice -c "myservice-init"
    touch /var/db/myservice/initialized
fi

# Start service
service myservice start
```

## UI JSON Template

```json
{
    "adminportal": "http://%%IP%%:8080"
}
```

## Common Packages for Plugins

### Web Servers
- `nginx`
- `apache24`
- `lighttpd`

### Databases
- `postgresql17-server`
- `postgresql17-contrib`
- `mysql91-server`
- `sqlite3`
- `redis`

### Python
- `py311-pip`
- `py311-setuptools`

### PHP
- `php84`
- `php84-extensions`

### Node.js
- `node20`
- `npm-node20`

## Troubleshooting

### Check Service Status
```bash
iocage console plugin-name
service myservice status
```

### View Logs
```bash
iocage console plugin-name
tail -f /var/log/myservice.log
```

### Test Network
```bash
iocage console plugin-name
ping -c 3 8.8.8.8
curl -I http://localhost:8080
```

### Package Issues
```bash
iocage console plugin-name
pkg info
pkg search package-name
```

## File Locations

- Plugin manifests: `/home/runner/work/iocage-plugin-index/iocage-plugin-index/*.json`
- Icons: `/home/runner/work/iocage-plugin-index/iocage-plugin-index/icons/`
- INDEX: `/home/runner/work/iocage-plugin-index/iocage-plugin-index/INDEX`
- Template: `/home/runner/work/iocage-plugin-index/iocage-plugin-index/template/`

## Useful Resources

- [FreeBSD Ports Search](https://www.freshports.org/)
- [TrueNAS Forums](https://www.truenas.com/community/)
- [iocage Documentation](https://iocage.readthedocs.io/)
- [FreeBSD Handbook](https://docs.freebsd.org/en/books/handbook/)

## Validation Checklist

- [ ] JSON syntax valid
- [ ] All required fields present
- [ ] Icon file exists (PNG, 128x128)
- [ ] Artifact repository accessible
- [ ] Packages available in FreeBSD repos
- [ ] post_install.sh tested
- [ ] Services start correctly
- [ ] Admin portal accessible
- [ ] Plugin can be stopped/started
- [ ] Plugin can be deleted cleanly
