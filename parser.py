import urllib.request
from urllib.parse import urlparse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_script import Domain, Url, Base
from config import *
from lxml import etree
from parser_v2 import domain_parser, ip_parser
from ip_map import plot_map


def parser():
    f = urllib.request.urlopen(request_link)
    data = f.read()
    root = etree.fromstring(data)
    for item in root.getchildren():
        for elem in item.getchildren():
            for tab in elem.getchildren():
                if tab.tag == "url":
                    text = tab.text
                    url = text
                    dom = urlparse(url)[1]
                for sub in tab.getchildren():
                    if sub.tag == "submission_time":
                        text = sub.text
                        check_domain = session.query(Domain).filter(Domain.domain == dom).first()
                        if check_domain:
                            new_domain = check_domain
                            session.commit()
                        else:
                            new_domain = Domain(domain=dom, first_seen=text, resource="PhishTank")
                            session.add(new_domain)
                            session.commit()
                        check_url = session.query(Url).filter(Url.url == url).first()
                        if not check_url:
                            new_url = Url(url=url, dom=new_domain, submission=text, resource="PhishTank")
                            session.add(new_url)
                            session.commit()
    session.close()
    f.close()


if __name__ == "__main__":
    engine = create_engine('postgresql://postgres:Keyfahtz15@localhost:5432/DBMalicious', echo=False)
    Base.metadata.bind = engine
    Session = sessionmaker(bind=engine)
    session = Session()
    parser()
    ip_parser(req_link_1, session)
    domain_parser(req_link_2, session)
    domain_parser(req_link_3, session)
    plot_map(session)
