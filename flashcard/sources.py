import re
import requests
from urllib.parse import urlparse
from typing import Tuple

from flashcard.property import Flashcard


def fetch_google_spreadsheet(url: str, fmt="tsv") -> Flashcard:
    """ Obtain flashcard data from Google Speradsheet

    :param url:
    :param fmt:
    :return:
    """

    assert url.startswith("https://docs.google.com/spreadsheets/"), \
        "URL should start with https://docs.google.com/spreadsheets/"
    assert fmt == "tsv" or fmt == "csv"

    # set delimiter
    delimiter = ""
    if fmt == "tsv":
        delimiter = "\t"
    if fmt == "csv":
        delimiter = ","

    # generate downloadable url
    _id, gid = _parse_google_spreadsheet(url)
    downloadable_url = _generate_downloadable_url(_id, gid, fmt)

    # set parameter in order to fetch dat in appropriate format
    r = requests.get(downloadable_url)
    r.encoding = 'utf-8'

    ret = []
    for row in r.text.split("\n"):
        ret.append([e.strip("\r").strip() for e in row.split(delimiter)])

    return ret


def _parse_google_spreadsheet(url: str) -> Tuple[str, str]:
    """ Parse id and gid from url of Google Spreadsheet

    :param url:
    :return:
    """

    o = urlparse(url)
    path = o.path  # e.g., '/spreadsheets/d/3bHXt4ZY0S54RU6EeT7eHGh_KAI9ncdn96KTh-Hx0xGe/edit'
    fragment = o.fragment  # e.g., 'gid=742930534'

    # parse id
    _id = None
    r = re.compile('/spreadsheets/d/')
    _id = r.sub('', path)
    r = re.compile('edit.*')
    _id = r.sub('', _id)
    _id = _id.strip("/")

    # parse gid
    gid = None
    if 'gid' in fragment:
        r = re.compile('gid=[0-9]*')
        gid = r.match(fragment).group().lstrip('gid=')

    return _id, gid


def _generate_downloadable_url(_id: str, gid: str, fmt="tsv") -> str:
    """

    :param _id:
    :param gid:
    :return:
    """

    assert (_id is not None) and (_id != ""), "id is not set"

    url = "https://docs.google.com/spreadsheets/d/{}/export?".format(_id)
    if gid is None or gid == "":
        gid = "0"
    url += "gid={}&format={}".format(gid, fmt)

    return url
