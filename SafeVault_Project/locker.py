#JSON / File Read and Write (20 pts)
 
def make_secret(text):
    result = ""
    for letter in text:
        result = result + letter + "-"
    return result
