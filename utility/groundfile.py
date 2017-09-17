import re


def parse_ground_file(file_name):
    threshold_found = False
    with open(file_name) as in_file:
        for line in in_file:
            print("Input text--> {}".format(line))
            # Search for the threshold value
            if(not threshold_found):
                threshold = re.search(re.compile('[+|-]\d+'), line).group(0)
            if(threshold_found):
                #Search for the first occurunce only as there can be only one ground function
                func = re.search(re.compile('([+|-]\d+(\s+[+|-]\d+)*)?'), line).group(0)
                if (func):
                    print("Ground function -->{}".format(func))
                    pattern_term = re.compile('\s*([+|-]\d+)\s*')
                    terms = re.findall(pattern_term, func)
                    print(terms)
                    sum = 0
                    for term in terms:
                        #sign, value = term
                        sum += float(term)
                        #print("Term -->{}, Sign --> {}, Value --> {} ".format(term, sign, value))
                        print("Term -->{} ".format(term))
                        print("Sum --> {} ".format(sum))
            if (threshold):
                threshold_found = True
                print("Threshold -->"+threshold)

    # for term in search_res:
    #     print term

parse_ground_file('sample_thresh')
