// First line must be a comment.

pref("general.config.filename", "enablelegacy.cfg");
pref("general.config.obscure_value", 0);

// Do not automatically upgrade legacy add-ons when upgrading the browser.
// (Note: To avoid unwanted legacy -> WebExtension upgrades,
//  visit about:config and set extensions.update.autoUpdateDefault to false ).
pref("extensions.showMismatchUI", false);

// When this preference is toggled, legacy add-ons are automatically re-enabled.
// Non-restartless add-ons may require a restart of the browser.
// Non-multiprocess-compatible add-ons may disable e10s.
// pref("extensions.legacy.enabled", true);
// pref("xpinstall.signatures.required", false);
// (Note: uncommenting won't work because app/profile/firefox.js also sets them)

// Maybe even the following, to allow manual execution of JS code in the global console.
// pref("devtools.chrome.enabled", true);
