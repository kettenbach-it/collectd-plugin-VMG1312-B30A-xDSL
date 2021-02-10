import re
import datetime


class XdslInfo:
    raw: str

    vdsl_trainingstatus: str
    vdsl_mode: str
    vdsl_profile: str
    vdsl_gvector: bool
    vdsl_traffictype: str
    vdsl_linkuptime_str: str
    vdsl_linkuptime_timedelta: datetime.timedelta

    vdsl_upstream_linerateMbps: float
    vdsl_upstream_netdatarateMbps: float
    vdsl_upstream_trelliscoding: bool
    vdsl_upstream_snrmarginDB: float
    vdsl_upstream_actualdelayMS: float
    vdsl_upstream_transmitPowerDBm: float
    vdsl_upstream_receivePowerDBm: float
    vdsl_upstream_actualInpSymbols: float
    vdsl_upstream_totalAttenuationDB: float
    vdsl_upstream_attainableNetDataRateMbps: float

    vdsl_downstream_linerateMbps: float
    vdsl_downstream_netdatarateMbps: float
    vdsl_downstream_trelliscoding: bool
    vdsl_downstream_snrmarginDB: float
    vdsl_downstream_actualdelayMS: float
    vdsl_downstream_transmitPowerDBm: float
    vdsl_downstream_receivePowerDBm: float
    vdsl_downstream_actualInpSymbols: float
    vdsl_downstream_totalAttenuationDB: float
    vdsl_downstream_attainableNetDataRateMbps: float

    vdsl_band_lineattenuationDB_U0: float = None
    vdsl_band_signalattenuationDB_U0: float = None
    vdsl_band_snrMargin_U0: float = None
    vdsl_band_txPower_U0: float = None

    vdsl_band_lineattenuationDB_U1: float = None
    vdsl_band_signalattenuationDB_U1: float = None
    vdsl_band_snrMargin_U1: float = None
    vdsl_band_txPower_U1: float = None

    vdsl_band_lineattenuationDB_U2: float = None
    vdsl_band_signalattenuationDB_U2: float = None
    vdsl_band_snrMargin_U2: float = None
    vdsl_band_txPower_U2: float = None

    vdsl_band_lineattenuationDB_U3: float = None
    vdsl_band_signalattenuationDB_U3: float = None
    vdsl_band_snrMargin_U3: float = None
    vdsl_band_txPower_U3: float = None

    vdsl_band_lineattenuationDB_U4: float = None
    vdsl_band_signalattenuationDB_U4: float = None
    vdsl_band_snrMargin_U4: float = None
    vdsl_band_txPower_U4: float = None

    vdsl_band_lineattenuationDB_D1: float = None
    vdsl_band_signalattenuationDB_D1: float = None
    vdsl_band_snrMargin_D1: float = None
    vdsl_band_txPower_D1: float = None

    vdsl_band_lineattenuationDB_D2: float = None
    vdsl_band_signalattenuationDB_D2: float = None
    vdsl_band_snrMargin_D2: float = None
    vdsl_band_txPower_D2: float = None

    vdsl_band_lineattenuationDB_D3: float = None
    vdsl_band_signalattenuationDB_D3: float = None
    vdsl_band_snrMargin_D3: float = None
    vdsl_band_txPower_D3: float = None

    def xstr(self, s):
        if s is None:
            return 'N/A '
        else:
            return str(s)

    def __str__(self):
        out = "VDSL Training Status:       " + self.vdsl_trainingstatus
        out += "\nVDSL Mode:                  " + self.vdsl_mode
        out += "\nVDSL Profile:               " + self.vdsl_profile
        out += "\nG.Vector:                   " + str(self.vdsl_gvector)
        out += "\nTraffic Type:               " + self.vdsl_traffictype
        out += "\nLink Uptime:                " + str(self.vdsl_linkuptime_timedelta) + " (" + str(self.vdsl_linkuptime_timedelta.total_seconds()) + "s)"
        out += "\n========================================================="
        out += "\nVDSL Port Details           Upstream         Downstream"
        out += "\nLine Rate:                  " + str(self.vdsl_upstream_linerateMbps) \
               + " Mbps      " + str(self.vdsl_downstream_linerateMbps) + " Mbps"
        out += "\nActual Net Data Rate:       " + str(self.vdsl_upstream_netdatarateMbps) \
               + " Mbps      " + str(self.vdsl_downstream_netdatarateMbps) + " Mbps"
        out += "\nTrellis Coding:             " + str(self.vdsl_upstream_trelliscoding) \
               + "             " + str(self.vdsl_downstream_trelliscoding)
        out += "\nSNR Margin:                 " + str(self.vdsl_upstream_snrmarginDB) \
               + " dB           " + str(self.vdsl_downstream_snrmarginDB) + " dB"
        out += "\nActual Delay:               " + str(self.vdsl_upstream_actualdelayMS) \
               + " ms           " + str(self.vdsl_downstream_actualdelayMS) + " ms"
        out += "\nTransmit Power:             " + str(self.vdsl_upstream_transmitPowerDBm) \
               + " dBm          " + str(self.vdsl_downstream_transmitPowerDBm) + " dBm"
        out += "\nReceive Power:              " + str(self.vdsl_upstream_receivePowerDBm) \
               + " dBm         " + str(self.vdsl_downstream_receivePowerDBm) + " dBm"
        out += "\nActual INP:                 " + str(self.vdsl_upstream_actualInpSymbols) \
               + " symbols     " + str(self.vdsl_downstream_actualInpSymbols) + " symbols"
        out += "\nTotal Attenuation:          " + str(self.vdsl_upstream_totalAttenuationDB) \
               + " dB           " + str(self.vdsl_downstream_totalAttenuationDB) + " dB"
        out += "\nAttainable Net Data Rate:   " + str(self.vdsl_upstream_attainableNetDataRateMbps) \
               + " Mbps      " + str(self.vdsl_downstream_attainableNetDataRateMbps) + " Mbps"
        out += "\n========================================================="
        out += "\nVDSL Band Status        U0      U1      U2      U3      U4      D1      D2      D3"
        out += "\nLine Attenuation(dB):   " + self.xstr(self.vdsl_band_lineattenuationDB_U0) + "     " \
               + self.xstr(self.vdsl_band_lineattenuationDB_U1) + "    " \
               + self.xstr(self.vdsl_band_lineattenuationDB_U2) + "    " \
               + self.xstr(self.vdsl_band_lineattenuationDB_U3) + "    " \
               + self.xstr(self.vdsl_band_lineattenuationDB_U4) + "    " \
               + self.xstr(self.vdsl_band_lineattenuationDB_D1) + "    " \
               + self.xstr(self.vdsl_band_lineattenuationDB_D2) + "    " \
               + self.xstr(self.vdsl_band_lineattenuationDB_D3) + "    "
        out += "\nSignal Attenuation(dB): " + self.xstr(self.vdsl_band_signalattenuationDB_U0) + "     " \
               + self.xstr(self.vdsl_band_signalattenuationDB_U1) + "    " \
               + self.xstr(self.vdsl_band_signalattenuationDB_U2) + "    " \
               + self.xstr(self.vdsl_band_signalattenuationDB_U3) + "    " \
               + self.xstr(self.vdsl_band_signalattenuationDB_U4) + "    " \
               + self.xstr(self.vdsl_band_signalattenuationDB_D1) + "    " \
               + self.xstr(self.vdsl_band_signalattenuationDB_D2) + "    " \
               + self.xstr(self.vdsl_band_signalattenuationDB_D3) + "    "
        out += "\nSNR Margin(dB):         " + self.xstr(self.vdsl_band_snrMargin_U0) + "     " \
               + self.xstr(self.vdsl_band_snrMargin_U1) + "      " \
               + self.xstr(self.vdsl_band_snrMargin_U2) + "     " \
               + self.xstr(self.vdsl_band_snrMargin_U3) + "     " \
               + self.xstr(self.vdsl_band_snrMargin_U4) + "    " \
               + self.xstr(self.vdsl_band_snrMargin_D1) + "    " \
               + self.xstr(self.vdsl_band_snrMargin_D2) + "    " \
               + self.xstr(self.vdsl_band_snrMargin_D3) + "    "
        out += "\nTX Power(dBm):         " + self.xstr(self.vdsl_band_txPower_U0) + "     " \
               + self.xstr(self.vdsl_band_txPower_U1) + "    " \
               + self.xstr(self.vdsl_band_txPower_U2) + "    " \
               + self.xstr(self.vdsl_band_txPower_U3) + "    " \
               + self.xstr(self.vdsl_band_txPower_U4) + "    " \
               + self.xstr(self.vdsl_band_txPower_D1) + "    " \
               + self.xstr(self.vdsl_band_txPower_D2) + "    " \
               + self.xstr(self.vdsl_band_txPower_D3) + "    "
        return out

    def parse(self, input_str: str):
        self.raw = input_str

        # https://regex101.com/r/ar6kj3/1
        self.vdsl_trainingstatus = re.search(r"VDSL Training Status: (.*)\n", input_str).group(1).strip()
        self.vdsl_mode = re.search(r"Mode: (.*)\n", input_str).group(1).strip()
        self.vdsl_profile = re.search(r"VDSL Profile: (.*)\n", input_str).group(1).strip()
        gvector = re.search(r"G.Vector: (.*)\n", input_str).group(1).strip()
        if gvector == "Enable":
            self.vdsl_gvector = True
        else:
            self.vdsl_gvector = False
        self.vdsl_traffictype = re.search(r"Traffic Type: (.*)\n", input_str).group(1).strip()
        self.vdsl_linkuptime_str = re.search(r"Link Uptime: (.*)\n", input_str).group(1).strip()
        td = re.search(r"Link Uptime: (.*) day.*: (.*) hour.*: (.*) minute.*\n", input_str)
        self.vdsl_linkuptime_timedelta = datetime.timedelta(
            days=int(td.group(1).strip()),
            hours=int(td.group(2).strip()),
            minutes=int(td.group(3).strip())
        )

        self.vdsl_upstream_linerateMbps = float(re.search(r"Line Rate: (.*) Mbps (.*) Mbps\n", input_str).group(1))
        self.vdsl_downstream_linerateMbps = float(re.search(r"Line Rate: (.*) Mbps (.*) Mbps\n", input_str).group(2))
        self.vdsl_upstream_netdatarateMbps = float(
            re.search(r"Actual Net Data Rate: (.*) Mbps (.*) Mbps\n", input_str).group(1))
        self.vdsl_downstream_netdatarateMbps = float(
            re.search(r"Actual Net Data Rate: (.*) Mbps (.*) Mbps\n", input_str).group(2))
        trellis = re.search(r"Trellis Coding:.*(\S{2}).*(\S{2})\n", input_str)
        if trellis.group(1) == "ON":
            self.vdsl_upstream_trelliscoding = True
        else:
            self.vdsl_upstream_trelliscoding = False
        if trellis.group(2) == "ON":
            self.vdsl_downstream_trelliscoding = True
        else:
            self.vdsl_downstream_trelliscoding = False
        self.vdsl_upstream_snrmarginDB = float(re.search(r"SNR Margin: (.*) dB (.*) dB\n", input_str).group(1))
        self.vdsl_downstream_snrmarginDB = float(re.search(r"SNR Margin: (.*) dB (.*) dB\n", input_str).group(2))
        self.vdsl_upstream_actualdelayMS = float(re.search(r"Actual Delay: (.*) ms (.*) ms\n", input_str).group(1))
        self.vdsl_downstream_actualdelayMS = float(re.search(r"Actual Delay: (.*) ms (.*) ms\n", input_str).group(2))
        self.vdsl_upstream_transmitPowerDBm = float(
            re.search(r"Transmit Power: (.*) dBm (.*) dBm\n", input_str).group(1))
        self.vdsl_downstream_transmitPowerDBm = float(
            re.search(r"Transmit Power: (.*) dBm (.*) dBm\n", input_str).group(2))
        self.vdsl_upstream_receivePowerDBm = float(re.search(r"Receive Power: (.*) dBm (.*) dBm\n", input_str).group(1))
        self.vdsl_downstream_receivePowerDBm = float(
            re.search(r"Receive Power: (.*) dBm (.*) dBm\n", input_str).group(2))
        self.vdsl_upstream_actualInpSymbols = float(re.search(r"Actual INP: (.*) symbols (.*) symbols\n", input_str).group(1))
        self.vdsl_downstream_actualInpSymbols = float(
            re.search(r"Actual INP: (.*) symbols (.*) symbols\n", input_str).group(2))
        self.vdsl_upstream_totalAttenuationDB = float(re.search(r"Total Attenuation: (.*) dB (.*) dB\n", input_str).group(1))
        self.vdsl_downstream_totalAttenuationDB = float(
            re.search(r"Total Attenuation: (.*) dB (.*) dB\n", input_str).group(2))
        self.vdsl_upstream_attainableNetDataRateMbps = float(re.search(r"Attainable Net Data Rate: (.*) Mbps (.*) Mbps\n", input_str).group(1))
        self.vdsl_downstream_attainableNetDataRateMbps = float(
            re.search(r"Attainable Net Data Rate: (.*) Mbps (.*) Mbps\n", input_str).group(2))

        lineAttenuation = re.search(r"Line Attenuation\(dB\):\t(.*)\t(.*)\t(.*)\t(.*)\t(.*)\t(.*)\t(.*)\t(.*)\t\n", input_str)
        if lineAttenuation.group(1).strip() != "N/A":
            self.vdsl_band_lineattenuationDB_U0 = float(lineAttenuation.group(1).strip())
        if lineAttenuation.group(2).strip() != "N/A":
            self.vdsl_band_lineattenuationDB_U1 = float(lineAttenuation.group(2).strip())
        if lineAttenuation.group(3).strip() != "N/A":
            self.vdsl_band_lineattenuationDB_U2 = float(lineAttenuation.group(3).strip())
        if lineAttenuation.group(4).strip() != "N/A":
            self.vdsl_band_lineattenuationDB_U3 = float(lineAttenuation.group(4).strip())
        if lineAttenuation.group(5).strip() != "N/A":
            self.vdsl_band_lineattenuationDB_U4 = float(lineAttenuation.group(5).strip())
        if lineAttenuation.group(6).strip() != "N/A":
            self.vdsl_band_lineattenuationDB_D1 = float(lineAttenuation.group(6).strip())
        if lineAttenuation.group(7).strip() != "N/A":
            self.vdsl_band_lineattenuationDB_D2 = float(lineAttenuation.group(7).strip())
        if lineAttenuation.group(8).strip() != "N/A":
            self.vdsl_band_lineattenuationDB_D3 = float(lineAttenuation.group(8).strip())

        signalAttenuation = re.search(
            r"Signal Attenuation\(dB\):\t(.*)\t(.*)\t(.*)\t(.*)\t(.*)\t(.*)\t(.*)\t(.*)\t\n", input_str)
        if signalAttenuation.group(1).strip() != "N/A":
            self.vdsl_band_signalattenuationDB_U0 = float(signalAttenuation.group(1).strip())
        if signalAttenuation.group(2).strip() != "N/A":
            self.vdsl_band_signalattenuationDB_U1 = float(signalAttenuation.group(2).strip())
        if signalAttenuation.group(3).strip() != "N/A":
            self.vdsl_band_signalattenuationDB_U2 = float(signalAttenuation.group(3).strip())
        if signalAttenuation.group(4).strip() != "N/A":
            self.vdsl_band_signalattenuationDB_U3 = float(signalAttenuation.group(4).strip())
        if signalAttenuation.group(5).strip() != "N/A":
            self.vdsl_band_signalattenuationDB_U4 = float(signalAttenuation.group(5).strip())
        if signalAttenuation.group(6).strip() != "N/A":
            self.vdsl_band_signalattenuationDB_D1 = float(signalAttenuation.group(6).strip())
        if signalAttenuation.group(7).strip() != "N/A":
            self.vdsl_band_signalattenuationDB_D2 = float(signalAttenuation.group(7).strip())
        if signalAttenuation.group(8).strip() != "N/A":
            self.vdsl_band_signalattenuationDB_D3 = float(signalAttenuation.group(8).strip())

        snrMargin = re.search(
            r"SNR Margin\(dB\):\t(.*)\t(.*)\t(.*)\t(.*)\t(.*)\t(.*)\t(.*)\t(.*)\t\n", input_str)
        if snrMargin.group(1).strip() != "N/A":
            self.vdsl_band_snrMargin_U0 = float(snrMargin.group(1).strip())
        if snrMargin.group(2).strip() != "N/A":
            self.vdsl_band_snrMargin_U1 = float(snrMargin.group(2).strip())
        if snrMargin.group(3).strip() != "N/A":
            self.vdsl_band_snrMargin_U2 = float(snrMargin.group(3).strip())
        if snrMargin.group(4).strip() != "N/A":
            self.vdsl_band_snrMargin_U3 = float(snrMargin.group(4).strip())
        if snrMargin.group(5).strip() != "N/A":
            self.vdsl_band_snrMargin_U4 = float(snrMargin.group(5).strip())
        if snrMargin.group(6).strip() != "N/A":
            self.vdsl_band_snrMargin_D1 = float(snrMargin.group(6).strip())
        if snrMargin.group(7).strip() != "N/A":
            self.vdsl_band_snrMargin_D2 = float(snrMargin.group(7).strip())
        if snrMargin.group(8).strip() != "N/A":
            self.vdsl_band_snrMargin_D3 = float(snrMargin.group(8).strip())
            
        txPower = re.search(
            r"TX Power\(dBm\):\t(.*)\t(.*)\t(.*)\t(.*)\t(.*)\t(.*)\t(.*)\t(.*)\t\n", input_str)
        if txPower.group(1).strip() != "N/A":
            self.vdsl_band_txPower_U0 = float(txPower.group(1).strip())
        if txPower.group(2).strip() != "N/A":
            self.vdsl_band_txPower_U1 = float(txPower.group(2).strip())
        if txPower.group(3).strip() != "N/A":
            self.vdsl_band_txPower_U2 = float(txPower.group(3).strip())
        if txPower.group(4).strip() != "N/A":
            self.vdsl_band_txPower_U3 = float(txPower.group(4).strip())
        if txPower.group(5).strip() != "N/A":
            self.vdsl_band_txPower_U4 = float(txPower.group(5).strip())
        if txPower.group(6).strip() != "N/A":
            self.vdsl_band_txPower_D1 = float(txPower.group(6).strip())
        if txPower.group(7).strip() != "N/A":
            self.vdsl_band_txPower_D2 = float(txPower.group(7).strip())
        if txPower.group(8).strip() != "N/A":
            self.vdsl_band_txPower_D3 = float(txPower.group(8).strip())
