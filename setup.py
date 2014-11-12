from distutils.core import setup

import platform, os
sysname = platform.system()
if sysname == "Windows":
    binpath = os.getenv("SystemRoot")
else:
    binpath = r"/usr/local/bin"

setup(
    name = "Toast",
    packages = ["Toast"],
    version = "0.0.1",
    # data_files = [(binpath, ["scripts/gmailsend"])],
    description = "Cross-platform desktop notification using Qt",
    author = "Kaiyin Zhong",
    author_email = "kindlychung@gmail.com",
    url = "https://github.com/kindlychung/Toast",
    keywords = ["notification", "cross-platform"]
    )

