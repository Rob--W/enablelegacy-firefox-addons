#!/usr/bin/env python2

import sys
install = sys.argv[1] == 'install'
omnija = sys.argv[2]

with open(omnija, 'rb') as f:
    data = f.read()

databackup = data


def setAppConstant(key, defaultValue, newValue):
    """
    In Firefox 107 and earlier, the source looks like this:
    <blank line>
      MOZ_REQUIRE_SIGNING:
    //@line 287 "$SRCDIR/toolkit/modules/AppConstants.jsm"
      true,
    //@line 291 "$SRCDIR/toolkit/modules/AppConstants.jsm"
    <blank line>

    Since Firefox 108, the source looks like this:
    <blank line>
      MOZ_REQUIRE_SIGNING:
      true,
    <blank line>

    """
    global data
    key = b'\n\n  %s:\n' % key
    i = data.find(key)
    assert i != -1, b'Must find AppConstants.%s' % key
    i += len(key)

    # Find end of next line
    j = data.find(b'\n', i)
    assert i != -1, b'Must have a full line after AppConstants.%s key' % key
    line = data[i:j]
    if b'AppConstants.jsm"' in line:
        # Firefox 107 and earlier had a line with a comment.
        assert b'//' in line, b'Must be a comment: "%s"' % line
        i = j + 1  # 1 = len(b'\n')
        j = data.find(b'\n', i)
        assert j != -1, b'Must have a line after AppConstants.%s comment' % key
        line = data[i:j]
    else:
        # Firefox 108 and later no longer contains a comment. Let's verify that
        # we are in the AppConstants.sys.mjs file.
        filestart = data.rfind(b'mozilla.org/MPL', 0, i)
        assert filestart != -1, b'Must find license of AppConstants.%s' % key
        assert b'AppConstants = Object.freeze' in data[filestart:i], \
               b'Must find AppConstants.%s within AppConstants.sys.mjs' % key

    # Find the interesting line
    def makeLine(val): return b'  %s,' % val
    expectedLine = makeLine(defaultValue)
    assert line == expectedLine, \
        b'AppConstants.%s: "%s" == "%s"' % (key, expectedLine, line)
    data = data[:i] + makeLine(newValue) + data[j:]


if install:
    setAppConstant(b'MOZ_REQUIRE_SIGNING', b'true', b'!!!1')
else:
    setAppConstant(b'MOZ_REQUIRE_SIGNING', b'!!!1', b'true')


# Write only after all validation has passed.

with open('%s.bak' % omnija, 'wb') as f:
    f.write(databackup)

with open(omnija, 'wb') as f:
    f.write(data)
