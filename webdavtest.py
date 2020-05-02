from webdav3.client import Client
import os
import sys
from pathlib import Path

# simple example on how to talk to the transip stack storage api (which is just webdav)
# this sample expects the following environment variables to be set
# export STACK_USERNAME=<your username>
# export STACK_PASSWORD=<your password>
# export STACK_HOSTNAME=https://<your name>.stackstorage.com


def upload():
    options = {
        "webdav_hostname": os.environ["STACK_HOSTNAME"],
        "webdav_root": "/remote.php/webdav/",
        "webdav_login": os.environ["STACK_USERNAME"],
        "webdav_password": os.environ["STACK_PASSWORD"],
        # 'webdav_verbose': True,
    }
    if not options["webdav_hostname"]:
        raise Exception("STACK_HOSTNAME environment variable not set")
    if not options["webdav_login"]:
        raise Exception("STACK_USERNAME environment variable not set")
    if not options["webdav_password"]:
        raise Exception("STACK_PASSWORD environment variable not set")

    if len(sys.argv) != 3:
        raise Exception("syntax: {} <local file> <remote file>".format(sys.argv[0]))

    if not Path(sys.argv[1]).exists:
        raise Exception("local file does not exist")

    if not sys.argv[2].startswith("/"):
        raise Exception("remote file is not an absolute path")

    client = Client(options)
    # client.verify = False  # To not check SSL certificates (Default = True)

    # client.execute_request("clean", "/mytestdir")
    # client.execute_request("mkdir", '/mytestdir')
    # client.upload_file("/mytestdir/lorum.txt", "/tmp/testfile.txt")
    client.upload_file(sys.argv[2], sys.argv[1])
