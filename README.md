# collectd-plugin-VMG1312-B30A-xDSL

## Supported hardware
This is a [collectd](https://collectd.org/) plugin for monitoring the
xDSL status of Zyxel VMG1312 VDSL/VDSL2 modems/routers.

I developed and tested it with the B30A-version (a VDSL2-Vectoring modem
for Germany) of this modem, but it might work as well with other
variants.


## Supported parameters
This plugin reads the ***xDSL-status only***!

For reading things like interface-counters etc. the modem has an
**SNMP-server** that can be used. Unfortunately this SNMP-server does
not serve the xDSL-status (facepalm!), that's where this plugin comes
into place.

If your modem has a page like the one shown below, this plugin will
probably be able to read all status parameters of the first three
sections. The "VDSL Counters" section won't be a read - I don't see much
use in reading these.

![VMG1312-B30A-xDSL-page](VMG1312-B30A-xDSL-page.png)

## Dependencies
- collectd 4.9+

## Installation
1. `pip install collectd-plugin-VMG1312-B30A-xDSL `
2. Configure the plugin as shown below
3. Restart collectd

## Configuration
```
<LoadPlugin python> 
    Globals true 
</LoadPlugin> 
<Plugin python>
    Import "collectd-plugin-VMG1312-B30A-xDSL"

    <Module collectd-plugin-VMG1312-B30A-xDSL>
        URL "http://yourmodem.yourdomain"
        User "admin"
        Password "1234"
    </Module>
</Plugin>
````

## License
This project is licensed under the terms of the GPLv3 license.



