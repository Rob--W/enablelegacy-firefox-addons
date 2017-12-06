.PHONY: install uninstall

FIREFOXDIR := /usr/lib/firefox

install:
	test -f $(FIREFOXDIR)/firefox  # FIREFOXDIR must contain the "firefox" binary
	install -Dm644 mozilla.cfg $(FIREFOXDIR)/mozilla.cfg
	install -Dm644 enablelegacy-prefs.js $(FIREFOXDIR)/defaults/pref/enablelegacy-prefs.js

uninstall:
	rm -f $(FIREFOXDIR)/mozilla.cfg $(FIREFOXDIR)/defaults/pref/enablelegacy-prefs.js
