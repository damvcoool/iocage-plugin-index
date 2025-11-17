[plugins-shield]:https://img.shields.io/badge/TrueNAS%20CORE-Personal%20Plugin%20Index-blue?logo=TrueNAS&style=for-the-badge
[plugins-link]:https://www.truenas.com/plugins/
[release-shield]:https://img.shields.io/badge/FreeBSD-13.5--RELEASE-blue?logo=FreeBSD&logoColor=red&style=for-the-badge
[release-link]:https://www.freebsd.org/releases/13.5R/relnotes/

[![x][plugins-shield]][plugins-link] [![x][release-shield]][release-link]

![GitHub last commit](https://img.shields.io/github/last-commit/damvcoool/iocage-plugin-index?style=for-the-badge)
![GitHub repo size](https://img.shields.io/github/repo-size/damvcoool/iocage-plugin-index?style=for-the-badge)

# TrueNAS Core 13 Personal Plugin Index

Personal repository for [TrueNAS Core 13](https://www.truenas.com/) Plugins/Jails based on [FreeBSD 13.5-RELEASE](http://www.freebsd.org).

This is a custom plugin index maintained for personal use, containing plugins compatible with TrueNAS Core 13.

## Available Plugins

Currently available plugins in this index:

- **Gitea** - Lightweight code hosting solution written in Go
- **Nextcloud** - File hosting and collaboration platform
- **Odoo** - Open-source ERP and CRM suite

# Creating Plugins

To add a new plugin to this personal index:

1. Create a plugin JSON manifest file (e.g., `myplugin.json`) with the required fields:
   - `name`: Plugin name
   - `release`: FreeBSD release (e.g., "13.5-RELEASE")
   - `artifact`: URL to your plugin artifact repository
   - `pkgs`: Array of FreeBSD packages to install
   - `properties`: Plugin properties (networking, etc.)

2. Add an icon for your plugin in the [icons directory](icons/) (PNG format, 128x128 pixels recommended)

3. Update the [INDEX file](INDEX) with your plugin entry in alphabetical order

4. Ensure your plugin artifact repository contains:
   - `post_install.sh` - Post-installation script
   - `ui.json` - Admin portal configuration (optional)
   - `settings.json` - Plugin settings interface (optional)

For detailed information on creating plugins, see the [template directory](template/) and [TrueNAS documentation](https://www.truenas.com/docs/core/).

# Installing Plugins

## Prerequisites

- TrueNAS Core 13.x system
- Network connectivity
- Available storage for jail creation

## Using This Custom Index

To use this personal plugin index with iocage on TrueNAS Core 13:

<pre>
iocage fetch -P <i>plugin-name</i> -g https://github.com/damvcoool/iocage-plugin-index ip4_addr="<i>interface</i>|<i>IPaddress</i>"
</pre>

where:
- *plugin-name* is the name from the INDEX file (e.g., `gitea`, `nextcloud`, `odoo`)
- *interface* is the name of the active network interface (e.g., `em0`, `igb0`)
- *IPaddress* is the desired IP address for the plugin (e.g., `192.168.1.100`)

**Example:**
<pre>
iocage fetch -P gitea -g https://github.com/damvcoool/iocage-plugin-index ip4_addr="igb0|192.168.1.100"
</pre>

## Using Local File

To install a plugin using a local manifest file:
<pre>
iocage fetch -P /path/to/local/plugin.json ip4_addr="<i>interface</i>|<i>IPaddress</i>"
</pre>

## Post-Installation

After installation, access your plugin's web interface (if available) through the admin portal URL specified in the plugin's `ui.json` file. Check the jail's IP address with:

<pre>
iocage list
</pre>

## Plugin Repositories

Each plugin references an artifact repository that contains the installation scripts and configuration:

- **Gitea**: https://github.com/damvcoool/iocage-plugin-gitea
- **Nextcloud**: https://github.com/damvcoool/iocage-plugin-nextcloud  
- **Odoo**: https://github.com/damvcoool/iocage-plugin-odoo

# Contributing

This is a personal repository, but contributions and suggestions are welcome! Feel free to:

- Report issues with existing plugins
- Suggest improvements to plugin configurations
- Propose new plugins for TrueNAS Core 13

Please open an issue or pull request with your suggestions.

# Resources

- [TrueNAS Core Documentation](https://www.truenas.com/docs/core/)
- [FreeBSD Handbook](https://docs.freebsd.org/en/books/handbook/)
- [iocage Documentation](https://iocage.readthedocs.io/)
- [Plugin Template](template/)

# License

This repository is maintained for personal use. Individual plugins may have their own licenses - please check each plugin's artifact repository for details.
