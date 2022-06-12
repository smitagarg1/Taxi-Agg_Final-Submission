# Copyright 2014-present MongoDB, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you
# may not use this file except in compliance with the License.  You
# may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.  See the License for the specific language governing
# permissions and limitations under the License.

"""A fake SSLContext implementation."""

import ssl as _ssl
import sys as _sys

# PROTOCOL_TLS_CLIENT is Python 3.6+
PROTOCOL_SSLv23 = getattr(_ssl, "PROTOCOL_TLS_CLIENT", _ssl.PROTOCOL_SSLv23)
OP_NO_SSLv2 = getattr(_ssl, "OP_NO_SSLv2", 0)
OP_NO_SSLv3 = getattr(_ssl, "OP_NO_SSLv3", 0)
OP_NO_COMPRESSION = getattr(_ssl, "OP_NO_COMPRESSION", 0)
# Python 3.7+, OpenSSL 1.1.0h+
OP_NO_RENEGOTIATION = getattr(_ssl, "OP_NO_RENEGOTIATION", 0)

HAS_SNI = getattr(_ssl, "HAS_SNI", False)
IS_PYOPENSSL = False

# Base Exception class
SSLError = _ssl.SSLError

from ssl import SSLContext  # noqa: F401,E402

if hasattr(_ssl, "VERIFY_CRL_CHECK_LEAF"):
    from ssl import VERIFY_CRL_CHECK_LEAF  # noqa: F401
# Python 3.7 uses OpenSSL's hostname matching implementation
# making it the obvious version to start using SSLConext.check_hostname.
# Python 3.6 might have been a good version, but it suffers
# from https://bugs.python.org/issue32185.
CHECK_HOSTNAME_SAFE = _sys.version_info[:2] >= (3, 7)
