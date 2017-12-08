# Enabling legacy add-ons in Firefox Quantum
Legacy Firefox add-ons are not supported any more in Firefox 57.
The successor, WebExtensions, are more secure but less powerful.
If you want to load a legacy add-on, then the following steps will allow you to
do so. Just keep in mind that these add-ons can break at any time when Firefox
updates.

**Add-ons built using legacy technology are a security and stability risk,
because these add-ons run with the full privileges of the browser without any
sandboxing.
Do not follow these instructions unless you are aware of the consequences.**

These steps rely on "autoconfig", a feature to support
[enterprise deployments of Firefox](https://developer.mozilla.org/en-US/Firefox/Enterprise_deployment#Configuration).

To enable legacy add-ons:

1. Copy the `enablelegacy.cfg` to Firefox's application directory,
   and `enablelegacy-prefs.js` to the `defaults/pref/` subdirectory.
   If you use Linux, just run `sudo make install`.
2. Visit `about:config` and set the preferences:

  - `extensions.legacy.enabled` to `true`.

3. Optionally, to disable automatic updating:

  - `extensions.update.autoUpdateDefault` to `false`.

4. Optionally, if you want to disable extension signing, that can be done too:

  - `xpinstall.signatures.required` to `false`.

5. If you want to revert back to the default behavior
   (where the legacy and signatures preferences are ignored),
   delete the files from step 1 (or run `sudo make uninstall`).

If your Firefox directory is not located at `/usr/lib/firefox`,
use the `FIREFOXDIR` variable to customize the location.
For example if you extracted a Firefox package to `/tmp/firefox57`,
use `make FIREFOXDIR=/tmp/firefox57/usr/lib/firefox install`.


## Migrating from Firefox 56 or earlier to Firefox 57 or later

When you are running Firefox 56 with several legacy add-ons,
and don't want them to be disabled or updated to a newer
WebExtension version, follow the next steps:

1. Run `sudo make install` (on Linux).
   (for Windows/macOS, see the first step of the previous section).
2. Start Firefox (any version) and visit `about:config`.
3. Create and/or set the following preferences:

  - `extensions.legacy.enabled` to `true`.
  - `extensions.update.autoUpdateDefault` to `false`.

  NOTE: If you do not want to be without legacy add-ons during the upgrade,
  set these preferences *before* starting the new Firefox version.

4. Go to `about:addons` and confirm that the list of add-ons looks fine.
5. Some add-ons may already be enabled. If a request to restart Firefox
   appears, then the add-on is either not restartless, or not marked as
   multiprocess-compatible. In the latter case, restarting Firefox will
   cause it to start in single-process mode (which has a worse performance).

**Legacy add-ons are not supported in Firefox 57 and may break at any time.**


### Installing / updating legacy add-ons

Do not use the built-in updater to update a legacy add-on, unless you are
willing to upgrade to a WebExtension version of the add-on (with potentially
different functionality).

To update a legacy add-on (or install a new one) from addons.mozilla.org, you
can either copy the "Download anyway" link below the install button, remove
`type:attachment/` from the URL, paste the URL in the location bar and press
Enter.

Another way to get the install button to be clickable (and search results to
include legacy add-ons) is to use the built-in devtools to change the
[user agent](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent/Firefox):

1. Open the built-in Responsive Design Mode (devtools)
   (shortcut: <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>M</kbd>).
2. Find your user agent string, e.g. by opening the devtools (<kbd>F12</kbd>)
   and copying the result of running `navigator.userAgent`.
3. Paste the user agent string in the User Agent input box at the top of the
   Responsive Design Mode tool, change the last number to 56 and click inside
   the page to refresh. Here is an example of a user agent string that enables
   installation of legacy add-ons (for Linux):  

     Mozilla/5.0 (X11; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/56.0

4. Now the Install button for legacy add-ons is enabled again on AMO!

To install an unsigned legacy add-on from another location, visit `about:config`
and set `xpinstall.signatures.required` to `false`. Use at your own risk!
