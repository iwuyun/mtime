# -*- coding: utf-8 -*-

import MySQLdb

star_info_list = [
    'biography',
    'name',
    'english_name',
    'profession',
    'zodiac',
    'gender',
    'height',
    'weight',
    'blood_group',
    'birthday',
    'birthplace',
    'relationship',
]


class Star(object):
    def __init__(self):
        self.info = []
        info_list = self.info
        self.name = None
        info_list.append(self.name)
        self.english_name = None
        info_list.append(self.english_name)
        self.profession = None
        info_list.append(self.profession)
        self.zodiac = None
        info_list.append(self.zodiac)
        self.gender = None
        info_list.append(gender)
        self.height = None
        info_list.append(self.height)
        self.weight = None
        info_list.append(self.weight)
        self.blood_group = None
        info_list.append(self.blood_group)
        self.birthday = None
        info_list.append(self.birthday)
        self.birthplace = None
        info_list.append(self.birthplace)
        self.biography = None
        info_list.append(self.biography)
        self.relationship = None
        info_list.append(self.relationship)

    def save_star_info(self, connection_wrapper):
        info_list = []
        for item in self.info:
            if item is not None and isinstance(item, (unicode, str)):
                item = MySQLdb.escape_string(item)
            info_list.append(item)
        connection_wrapper.insert_row(info_list)
