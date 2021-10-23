def remove_punc(string):
    # input: a string
    # output: another string with all the punctuations deleted
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    st = string
    for c in punctuations:
        st = st.replace(c,"")
    return st

remove_punc("Hello in 36-650,& other MSP courses.")