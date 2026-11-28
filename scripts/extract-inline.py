#!/usr/bin/env python3
"""Print the main inline <script> of an HTML file, for node --check."""
import sys
h = open(sys.argv[1], encoding="utf-8").read()
i = h.rindex("<script>")
j = h.index("</script>", i)
sys.stdout.write(h[i + 8:j])
