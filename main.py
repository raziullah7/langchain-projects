# Workaround: if IPv6 to Google's API hangs on your network, uncomment
# this to resolve IPv4 only.
# import socket
#
# _getaddrinfo = socket.getaddrinfo
# socket.getaddrinfo = lambda *a, **k: [
#     r for r in _getaddrinfo(*a, **k) if r[0] == socket.AF_INET
# ]


def main():
    print("Hello from langchain-projects!")


if __name__ == "__main__":
    main()
