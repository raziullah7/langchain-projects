import socket


def force_ipv4():
    """Resolve hostnames to IPv4 only.

    Workaround for networks where IPv6 to Google's API hangs.
    """
    _getaddrinfo = socket.getaddrinfo
    socket.getaddrinfo = lambda *a, **k: [
        r for r in _getaddrinfo(*a, **k) if r[0] == socket.AF_INET
    ]
