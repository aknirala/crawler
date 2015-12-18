#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os
import string


def remove_punctuations(word):
    return str(word).translate(None, string.punctuation)


def main():
    data_dir = 'data'
    file_list = [_file for _file in os.listdir(data_dir) if _file.endswith('.json')]
    for _file in file_list:
        with open(os.path.join(data_dir, _file)) as json_file:
            json_data = json.load(json_file)
            for article_year in json_data:
                for article in article_year:
                    print article['date']
                    break

main()
