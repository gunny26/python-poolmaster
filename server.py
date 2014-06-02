#!/usr/bin/python

import web
import json
from MCP3008 import MCP3008 as MCP3008

# GPIO.setmode(GPIO.BCM)
# Variablendefinition
SCLK        = 18 # Serial Clock
MOSI        = 24 # Master-Out Slave-IN
MISO        = 23 # Master-In Slave-Out
CS          = 25 # Chip-Select
mcp3008 = MCP3008(SCLK, MOSI, MISO, CS)

# web.py initialization
urls = ["/", "hello",
        "/getTemp", "getTemp",
        ]
app = web.application(urls, globals())

class hello(object):

    def GET(self):
        return("Hello\n")

class getTemp(object):

    def GET(self):
        data = {
            "TMP36-1 Pool Bottom" : mcp3008.read_tmp36(0),
            "TMP36-1 Pool Earth" : mcp3008.read_tmp36(1),
            "TMP36-1 Carport Air" : mcp3008.read_tmp36(2),
            "TMP36-1 T4" : mcp3008.read_tmp36(3),
            "TMP36-1 T5" : mcp3008.read_tmp36(4),
            "TMP36-1 T6" : mcp3008.read_tmp36(5),
        }
        return(json.dumps(data))

if __name__ == "__main__":
    app.run()
