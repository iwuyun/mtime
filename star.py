# -*- coding: utf-8 -*-

import MySQLdb

star_info_list = [
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
    'biography',
]


class Star(object):
    def __init__(self):
        self.info = {}
        self.name = None
        self.english_name = None
        self.profession = None
        self.zodiac = None
        self.gender = 'male'
        self.height = None
        self.weight = None
        self.blood_group = None
        self.birthday = None
        self.birthplace = None
        self.biography = None
        self.relationship = None

    def update_info(self):
        self.info.update({'name': self.name})
        self.info.update({'english_name': self.english_name})
        self.info.update({'profession': self.profession})
        self.info.update({'zodiac': self.zodiac})
        self.info.update({'gender': self.gender})
        self.info.update({'height': self.height})
        self.info.update({'weight': self.weight})
        self.info.update({'blood_group': self.blood_group})
        self.info.update({'birthday': self.birthday})
        self.info.update({'birthplace': self.birthday})
        self.info.update({'biography': self.biography})
        self.info.update({'relationship': self.relationship})

    def save_star_info(self, connection_wrapper):
        info_list = []
        for key in star_info_list:
            item = self.info[key]
            if item is None:
                item = 'null'
            elif isinstance(item, unicode):
                item = '"{}"'.format(MySQLdb.escape_string(item.encode('utf8')))
            elif isinstance(item, str):
                item = '"{}"'.format(MySQLdb.escape_string(item))
            info_list.append(item)
        connection_wrapper.insert_row(info_list)
