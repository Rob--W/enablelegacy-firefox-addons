This method patches Firefox so that the legacy extension and signing preferences are customizable again
(on release versions these are disabled by default).

The patcher validates that the files have the expected format before modifying the `omni.ja` package.
Before a change is made, the file is backed up as `omni.ja.bak`.

**Only use this when necessary, at your own risk.**

Usage:

```sh
# Enable
./patch-firefox-enable-legacy.py install /usr/lib/firefox/omni.ja

# Restore
./patch-firefox-enable-legacy.py uninstall /usr/lib/firefox/omni.ja
```

Or:

```sh
# Enable
make install

# Restore
make uninstall
```

If using a non-standard Firefox directory:

```sh
make install FIREFOXDIR=/path/to/firefoxdir
```

For ArchLinux (that uses pacman as a package manager),
it is possible to automatically patch the file when the Firefox package is updated.
To install the hook, use `sudo make install-hook`.
To uninstall the hook, use `sudo make uninstall-hook`.
