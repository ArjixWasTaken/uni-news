from datetime import datetime
import textwrap
import httpx

client = httpx.Client(headers={"User-Agent": "rss-spider/1.0"}, verify=False)

GENERAL_FEED = "https://cs.unipi.gr/wp-json/wp/v2/posts?category=7314"


def get_cs_feed():
    feed = client.get(GENERAL_FEED).json()

    items = "\n".join([
        f"""\
    <item>
        <title>{x["title"]["rendered"]}</title>
        <link>{x["link"]}</link>
        <description>
            <![CDATA[\n{textwrap.indent(x["content"]["rendered"], 16*' ')}
            ]]>
        </description>
        <pubDate>{datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S').strftime('%a, %d %b %Y %H:%M:%S')}</pubDate>
    </item>
    """
        for x in feed
    ])

    return f"""\
<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">

<channel>
<title>cs.unipi.gr - News and Announcements</title>
<link>https://feed.arjix.dev/uni/news-and-announcements</link>
<description>Made by https://github.com/ArjixWasTaken</description>
{items}
</channel>
</rss>
"""
