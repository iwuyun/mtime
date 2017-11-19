# -*- coding: utf-8 -*-

import re

import scrapy
from scrapy.selector import Selector

from star import Star
from mysql_helper import mysql_connection_wrapper


def trim_and_encode_string(source):
    source = source.strip().encode('utf8')
    source = re.sub(r'(\s)\s+', '', source)
    return source


class MtimeSpider(scrapy.Spider):
    name = 'mtime'
    allowed_domains = ['mtime.com']
    start_urls = ['http://mtime.com/']

    def __init__(self):
        self.connection_wrapper = mysql_connection_wrapper()

    def parse(self, response):
        content = response.body
        idol = Star()
        selector = Selector(text=content)
        bio_wrapper = selector.xpath('//div[@pan="M14_Person_PersonBiography"]')
        if len(bio_wrapper):
            biography = (bio_list[0].xpath('p')[0]
                         .xpath('text()')[0].extract())
            idol.biography = trim_and_encode_string(biography)
        star_header = selector.xpath('//div[@class="per_header"]')[0]
        idol.name = star_header.xpath('h2/text()')[0].extract()
        idol.english_name = start_urls.xpath('p[@class="enname"]/text()')[0].extract()
        idol.profession = star_header.xpath('p[@pan]/text()')[0].extract()
        basic_info, born_info = selector.xpath('//dl[@pan="M14_Person_Index_PersonBasicInfo"]')
        idol.gender = basic_info.xpath('dd/i/@class')[0].extract().replace('icon_', '')
        zodiac_wrapper = basic_info.xpath('dd/a/i')
        if len(zodiac_wrapper):
            zodiac = zodiac_wrapper[0].xpath('@class')[0].extract()
            zodiac = trim_and_encode_string(zodiac)
            idol.zodiac = int(re.sub(r'(?<=icon_star)\d+', zodiac))
        blood_wrapper = basic_info.xpath('dd/div[@class="icon_blood"]/i')
        if len(blood_wrapper):
            idol.blood_group = blood_wrapper[0].xpath('text()')[0].extract()
        body_wrapper = basic_info.xpath('dd/span')
        if len(body_wrapper):
            idol.height, idol.weight = body_wrapper[0].xpath('text()').extract()
        born_wrapper = born_info.xpath('dd/text()')
        if len(birthday_wrapper):
            birthday_wrapper, birthplace = born_wrapper.extract()
            idol.birthplace = trim_and_encode_string(birthplace)
            if birthday_wrapper.strip() != '':
                idol.birthday = birthday_wrapper.strip()
        relationship_wrapper = selector.xpath('//div[@class="peo_relationship"]')
        if len(relationship_wrapper):
            idol.relationship = relationship_wrapper[0].extract().encode('utf8')
        star.save_info(self.connection_wrapper)
