.PHONY: install uninstall install-hook uninstall-hook

FIREFOXDIR := /usr/lib/firefox
LIBALPMDIR := /usr/share/libalpm

install:
	test -f $(FIREFOXDIR)/firefox  # FIREFOXDIR must contain the "firefox" binary
	./patch-firefox-enable-legacy.py install $(FIREFOXDIR)/omni.ja

uninstall:
	./patch-firefox-enable-legacy.py uninstall $(FIREFOXDIR)/omni.ja

install-hook:
	install -Dm644 firefox-enable-legacy.hook $(LIBALPMDIR)/hooks/firefox-enable-legacy.hook
	install -Dm755 patch-firefox-enable-legacy.py $(LIBALPMDIR)/scripts/patch-firefox-enable-legacy.py

uninstall-hook:
	cd $(LIBALPMDIR) && \
		rm -f hooks/firefox-enable-legacy.hook \
		rm -f scripts/patch-firefox-enable-legacy.py
