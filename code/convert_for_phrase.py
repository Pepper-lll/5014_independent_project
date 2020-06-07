#!/usr/bin/env python
# coding: utf-8

import pickle

data = pickle.load(open('content_len10.pkl', 'rb'))


def all_Chinese(s):
    for c in s:
        if ((c >= u'\u0041' and c<=u'\u005a') or (c >= u'\u0061' and c <=u'\u007a')):
            return False
    return True


def is_letter(c):
    if ((c >= u'\u0041' and c<=u'\u005a') or (c >= u'\u0061' and c <=u'\u007a')):
        return True
    return False


result = []
for s in data:

    i = 0
    res = []
    while i<len(s):
        if is_letter(s[i]):
            start_i = i
            while i < len(s) and is_letter(s[i]):
                i += 1
            res.append(s[start_i:i])
            continue
        else:
            if s[i] != ' ':
                res.append(s[i])
            i += 1
    result.append(res)
        

 
pickle.dump(result, open('for_phrases.pkl' ,'wb'))

