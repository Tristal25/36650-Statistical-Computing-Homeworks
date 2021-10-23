def remove_punc(string):
    # input: a string
    # output: another string with all the punctuations deleted
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    st = string
    for c in punctuations:
        st = st.replace(c,"")
    return st
