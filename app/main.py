from fastapi import FastAPI, Response
from .feeds import get_cs_feed

app = FastAPI()

@app.get("/uni/news-and-announcements")
def news_and_announcements() -> Response:
    return Response(content=get_cs_feed(), media_type="application/rss+xml", charset="utf-8")
