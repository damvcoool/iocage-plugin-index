# Contributing to TrueNAS Core 13 Plugin Index

Thank you for your interest in contributing to this personal TrueNAS Core 13 plugin index!

## Overview

This is a personal repository for maintaining plugins compatible with TrueNAS Core 13 (FreeBSD 13.5-RELEASE). While primarily maintained for personal use, contributions and suggestions are welcome.

## How to Contribute

### Reporting Issues

If you encounter issues with existing plugins:

1. Check if the issue has already been reported
2. Create a new issue with:
   - Plugin name and version
   - TrueNAS Core version
   - Detailed description of the problem
   - Steps to reproduce
   - Expected vs actual behavior

### Suggesting Improvements

To suggest improvements to existing plugins:

1. Open an issue describing the proposed improvement
2. Explain the benefits and use cases
3. Reference any relevant documentation

### Proposing New Plugins

To propose a new plugin for inclusion:

1. Ensure the plugin works with FreeBSD 13.5-RELEASE / TrueNAS Core 13
2. Create the plugin artifact repository with:
   - `post_install.sh` - Installation and setup script
   - `ui.json` - Admin portal configuration (optional)
   - `settings.json` - Plugin settings interface (optional)
   - `README.md` - Documentation
3. Test the plugin thoroughly
4. Open a pull request with:
   - Plugin JSON manifest
   - Icon file (PNG, 128x128 pixels recommended)
   - INDEX file entry

## Plugin Development Guidelines

### Plugin Manifest Requirements

Your plugin JSON manifest must include:

```json
{
    "name": "Plugin Name",
    "release": "13.5-RELEASE",
    "artifact": "https://github.com/username/iocage-plugin-name.git",
    "pkgs": [
        "package1",
        "package2"
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

### Best Practices

1. **Naming**: Use lowercase for plugin names in INDEX and JSON files
2. **Release Version**: Use FreeBSD 13.5-RELEASE for TrueNAS Core 13 compatibility
3. **Packages**: Only include necessary packages to minimize jail size
4. **Testing**: Test plugins in a clean environment before submission
5. **Documentation**: Include clear setup instructions in your artifact repository
6. **Security**: Use HTTPS for all artifact URLs
7. **Icons**: Provide clear, recognizable icons (PNG format, 128x128 pixels)

### Artifact Repository Structure

```
iocage-plugin-name/
├── README.md
├── post_install.sh
├── ui.json (optional)
├── settings.json (optional)
└── overlay/ (optional)
    └── usr/
        └── local/
            └── etc/
                └── config_files
```

### Post-Install Script

The `post_install.sh` script should:

- Enable necessary services in `/etc/rc.conf`
- Set appropriate file permissions
- Create required directories
- Initialize databases or configurations
- Start services

Example:

```bash
#!/bin/sh

# Enable service
sysrc -f /etc/rc.conf myservice_enable="YES"

# Create directories
mkdir -p /var/db/myservice
chown myuser:myuser /var/db/myservice

# Start service
service myservice start
```

## Pull Request Process

1. Fork the repository
2. Create a feature branch (`git checkout -b add-plugin-name`)
3. Add your plugin files:
   - Plugin JSON manifest
   - Icon in `icons/` directory
   - Entry in `INDEX` file (alphabetical order)
4. Test your changes
5. Commit with descriptive messages
6. Push to your fork
7. Open a pull request

### Pull Request Checklist

- [ ] Plugin JSON manifest is valid
- [ ] Icon file added to `icons/` directory
- [ ] Entry added to INDEX file in alphabetical order
- [ ] Plugin tested on TrueNAS Core 13
- [ ] Artifact repository is accessible
- [ ] README.md updated if needed
- [ ] All JSON files pass validation

## Testing

Before submitting:

1. Validate JSON syntax:
   ```bash
   python -m json.tool your-plugin.json
   ```

2. Test plugin installation:
   ```bash
   iocage fetch -P your-plugin -g https://github.com/damvcoool/iocage-plugin-index ip4_addr="em0|192.168.1.100"
   ```

3. Verify services start correctly
4. Test admin portal access (if applicable)
5. Check logs for errors

## Questions?

Feel free to open an issue for any questions or clarifications needed.

## Code of Conduct

Please be respectful and constructive in all interactions. This is a community-focused project.

## License

By contributing, you agree that your contributions will be licensed under the same terms as the repository.
