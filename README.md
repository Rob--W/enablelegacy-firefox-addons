To enable legacy add-ons:

1. Run `sudo make install` to configure Firefox to respect the legacy extension preference.
2. Visit `about:config` and set the preferences:

  - `extensions.legacy.enabled` to `true`.

3. Optionally, to disable automatic updating:

  - `extensions.update.autoUpdateDefault` to `false`.

4. Optionally, if you want to disable extension signing, that can be done too:

  - `xpinstall.signatures.required` to `false`.

5. If you want to revert back to the default behavior
   (where the legacy and signatures preferences are ignored),
   run `sudo make uninstall`.

If your Firefox directory is not located at `/usr/lib/firefox`,
use the `FIREFOXDIR` variable to customize the location.
For example if you extracted a Firefox package to `/tmp/firefox57`,
use `make FIREFOXDIR=/tmp/firefox57/usr/lib/firefox install`.
