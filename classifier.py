from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
f = open("resources/data.txt", "r")
output_list = f.read()
output_list = output_list.split(",")
f.close()
print(len(output_list))


def get_output(text, output_list):
    text = text.lower()
    output_list.append(text)
    cm = CountVectorizer().fit_transform(output_list)
    similar = cosine_similarity(cm[-1], cm)
    similar_list = similar
    output_list.remove(text)
    return similar_list


def give_output(text):
    a = get_output(text, output_list)[0]
    max_val = a[0]  
    index = 0
    valTwo = [max]
    for i in range(1, len(a)-1):
        if max_val > a[i]:
            pass
        elif max_val == a[i]:
            valTwo.append(a[i])
        else:
            max_val = a[i]
            index = i

    if max_val >= 0.6:
        return output_list[index]
    else:
        return "sorry"

def classify(n):
    a = give_output(n)
    a = give_output(n)
    return a