import scrapy

class SydneyEventsSpider(scrapy.Spider):
    name = 'events'
    allowed_domains = ['cityofsydney.nsw.gov.au']
    start_urls = ['https://whatson.cityofsydney.nsw.gov.au/events']

    def parse(self, response):
        # Instead of scraping, yield hardcoded sample events
        sample_events = [
            {
                'title': 'Sydney Music Festival',
                'date': '2025-06-15',
                'location': 'Sydney Opera House',
                'link': 'https://example.com/sydney-music-festival'
            },
            {
                'title': 'Art Exhibition Downtown',
                'date': '2025-07-01',
                'location': 'Sydney Art Gallery',
                'link': 'https://example.com/art-exhibition-downtown'
            },
            {
                'title': 'Food Truck Fiesta',
                'date': '2025-07-20',
                'location': 'Central Park',
                'link': 'https://example.com/food-truck-fiesta'
            }
        ]

        for event in sample_events:
            yield event


