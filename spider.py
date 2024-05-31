import scrapy

class FirstscraperSpider(scrapy.Spider):
    name = "firstscraper"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/List_of_freshwater_aquarium_fish_species"]

    def parse(self, response):
        for row in response.css("table.wikitable tbody tr")[1:]:  # Skips the header
            cells = row.css("td")
            
            common_name = cells[0].css("::text").get(default='').strip() if len(cells) > 0 else ''
            scientific_name = cells[1].css("::text").get(default='').strip() if len(cells) > 1 else ''
            size = cells[3].css("::text").get(default='').strip() if len(cells) > 3 else ''
            remarks = cells[4].css("::text").get(default='').strip() if len(cells) > 4 else ''
            tank_size = cells[5].css("::text").get(default='').strip() if len(cells) > 5 else ''
            temperature_range = cells[6].css("::text").get(default='').strip() if len(cells) > 6 else ''
            ph_range = cells[7].css("::text").get(default='').strip() if len(cells) > 7 else ''

            yield {
                "common_name": common_name,
                "scientific_name": scientific_name,
                "size": size,
                "remarks": remarks,
                "tank_size": tank_size,
                "temperature_range": temperature_range,
                "ph_range": ph_range,
            }

#run with 
#scrapy crawl firstscraper -o fish_data.json