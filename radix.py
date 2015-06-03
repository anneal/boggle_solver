from pprint import pprint
from collections import defaultdict

def max_length(list_of_data):
    query = [ len(j) for j in list_of_data ]
    return max(query)


def bucketize(list_of_data, place=0):
    bucket = defaultdict(list)
    for nums in list_of_data:
        location = str(nums[place])
        bucket[location].append(nums)
    return dict(bucket)


def check_lower_buckets(buckets, place=0):
    for key in buckets:
        if len(buckets[key]) >= 1 and place < len(buckets[key][0])-1:
            buckets[key] = bucketize(buckets[key],place + 1)
            check_lower_buckets(buckets[key], place + 1)
    return True

def combine_buckets(buckets, result = []):
    for key in sorted(buckets):
        if type(buckets[key]) == list:
            result.append(buckets[key][0])
            return result
        else:
            combine_buckets(buckets[key])

    return result        
       
def main():
    data = [ words.strip() for words in open('wordlist.txt','r')]
    
    buckets = bucketize(data)
    check_lower_buckets(buckets)
    print('\nThe most significant digit radix sort provides the following:\n')
    pprint(buckets)
    

main()
