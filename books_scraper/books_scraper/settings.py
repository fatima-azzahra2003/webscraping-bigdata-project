BOT_NAME = "books_scraper"

SPIDER_MODULES = ["books_scraper.spiders"]
NEWSPIDER_MODULE = "books_scraper.spiders"

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    "books_scraper.pipelines.MongoPipeline": 300,
}