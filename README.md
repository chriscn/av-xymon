# av-xymon

Xymon plays an important role within the Audio Visual department; within the software it has a feature to view all 'nongreen' systems. Annoyingly the list isn't sorted alphabetically; this scripts monitors the `nongreen.html` file, parses it, sorts it alphabetically and then writes the output to `nongreen_sorted.html`.

Xymon writes a new file to disk every sixty seconds, currently the script just runs every sixty seconds.

## Installation

These installation instructions are relatively customised for the University of York's Audio Visual setup; if you'd like some help in setting it up then please contact the author and/or raise an issue here.

### Create a user

You'll need to create a user, then add to the group `xymon` so that it can write to the `/var/lib/xymon/www` directory. It will be assumed that the user is created, and you are logged in as them for the rest of this installation instruction.

### Clone the repository

Run `git clone https://github.com/chriscn/av-xymon.git` to your home directory. If you do not have `git` installed then you can just download the zip from the [GitHub](https://github.com/chriscn/av-xymon).

### Install the dependencies

Ensure that you have the following installed on your system.

- Python3+
- PIP

Then run `pip<3> install -r requirements.txt` to install BeautifulSoup; this is the main dependency that does the processing. You should ensure these dependencies are installed globally.

### Service Installation

These instructions are largely copied from this [Guide](https://medium.com/codex/setup-a-python-script-as-a-service-through-systemctl-systemd-f0cc55a42267).

Copy the follow into `/etc/systemd/system/av-xymon.service`. Replacing username with the username that you chose earlier.

```
[Unit]
Description=av-xymon
After=multi-user.target

[Service]
Type=simple
Restart=always
ExecStart=/usr/bin/python3 /home/<username>/av-xymon/sort.py

[Install]
WantedBy=multi-user.target
```

Then run the following commands:

- `sudo systemctl daemon-reload`
- `sudo systemctl enable av-xymon.service`
- `sudo systemctl start av-xymon.service`

Then check the status with: `sudo systemctl status av-xymon.service`
