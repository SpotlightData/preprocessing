'''text preprocessing module for the preprocessing package'''

import html
from os import environ, path
import re
import string

import nltk
nltk.data.path=[path.join(path.dirname(__file__), "data")]
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer


PUNCT = string.punctuation
STOPWORDS = stopwords.words("english")
TOKENIZER = RegexpTokenizer(r'\b[\w.\/,-]+\b|[-.,\/()]')


#error handles
class Error(Exception):
    '''base error handle'''
    pass

class FunctionError(Error):
    '''error handle for incorrect functions passed as arguments'''
    pass

class InputError(Error):
    '''error handle for incorrect function arguments'''
    pass


#functions
def convert_html_entities(text_string):
    '''returns string with converted html entities'''
    if text_string is None or text_string == "":
        return ""
    elif isinstance(text_string, str):
        return html.unescape(text_string)
    else:
        raise InputError("string not passed as argument")

def keyword_tokenize(text_string):
    '''returns string comprised of only the keywords for the input text'''
    if text_string is None or text_string == "":
        return ""
    elif isinstance(text_string, str):
        return " ".join([word for word in TOKENIZER.tokenize(text_string) if word not in STOPWORDS and len(word) >= 3])
    else:
        raise InputError("string not passed as argument")

def lowercase(text_string):
    '''returns string in lowercase'''
    if text_string is None or text_string == "":
        return ""
    elif isinstance(text_string, str):
        return text_string.lower()
    else:
        raise InputError("string not passed as argument")

def preprocess_text(text_string, function_list):
    '''returns preprocessed text, performing functions in order of appearance in
    list'''
    if isinstance(text_string, str):
        if isinstance(function_list, list):
            for func in function_list:
                try:
                    text_string = func(text_string)
                except (NameError, TypeError):
                    raise FunctionError("invalid function passed as element of function_list")
                except:
                    raise
            return text_string
        else:
            raise InputError("list of functions not passed as argument for function_list")
    else:
        raise InputError("string not as argument for text_string")

def remove_esc_chars(text_string):
    '''returns text string without escape characters'''
    if text_string is None or text_string == "":
        return ""
    elif isinstance(text_string, str):
        return " ".join(re.sub(r'\\\w', "", text_string).split())
    else:
        raise InputError("string not passed as argument")

def remove_numbers(text_string):
    '''returns text without numbers'''
    if text_string is None or text_string == "":
        return ""
    elif isinstance(text_string, str):
        return " ".join(re.sub(r'\b[\d.\/,]+', "", text_string).split())
    else:
        raise InputError("string not passed as argument")

def remove_non_bound_punct(text_string):
    '''returns string without non word boundary punctuation'''
    if text_string is None or text_string == "":
        return ""
    elif isinstance(text_string, str):
        return " ".join(re.sub(r'\B['+PUNCT+r']', "", text_string).split())
    else:
        raise InputError("string not passed as argument")

def remove_urls(text_string):
    '''returns text string without urls'''
    if text_string is None or text_string == "":
        return ""
    elif isinstance(text_string, str):
        return " ".join(re.sub(r'http\S+', "", text_string).split())
    else:
        raise InputError("string not passed as argument")
