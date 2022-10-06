import json
from difflib import get_close_matches

data = json.load(open('data.json'))


def translate(ww):
    ww = ww.lower()
    if ww in data:
        return data[ww]
    elif ww.title() in data:
        return data[ww.title()]
    elif ww.upper() in data:
        return data[ww.upper()]    
    elif len(get_close_matches(ww, data.keys())) > 0:
        yn = input( "Did you mean %s instead? Enter Y if yes, or N if no." % get_close_matches(ww, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(ww, data.keys())[0]]  
        elif yn == "N":
            return "The word doesn`t exist, please check it."
        else:
            return "We didin`t understand your entry."  
    else:
        return "The word doesn`t exist, please check it."
    

iw = input("Enter word:")
#print(translate(iw))
output = translate(iw)

if type(output) == list:
    for i in output: 
        print(i)

else:
    print(output)




