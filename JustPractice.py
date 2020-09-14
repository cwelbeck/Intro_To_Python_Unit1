
def string_analysis(string):
    if string.isdigit() == True:
        if int(string) > 99:
            return "Big Number"
        else:
            return "Small Number"
    elif string.isalpha() == True:
        return "This string is all alpha."
    elif string.isalpha() == False:
        return "This string is not all alpha nor all digit."
    '''else:
        return "This is a normal string."'''