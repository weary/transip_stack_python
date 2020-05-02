
# How to use the TransIP STACK API from python
Turns out TransIP just uses webdav, so any python webdav wrapper will work

# The example
My example uses the webdavclient3 library to talk to stackstorage. To run the example export these environment variables:

```
export STACK_USERNAME=<your username>
export STACK_PASSWORD=<your password>
export STACK_HOSTNAME=https://<your name>.stackstorage.com
```

Run pip-install to pull in dependencies

```
pip install -e .
```

Run the example
```
transip_upload /tmp/localtestfile.txt /remotedestination.txt
```
