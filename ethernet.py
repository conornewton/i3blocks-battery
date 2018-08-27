#!/usr/bin/env python3

import subprocess

ethernet = subprocess.check_output(["nmcli"],universal_newlines=True)
print(ethernet)
