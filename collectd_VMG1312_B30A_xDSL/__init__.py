try:
    import collectd
except:
    pass
import requests
from xdslInfo import XdslInfo
from bs4 import BeautifulSoup

loginpath = "/login/login-page.cgi"
dslpath = "/pages/systemMonitoring/xdslStatistics/xdslStatistics.html"
xdslinfo = XdslInfo()
params = {}


def getXDSLStats(host, user, password):
    # Login first
    # Using session to store cookies:
    session = requests.session()
    loginrequest = session.post(host + loginpath, {
        'AuthName': user,
        'AuthPassword': password
    })

    # Get gage with xDSL Stats
    xdslrequest = session.get(host + dslpath)
    # Parse page with BS
    soup = BeautifulSoup(xdslrequest.content, 'html.parser')
    # Extract text-object and prase with XdslInfo
    xdslinfo.parse(soup.find(id='VdslInfoDisplay').text)


def printDSLStats():
    print(xdslinfo)


def callback_configure(config):
    """ Configure callback """
    for node in config.children:
        if node.key == 'URL':
            params['url'] = node.values[0]
        elif node.key == 'User':
            params['user'] = node.values[0]
        elif node.key == 'Password':
            params['password'] = node.values[0]
        elif node.key == 'Verbose':
            params['verbose'] = node.values[0]
        else:
            collectd.warning('fritzcollectd: Unknown config %s' % node.key)


def read():
    pass


try:
    collectd.register_config(callback_configure)
    collectd.register_read(read)
except:
    pass
