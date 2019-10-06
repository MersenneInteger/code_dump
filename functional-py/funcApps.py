##functional applications

#implement a word counter
from itertools import groupby
import re

def split_line(lines):
    return lines.split(' ')

def convert_lower(words_list):
    return list(map(lambda x: x.lower(), words_list))

def trim_lines(lines_list):
    return list(map(lambda x: x.strip(), lines_list))

def remove_empty(words_list):
    return list(filter(lambda x: x != '', words_list))

def remove_punctuation(string):
    return re.sub(r'[^\w\s]', '',string)

def group_words(words_list):
    return groupby(sorted(words_list))

def get_word_count(grouped_words):
    return list(map(lambda x: (x[0], len(list(x[1]))), grouped_words))

string = """hello this is a string. This is a good String.
            hello world!!! """

remove_punc = remove_punctuation(string)
words_list = split_line(remove_punc)
lower_and_trim_list = trim_lines(convert_lower(words_list))
filtered_words = remove_empty(lower_and_trim_list)
grouped_word_list = group_words(filtered_words)
word_count = get_word_count(grouped_word_list)

print(word_count)

#implement a csv reader
csv_file = """ID, Designation,Name,Salary(USD)
123,Manager,John Doe, 10000
157,Engineer,Jimmy Joe,5000
190,Engineer,Alice Holmes,6000
191,Accountant,Jack Oliver,8000
200,Intern,Jessica Jones,1000
202,HR Manager, Rober Stark, 4000"""

def split_new_lines(lines):
    return lines.split('\n')

def split_delimeter(list_lines, delim=','):
    return list(map(lambda x: x.split(delim), list_lines))

def seperate_header(lines):
    return lines[0], lines[1:]

def create_row(header, data_rows):
    return list(map(lambda x:{k:v for k, v in zip(header,x)}, data_rows))

get_lines = split_new_lines(csv_file)
print('split new lines\n', get_lines)
get_rows_list = split_delimeter(get_lines)
print('get rows as a list\n', get_rows_list)
keys, values = seperate_header(get_rows_list)
print('keys\n', keys)
print('values\n', values)

employees = create_row(keys, values)
print('\nemployees: ', employees)

#word counter using multiprocessing
import multiprocessing
import time

def split_line2(lines):
    return lines.split(' ')

def convert_lower2(words_list):
    return list(map(lambda x: x.lower(), words_list))

def trim_lines2(lines_list):
    return list(map(lambda x: x.strip(), lines_list))

def remove_empty2(words_list):
    return list(filter(lambda x: x != '', words_list))

def remove_punctuation2(string):
    return re.sub(r'[^\w\s]', '',string)

def group_words2(words_list):
    return groupby(sorted(words_list))

def get_word_count2(grouped_words):
    return list(map(lambda x: (x[0], len(list(x[1]))), grouped_words))

def wordcount(text):
    remove_punc = remove_punctuation(string)
    words_list = split_line(remove_punc)
    lower_and_trim_list = trim_lines(convert_lower(words_list))
    filtered_words = remove_empty(lower_and_trim_list)
    grouped_word_list = group_words(filtered_words)
    word_count = get_word_count(grouped_word_list)
    return word_count

def time_deco(func):
    def inner_wrap(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print('Time in seconds: {0}'.format(end-start))
    return inner_wrap

big_str = ['This is a string'] * 100

@time_deco
def linear_word_count(multiple_strs):
    total_word_count = {}
    for string in multiple_strs:
        temp_count = wordcount(string)
        total_word_count.update(temp_count)
    return total_word_count

#lwc = linear_word_count(big_str)
#print(lwc)

@time_deco
def multiprocess_word_count(multiple_strs):
    total_word_count = {}
    with multiprocessing.Pool(4) as workers:
        result_iter = workers.map(wordcount, multiple_strs)
        for k in result_iter:
            total_word_count.update(k)
    return total_word_count

#mwc = multiprocess_word_count(big_str)
#print(mwc)

#using yield to pass input to functions

def yield_func():
    current_input = yield
    curr_sum = 0
    while True:
        curr_sum += current_input
        print('sum: {0}'.format(curr_sum))
        current_input = yield
yield_obj = yield_func()
next(yield_obj)
yield_obj.send(5)
yield_obj.send(10)
yield_obj.send(15)
yield_obj.send(30)

#coroutines in python
#coroutines are functions that use  yield statements to input data
#generators are producers while coroutines are consumers of data
#execute in response to next() and send() methods
#can run indefinitely, use close() to stop exe

def get_max_till_now():
    latest = yield
    max_till_now = latest
    while True:
        latest = yield max_till_now
        max_till_now = max(latest, max_till_now)
        yield max_till_now

max_gen = get_max_till_now()
next(max_gen)
print(max_gen.send(9))
print(max_gen.send(11))
print(max_gen.send(10))
print(max_gen.send(12))
max_gen.close()

def infinite_sum():
    print('infinite sum started')
    curr_sum = 0
    latest = -1
    try:
        while True:
            latest = yield
            curr_sum += latest
    except GeneratorExit:
        print('final sum is {0}'.format(curr_sum))

inf_sum = infinite_sum()
next(inf_sum)
inf_sum.send(9)
inf_sum.send(10)
inf_sum.send(11)
inf_sum.send(12)
inf_sum.send(13)
inf_sum.close()

def chain_coroutine(num_list, my_coroutine):
    for elem in num_list:
        my_coroutine.send(elem)
    my_coroutine.close()

inf_sum = infinite_sum()
next(inf_sum)
chain_coroutine([1,2,3,4,5,6], inf_sum)

#data pipelines with coroutines

#coroutines can suspend their execution like generators
#multiple coroutines can be chained together to form a pipeline
#roles
    #producer - send data to filters/sink in a series, w/ no yield statement
    #filter - receives data from previous step and sends data to next step
    #sink - uses yield to receive data but cannot send data

#filter: remove punctuation
def rem_punc(next_cor):
    print('Start punctuation removal')
    try:
        while True:
            word = yield
            next_cor.send(re.sub(r'[^\w\s]', '', word))
    except:
        next_cor.close()

#filter: change case to lowercase
def sani_word(next_cor):
    print('start lowering words')
    try:
        word = yield
        next_cor.send(word.lower())
    except:
        next_cor.close()

from collections import defaultdict

#sink: prints word count
def print_wc():
    word_count = {}
    try:
        while True:
            word = yield
            if word_count.get(word, None):
                word_count[word] += 1
            else:
                word_count[word] = 1
    except GeneratorExit:
        print(word_count)

#producer
def word_count_producer(text, sanitize_coroutine):
    for word in text.split(' '):
        sanitize_coroutine.send(word)
    sanitize_coroutine.close()

#init sink and then coroutine in reverse order
my_wc = print_wc()
#call next over sink
next(my_wc)
#init filters in reverse and chain the sink to the last filter
sn_words = sani_word(my_wc)
next(sn_words)

rem_words = rem_punc(sn_words)
next(rem_words)
my_str = 'this is a string. And here is a string'
result = word_count_producer(my_str, rem_words)
print(result)
