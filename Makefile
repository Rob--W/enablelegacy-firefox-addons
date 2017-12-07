.PHONY: install uninstall

FIREFOXDIR := /usr/lib/firefox

install:
	test -f $(FIREFOXDIR)/firefox  # FIREFOXDIR must contain the "firefox" binary
	install -Dm644 enablelegacy.cfg $(FIREFOXDIR)/enablelegacy.cfg
	install -Dm644 enablelegacy-prefs.js $(FIREFOXDIR)/defaults/pref/enablelegacy-prefs.js

uninstall:
	rm -f $(FIREFOXDIR)/enablelegacy.cfg $(FIREFOXDIR)/defaults/pref/enablelegacy-prefs.js
