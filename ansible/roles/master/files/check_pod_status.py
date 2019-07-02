import sys
import json

if __name__ == '__main__':
    
    json_str = sys.stdin.read()

    json_obj = json.loads(json_str)

    conditions_list = [item['status']['conditions'] for item in json_obj['items']]

    if len(conditions_list) != 9:
        print "Conditions list is not equal to 9"
        exit(1)

    for conditions in conditions_list:
        
        if len(conditions) != 4:
            print "Number of conditions is not 4"
            exit(1)

        for condition in conditions:
            if condition['status'] != 'True':
                print "Condition status is not True"
                exit(1)

    print "Pod status check is successful"
    exit(0)