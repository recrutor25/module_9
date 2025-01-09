#!/home/igor/PycharmProjects/module_9/.venv/bin/python
# -*- coding: utf-8 -*-

def all_variants(text):
   for i in range(1, len(text) + 1):
        for j in range(len(text) +1 - i):
            yield text[j:j + i]


a = all_variants("abcd")
for i in a:
    print(i)