import collectd
import requests
from xdslInfo import XdslInfo
from bs4 import BeautifulSoup

loginpath = "/login/login-page.cgi"
dslpath = "/pages/systemMonitoring/xdslStatistics/xdslStatistics.html"
xdslinfo = XdslInfo()


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


