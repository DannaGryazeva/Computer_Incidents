import pygeoip
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_script import Base, IP
import matplotlib.pylab as plt
from mpl_toolkits.basemap import Basemap
import numpy as np
import os


def save(name='', fmt='png'):
    pwd = os.getcwd()
    ipath = './static'
    if not os.path.exists(ipath):
        os.mkdir(ipath)
    os.chdir(ipath)
    plt.savefig('{}.{}'.format(name, fmt), fmt='png')
    os.chdir(pwd)


def plot_map(session):

    rows = session.query(IP.ip)
    lat = []
    lon = []
    for row in rows:
        g = pygeoip.GeoIP('GeoLiteCity.dat')
        try:
            lat.append(g.record_by_addr(str(row.ip))['latitude'])
            lon.append(g.record_by_addr(str(row.ip))['longitude'])
        except (TypeError, AttributeError):
            continue
    m = Basemap(projection='moll',lon_0=0,resolution='l')

    x, y = m(lon, lat)

    m.drawcoastlines()
    m.fillcontinents(color='g',lake_color='#d0fefe')
    m.drawparallels(np.arange(-90.,120.,30.))
    m.drawmeridians(np.arange(0.,420.,60.))
    m.drawmapboundary(fill_color='#d0fefe')
    m.scatter(x, y, 20, marker='o', color='r')
    save(name='pic_1', fmt='png')
    plt.show()

if __name__ == "__main__":
    engine = create_engine('sqlite:///DBMaliciousURL.db', echo=False)
    Base.metadata.bind = engine
    Session = sessionmaker(bind=engine)
    session = Session()
    plot_map(session)
    session.close()
