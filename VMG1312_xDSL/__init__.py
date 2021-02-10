try:
    # This is only availabe "inside" collectd
    import collectd
except ImportError:
    # Outside collectd we need to mock this class, since the linter will complain etc.
    import collectd_mock as collectd

import requests
import sys, time, os
from xdslInfo import XdslInfo
from bs4 import BeautifulSoup

PLUGIN_NAME = 'VMG1312-B30A-xDSL'

loginpath = "/login/login-page.cgi"
dslpath = "/pages/systemMonitoring/xdslStatistics/xdslStatistics.html"
xdslinfo = XdslInfo()
params = {}


def getXDSLStats(host, user, password):
    # Login first
    # Using session to store cookies:
    session = requests.session()
    session.post(host + loginpath, {
        'AuthName': user,
        'AuthPassword': password
    })

    # Get page with xDSL Stats
    xdslrequest = session.get(host + dslpath)
    # Parse page with BS
    soup = BeautifulSoup(xdslrequest.content, 'html.parser')
    # Extract text-object and parse with XdslInfo
    xdslinfo.parse(soup.find(id='VdslInfoDisplay').text)


def printDSLStats():
    log(xdslinfo)


def init():
    log("Plugin %s initializing..." % PLUGIN_NAME)


def shutdown():
    log("Plugin %s shutting down..." % PLUGIN_NAME)


def callback_configure(config):
    """ Configure callback """
    for node in config.children:
        if node.key == 'URL':
            params['url'] = node.values[0]
            log("Plugin %s configured to get " + params['url'] % PLUGIN_NAME)
        elif node.key == 'User':
            params['user'] = node.values[0]
        elif node.key == 'Password':
            params['password'] = node.values[0]
        else:
            collectd.warning('fritzcollectd: Unknown config %s' % node.key)


def log(param):
    if __name__ != '__main__':
        collectd.info("%s: %s" % (PLUGIN_NAME, param))
    else:
        sys.stderr.write("%s\n" % param)


