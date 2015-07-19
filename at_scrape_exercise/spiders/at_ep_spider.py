from scrapy import Spider, Selector

from at_api.models import Episode, Character
import django
from datetime import date
django.setup()


def convert_to_utc(_str):
        months = {
            "January": 1,
            "February": 2,
            "March": 3,
            "April": 4,
            "May": 5,
            "June": 6,
            "July": 7,
            "August": 8,
            "September": 9,
            "October": 10,
            "November": 11,
            "December": 12
        }
        date_list = _str.split(" ")
        return date(int(date_list[2]), months[date_list[0]], int(date_list[1][:-1]))


class AT_Episode_Detail_Spider(Spider):
    name = "ep_detail"
    allowed_domains = ["adventuretime.wikia.com"]
    start_urls = [
        "http://adventuretime.wikia.com/wiki/Animated_short",
        "http://adventuretime.wikia.com/wiki/Slumber_Party_Panic",
        "http://adventuretime.wikia.com/wiki/Jermaine_(episode)",
        "http://adventuretime.wikia.com/wiki/Loyalty_to_the_King",
        "http://adventuretime.wikia.com/wiki/James_(episode)",
        "http://adventuretime.wikia.com/wiki/Another_Five_More_Short_Graybles",
        "http://adventuretime.wikia.com/wiki/It_Came_from_the_Nightosphere",
        "http://adventuretime.wikia.com/wiki/Wizards_Only,_Fools",
    ]
    # start_urls = [url.strip() for url in characters.readlines()]

    def parse(self, response):
        sel = Selector(response)
        data = sel.xpath("//table[@class='infobox']")
        title = sel.xpath("//header[@id='WikiaPageHeader']//h1/text()").extract()[0].strip()
        print "===================NAME======================"
        title = title.replace(" (episode)", "")
        print title

        season_episode_str = data.xpath("normalize-space(tr[2]/td[1]/text())").extract()[0]
        season_id = season_episode_str.split("Season ", 1)[1].rpartition(",")[0]
        episode_id = season_episode_str.split("episode ", 1)[1]
        title_card = data.xpath("tr[2]/td/div/div/a/@href").extract()[0]
        production_code = data.xpath("normalize-space(tr[3]/td/text())").extract()[0]
        air_date = data.xpath("normalize-space(tr[4]/td/text())").extract()[0]
        air_date_utc = convert_to_utc(air_date)
        e, e_created = Episode.objects.get_or_create(title=title,
                                                     season_id=season_id,
                                                     episode_id=episode_id,
                                                     title_card=title_card,
                                                     production_code=production_code,
                                                     air_date=air_date,
                                                     air_date_utc=air_date_utc)

        # Note for characters. Towards the end, there is /a[1].The [1] is there because I only want the first link.
        # Sometimes something like Hunson Abadeer (name not revealed until "Return to the Nightosphere") will appear.
        # Both Hunson Abadeer and Return ... will be a tags, but Return is obviously not a character.
        characters = sel.xpath("//div[@id='mw-content-text']/*[self::h3 or self::h2][span[@id='Major_characters' or @id='Minor_characters']]/following-sibling::*[1]/li/a[1]/text() | "
                               "//div[@id='mw-content-text']/*[self::h3 or self::h2][span[@id='Major_characters' or @id='Minor_characters']]/following-sibling::*[1]/li/ul/li/a[1]/text()").extract()
        for char in characters:
            c, c_created = Character.objects.get_or_create(name=char)
            e.characters.add(c)
        print title_card
        print production_code
        print air_date
        print air_date_utc
        print characters
