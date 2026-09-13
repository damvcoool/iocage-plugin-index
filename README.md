[plugins-shield]:https://img.shields.io/badge/FreeCORE-Personal%20Plugin%20Index-blue?logo=FreeBSD&style=for-the-badge
[plugins-link]:https://github.com/freecore-project/
[release-shield]:https://img.shields.io/badge/FreeBSD-15.1--RELEASE-blue?logo=FreeBSD&logoColor=red&style=for-the-badge
[release-link]:https://www.freebsd.org/releases/15.1R/relnotes/

[![x][plugins-shield]][plugins-link] [![x][release-shield]][release-link]

![GitHub last commit](https://img.shields.io/github/last-commit/damvcoool/iocage-plugin-index?style=for-the-badge)
![GitHub repo size](https://img.shields.io/github/repo-size/damvcoool/iocage-plugin-index?style=for-the-badge)

# FreeCORE Personal Plugin Index

Personal repository for [FreeCORE](https://github.com/freecore-project/) plugin manifests based on [FreeBSD 15.1-RELEASE](http://www.freebsd.org).

This is a custom plugin index maintained for personal use, containing plugins compatible with FreeCORE.

---

## Available Plugins

- **Gitea** - Lightweight code hosting solution written in Go
- **Nextcloud** - File hosting and collaboration platform
- **Immich** - Self-hosted photo and video backup solution
- **Odoo** - Open-source ERP and CRM suite

---

## Installing Plugins

### Prerequisites

- FreeCORE system based on FreeBSD 15.x
- Network connectivity
- Available storage for jail creation

### Using This Index

Use iocage with the plugin name from the `INDEX` file:

```sh
iocage fetch -P <plugin-name> -g https://github.com/damvcoool/iocage-plugin-index ip4_addr="<interface>|<IPaddress>"
```

Where:

- `plugin-name` is the name from the `INDEX` file, such as `gitea`, `nextcloud`, or `odoo`
- `interface` is the active network interface, such as `em0` or `igb0`
- `IPaddress` is the desired IP address for the plugin, such as `192.168.1.100`

### Using a Local File

```sh
iocage fetch -P /path/to/local/plugin.json ip4_addr="<interface>|<IPaddress>"
```

---

## Creating Plugins

To add a new plugin to this index:

1. Create a plugin JSON manifest file with the required fields:
   - `name`: Plugin name
   - `release`: FreeBSD release, such as `13.5-RELEASE`
   - `artifact`: URL to the plugin artifact repository
   - `pkgs`: Array of FreeBSD packages to install
   - `properties`: Plugin properties such as networking
2. Add an icon for your plugin in the [icons directory](icons/) in PNG format.
3. Update the [INDEX file](INDEX) with your plugin entry in alphabetical order.
4. Ensure your plugin artifact repository contains the expected scripts and metadata:
   - `post_install.sh` - Post-installation script
   - `ui.json` - Admin portal configuration, if needed
   - `settings.json` - Plugin settings interface, if needed

For detailed guidance, see the [template directory](template/) and the [FreeBSD Handbook](https://docs.freebsd.org/en/books/handbook/).

---

## Plugin Repositories

Each plugin references an artifact repository that contains the installation scripts and configuration:

- **Gitea**: https://github.com/damvcoool/iocage-plugin-gitea
- **Nextcloud**: https://github.com/damvcoool/iocage-plugin-nextcloud
- **Immich**: https://github.com/damvcoool/iocage-plugin-immich
- **Odoo**: https://github.com/damvcoool/iocage-plugin-odoo

---

## Resources

- [FreeCORE Project](https://github.com/freecore-project/)
- [FreeBSD Handbook](https://docs.freebsd.org/en/books/handbook/)
- [iocage Documentation](https://iocage.readthedocs.io/)
- [Plugin Template](template/)

---

## Contributing

This is a personal repository, but contributions and suggestions are welcome. Please open an issue or pull request with your ideas.

## License

This repository is maintained for personal use. Individual plugins may have their own licenses, so check each plugin's artifact repository for details.