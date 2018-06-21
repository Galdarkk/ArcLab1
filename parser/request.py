import urllib3
import certifi

https = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())


def read_links(links):
    return list(map(
        lambda link:
            https.request('GET', link).data.decode('utf8', 'replace')
            if link != 'https://www.pravda.com.ua/rss/view_news/'
            else https.request('GET', link).data.decode('windows-1251', 'replace')
        , links
    ))
