# av-xymon
Xymon plays an important role within the Audio Visual department; within the software it has a feature to view all 'nongreen' systems. Annoyingly the list isn't sorted alphabetically; this scripts monitors the `nongreen.html` file, parses it, sorts it alphabetically and then writes the output to `nongreen_sorted.html`.

Xymon writes a new file to disk every sixty seconds, currently the script just runs every sixty seconds.
