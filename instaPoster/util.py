from collections import Counter

def get_top():

    with open('output.txt') as f:
        lines = f.readlines()

    counts = Counter(lines)
    final_string = ""
    for s in counts.most_common(3):
        final_string += s[0][:-1] + " "

    return final_string +" outfit"

if __name__=="__main__":
    get_top()