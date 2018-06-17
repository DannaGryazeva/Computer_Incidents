import re
from urllib.request import Request, urlopen
from urllib.parse import urlparse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_script import Domain, Url, Base, IP
from config import *


def ip_parser(req_link, session):
    req = Request(req_link, headers=hdr)
    data = urlopen(req).read().decode('utf-8')
    find_all_ip = re.findall(example, data)
    n = 0
    new_ip = ''
    for ip in find_all_ip:
        for octet in ip:
            if n < 4:
                new_ip = new_ip + octet + "."
                n += 1
            else:
                check_ip = session.query(IP).filter(IP.ip == new_ip[0:-1]).first()
                if not check_ip:
                    new = IP(ip=new_ip[0:-1], resource=urlparse(req_link)[1])
                    session.add(new)
                    session.commit()
                n = 0
                new_ip = ''


def domain_parser(req_link, session):
    req = Request(req_link, headers=hdr)
    data = urlopen(req)
    for link in data.readlines():
        if link.decode('utf-8')[:1] != '#':
            new_dom = link.decode('utf-8')
            check_dom = session.query(Domain).filter(Domain.domain == new_dom).first()
            if not check_dom:
                new = Domain(domain=new_dom, resource=urlparse(req_link)[1])
                session.add(new)
                session.commit()


if __name__ == "__main__":
    engine = create_engine('postgresql://postgres:Keyfahtz15@localhost:5432/DBMalicious', echo=False)
    Base.metadata.bind = engine
    Session = sessionmaker(bind=engine)
    session = Session()