def read():
    getXDSLStats(params['url'], params['user'], params['password'])
    if __name__ != "__main__":
        if xdslinfo.vdsl_trainingstatus == "Showtime":
            vdsl_trainingstatus = 1
        else:
            vdsl_trainingstatus = 0
        collectd.Values(plugin=PLUGIN_NAME,
                        type_instance="trainingstatus",
                        type="gauge",
                        values=[vdsl_trainingstatus]
                        ).dispatch()

        if xdslinfo.vdsl_gvector  == True:
            vdsl_gvector = 1
        else:
            vdsl_gvector = 0
        collectd.Values(plugin=PLUGIN_NAME,
                        type_instance="gvector",
                        type="gauge",
                        values=[vdsl_gvector]
                        ).dispatch()

        collectd.Values(plugin=PLUGIN_NAME,
                        type_instance="uptime",
                        type="uptime",
                        values=[xdslinfo.vdsl_linkuptime_timedelta.total_seconds()]
                        ).dispatch()

        # VDSL Port Details
        collectd.Values(plugin=PLUGIN_NAME,
                        type_instance="lineRate_upstream",
                        type="gauge",
                        values=[xdslinfo.vdsl_upstream_linerateMbps]
                        ).dispatch()

        collectd.Values(plugin=PLUGIN_NAME,
                        type_instance="lineRate_downstream",
                        type="gauge",
                        values=[xdslinfo.vdsl_downstream_linerateMbps]
                        ).dispatch()

        collectd.Values(plugin=PLUGIN_NAME,
                        type_instance="netDataRate_upstream",
                        type="gauge",
                        values=[xdslinfo.vdsl_upstream_netdatarateMbps]
                        ).dispatch()

        collectd.Values(plugin=PLUGIN_NAME,
                        type_instance="netDataRate_downstream",
                        type="gauge",
                        values=[xdslinfo.vdsl_downstream_netdatarateMbps]
                        ).dispatch()

        trellis = 0
        if xdslinfo.vdsl_upstream_trelliscoding:
            trellis = 1
        collectd.Values(plugin=PLUGIN_NAME,
                        type_instance="trellisCoding_upstream",
                        type="gauge",
                        values=[trellis]
                        ).dispatch()

        trellis = 0
        if xdslinfo.vdsl_downstream_trelliscoding:
            trellis = 1
        collectd.Values(plugin=PLUGIN_NAME,
                        type_instance="trellisCoding_downstream",
                        type="gauge",
                        values=[trellis]
                        ).dispatch()

        collectd.Values(plugin=PLUGIN_NAME,
                        type_instance="snrMargin_upstream",
                        type="gauge",
                        values=[xdslinfo.vdsl_upstream_snrmarginDB]
                        ).dispatch()

        collectd.Values(plugin=PLUGIN_NAME,
                        type_instance="snrMargin_downstream",
                        type="gauge",
                        values=[xdslinfo.vdsl_downstream_snrmarginDB]
                        ).dispatch()

        collectd.Values(plugin=PLUGIN_NAME,
                        type_instance="actualDelay_upstream",
                        type="gauge",
                        values=[xdslinfo.vdsl_upstream_actualdelayMS]
                        ).dispatch()

        collectd.Values(plugin=PLUGIN_NAME,
                        type_instance="actualDelay_downstream",
                        type="gauge",
                        values=[xdslinfo.vdsl_downstream_actualdelayMS]
                        ).dispatch()

        collectd.Values(plugin=PLUGIN_NAME,
                        type_instance="transmitPower_upstream",
                        type="gauge",
                        values=[xdslinfo.vdsl_upstream_transmitPowerDBm]
                        ).dispatch()

        collectd.Values(plugin=PLUGIN_NAME,
                        type_instance="transmitPower_downstream",
                        type="gauge",
                        values=[xdslinfo.vdsl_downstream_transmitPowerDBm]
                        ).dispatch()

        collectd.Values(plugin=PLUGIN_NAME,
                        type_instance="receivePower_upstream",
                        type="gauge",
                        values=[xdslinfo.vdsl_upstream_receivePowerDBm]
                        ).dispatch()

        collectd.Values(plugin=PLUGIN_NAME,
                        type_instance="receivePower_downstream",
                        type="gauge",
                        values=[xdslinfo.vdsl_downstream_receivePowerDBm]
                        ).dispatch()

        collectd.Values(plugin=PLUGIN_NAME,
                        type_instance="actualInpSymbols_upstream",
                        type="gauge",
                        values=[xdslinfo.vdsl_upstream_actualInpSymbols]
                        ).dispatch()

        collectd.Values(plugin=PLUGIN_NAME,
                        type_instance="actualInpSymbols_downstream",
                        type="gauge",
                        values=[xdslinfo.vdsl_downstream_actualInpSymbols]
                        ).dispatch()

        collectd.Values(plugin=PLUGIN_NAME,
                        type_instance="totalAttenuation_upstream",
                        type="gauge",
                        values=[xdslinfo.vdsl_upstream_totalAttenuationDB]
                        ).dispatch()

        collectd.Values(plugin=PLUGIN_NAME,
                        type_instance="totalAttenuation_downstream",
                        type="gauge",
                        values=[xdslinfo.vdsl_downstream_totalAttenuationDB]
                        ).dispatch()

        collectd.Values(plugin=PLUGIN_NAME,
                        type_instance="attainableNetDataRate_upstream",
                        type="gauge",
                        values=[xdslinfo.vdsl_upstream_attainableNetDataRateMbps]
                        ).dispatch()

        collectd.Values(plugin=PLUGIN_NAME,
                        type_instance="attainableNetDataRate_downstream",
                        type="gauge",
                        values=[xdslinfo.vdsl_downstream_attainableNetDataRateMbps]
                        ).dispatch()

        # VDSL Band Status
        # Line Attenuation(dB)
        if xdslinfo.vdsl_band_lineattenuationDB_U0 is not None:
            collectd.Values(plugin=PLUGIN_NAME,
                            type_instance="U0_lineattenuation",
                            type="gauge",
                            values=[xdslinfo.vdsl_band_lineattenuationDB_U0]
                            ).dispatch()
        if xdslinfo.vdsl_band_lineattenuationDB_U1 is not None:
            collectd.Values(plugin=PLUGIN_NAME,
                            type_instance="U1_lineattenuation",
                            type="gauge",
                            values=[xdslinfo.vdsl_band_lineattenuationDB_U1]
                            ).dispatch()
        if xdslinfo.vdsl_band_lineattenuationDB_U2 is not None:
            collectd.Values(plugin=PLUGIN_NAME,
                            type_instance="U2_lineattenuation",
                            type="gauge",
                            values=[xdslinfo.vdsl_band_lineattenuationDB_U2]
                            ).dispatch()
        if xdslinfo.vdsl_band_lineattenuationDB_U3 is not None:
            collectd.Values(plugin=PLUGIN_NAME,
                            type_instance="U3_lineattenuation",
                            type="gauge",
                            values=[xdslinfo.vdsl_band_lineattenuationDB_U3]
                            ).dispatch()
        if xdslinfo.vdsl_band_lineattenuationDB_U4 is not None:
            collectd.Values(plugin=PLUGIN_NAME,
                            type_instance="U4_lineattenuation",
                            type="gauge",
                            values=[xdslinfo.vdsl_band_lineattenuationDB_U4]
                            ).dispatch()
        if xdslinfo.vdsl_band_lineattenuationDB_D1 is not None:
            collectd.Values(plugin=PLUGIN_NAME,
                            type_instance="D1_lineattenuation",
                            type="gauge",
                            values=[xdslinfo.vdsl_band_lineattenuationDB_D1]
                            ).dispatch()
        if xdslinfo.vdsl_band_lineattenuationDB_D2 is not None:
            collectd.Values(plugin=PLUGIN_NAME,
                            type_instance="D2_lineattenuation",
                            type="gauge",
                            values=[xdslinfo.vdsl_band_lineattenuationDB_D2]
                            ).dispatch()
        if xdslinfo.vdsl_band_lineattenuationDB_D3 is not None:
            collectd.Values(plugin=PLUGIN_NAME,
                            type_instance="D3_lineattenuation",
                            type="gauge",
                            values=[xdslinfo.vdsl_band_lineattenuationDB_D3]
                            ).dispatch()

        # Signal Attenuation(dB)
        if xdslinfo.vdsl_band_signalattenuationDB_U0 is not None:
            collectd.Values(plugin=PLUGIN_NAME,
                            type_instance="U0_signalattenuation",
                            type="gauge",
                            values=[xdslinfo.vdsl_band_signalattenuationDB_U0]
                            ).dispatch()
        if xdslinfo.vdsl_band_signalattenuationDB_U1 is not None:
            collectd.Values(plugin=PLUGIN_NAME,
                            type_instance="U1_signalattenuation",
                            type="gauge",
                            values=[xdslinfo.vdsl_band_signalattenuationDB_U1]
                            ).dispatch()
        if xdslinfo.vdsl_band_signalattenuationDB_U2 is not None:
            collectd.Values(plugin=PLUGIN_NAME,
                            type_instance="U2_signalattenuation",
                            type="gauge",
                            values=[xdslinfo.vdsl_band_signalattenuationDB_U2]
                            ).dispatch()
        if xdslinfo.vdsl_band_signalattenuationDB_U3 is not None:
            collectd.Values(plugin=PLUGIN_NAME,
                            type_instance="U3_signalattenuation",
                            type="gauge",
                            values=[xdslinfo.vdsl_band_signalattenuationDB_U3]
                            ).dispatch()
        if xdslinfo.vdsl_band_signalattenuationDB_U4 is not None:
            collectd.Values(plugin=PLUGIN_NAME,
                            type_instance="U4_signalattenuation",
                            type="gauge",
                            values=[xdslinfo.vdsl_band_signalattenuationDB_U4]
                            ).dispatch()
        if xdslinfo.vdsl_band_signalattenuationDB_D1 is not None:
            collectd.Values(plugin=PLUGIN_NAME,
                            type_instance="D1_signalattenuation",
                            type="gauge",
                            values=[xdslinfo.vdsl_band_signalattenuationDB_D1]
                            ).dispatch()
        if xdslinfo.vdsl_band_signalattenuationDB_D2 is not None:
            collectd.Values(plugin=PLUGIN_NAME,
                            type_instance="D2_signalattenuation",
                            type="gauge",
                            values=[xdslinfo.vdsl_band_signalattenuationDB_D2]
                            ).dispatch()
        if xdslinfo.vdsl_band_signalattenuationDB_D3 is not None:
            collectd.Values(plugin=PLUGIN_NAME,
                            type_instance="D3_signalattenuation",
                            type="gauge",
                            values=[xdslinfo.vdsl_band_signalattenuationDB_D3]
                            ).dispatch()

        # SNR Margin(dB)
        if xdslinfo.vdsl_band_snrMargin_U0 is not None:
            collectd.Values(plugin=PLUGIN_NAME,
                            type_instance="U0_snrMargin",
                            type="gauge",
                            values=[xdslinfo.vdsl_band_snrMargin_U0]
                            ).dispatch()
        if xdslinfo.vdsl_band_snrMargin_U1 is not None:
            collectd.Values(plugin=PLUGIN_NAME,
                            type_instance="U1_snrMargin",
                            type="gauge",
                            values=[xdslinfo.vdsl_band_snrMargin_U1]
                            ).dispatch()
        if xdslinfo.vdsl_band_snrMargin_U2 is not None:
            collectd.Values(plugin=PLUGIN_NAME,
                            type_instance="U2_snrMargin",
                            type="gauge",
                            values=[xdslinfo.vdsl_band_snrMargin_U2]
                            ).dispatch()
        if xdslinfo.vdsl_band_snrMargin_U3 is not None:
            collectd.Values(plugin=PLUGIN_NAME,
                            type_instance="U3_snrMargin",
                            type="gauge",
                            values=[xdslinfo.vdsl_band_snrMargin_U3]
                            ).dispatch()
        if xdslinfo.vdsl_band_snrMargin_U4 is not None:
            collectd.Values(plugin=PLUGIN_NAME,
                            type_instance="U4_snrMargin",
                            type="gauge",
                            values=[xdslinfo.vdsl_band_snrMargin_U4]
                            ).dispatch()
        if xdslinfo.vdsl_band_snrMargin_D1 is not None:
            collectd.Values(plugin=PLUGIN_NAME,
                            type_instance="D1_snrMargin",
                            type="gauge",
                            values=[xdslinfo.vdsl_band_snrMargin_D1]
                            ).dispatch()
        if xdslinfo.vdsl_band_snrMargin_D2 is not None:
            collectd.Values(plugin=PLUGIN_NAME,
                            type_instance="D2_snrMargin",
                            type="gauge",
                            values=[xdslinfo.vdsl_band_snrMargin_D2]
                            ).dispatch()
        if xdslinfo.vdsl_band_snrMargin_D3 is not None:
            collectd.Values(plugin=PLUGIN_NAME,
                            type_instance="D3_snrMargin",
                            type="gauge",
                            values=[xdslinfo.vdsl_band_snrMargin_D3]
                            ).dispatch()

        # TX Power(dBm)
        if xdslinfo.vdsl_band_txPower_U0 is not None:
            collectd.Values(plugin=PLUGIN_NAME,
                            type_instance="U0_txPower",
                            type="gauge",
                            values=[xdslinfo.vdsl_band_txPower_U0]
                            ).dispatch()
        if xdslinfo.vdsl_band_txPower_U1 is not None:
            collectd.Values(plugin=PLUGIN_NAME,
                            type_instance="U1_txPower",
                            type="gauge",
                            values=[xdslinfo.vdsl_band_txPower_U1]
                            ).dispatch()
        if xdslinfo.vdsl_band_txPower_U2 is not None:
            collectd.Values(plugin=PLUGIN_NAME,
                            type_instance="U2_txPower",
                            type="gauge",
                            values=[xdslinfo.vdsl_band_txPower_U2]
                            ).dispatch()
        if xdslinfo.vdsl_band_txPower_U3 is not None:
            collectd.Values(plugin=PLUGIN_NAME,
                            type_instance="U3_txPower",
                            type="gauge",
                            values=[xdslinfo.vdsl_band_txPower_U3]
                            ).dispatch()
        if xdslinfo.vdsl_band_txPower_U4 is not None:
            collectd.Values(plugin=PLUGIN_NAME,
                            type_instance="U4_txPower",
                            type="gauge",
                            values=[xdslinfo.vdsl_band_txPower_U4]
                            ).dispatch()
        if xdslinfo.vdsl_band_txPower_D1 is not None:
            collectd.Values(plugin=PLUGIN_NAME,
                            type_instance="D1_txPower",
                            type="gauge",
                            values=[xdslinfo.vdsl_band_txPower_D1]
                            ).dispatch()
        if xdslinfo.vdsl_band_txPower_D2 is not None:
            collectd.Values(plugin=PLUGIN_NAME,
                            type_instance="D2_txPower",
                            type="gauge",
                            values=[xdslinfo.vdsl_band_txPower_D2]
                            ).dispatch()
        if xdslinfo.vdsl_band_txPower_D3 is not None:
            collectd.Values(plugin=PLUGIN_NAME,
                            type_instance="D3_txPower",
                            type="gauge",
                            values=[xdslinfo.vdsl_band_txPower_D3]
                            ).dispatch()
    else:
        print(xdslinfo)


if __name__ != "__main__":
    # when running inside plugin register each callback
    collectd.register_config(callback_configure)
    collectd.register_init(init)
    collectd.register_shutdown(shutdown)
    collectd.register_read(read)
else:
    # outside plugin just collect the info
    params['url'] = os.environ.get('URL')
    params['user'] = os.environ.get('USER')
    params['password'] = os.environ.get('PASSWORD')
    read()
    if len(sys.argv) < 2:
        while True:
            time.sleep(10)
            read()
