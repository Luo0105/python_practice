def word_search(doc_list, keyword):
    """
    Takes a list of documents (each document is a string) and a keyword.
    Returns list of the index values into the original list for all documents
    containing the keyword.

    Example:
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    >>> word_search(doc_list, 'casino')
    >>> [0]
    """
    result_indices = []
    keyword_lower = keyword.lower()
    for i, doc in enumerate(doc_list):
        lower_doc = doc.lower()
        words = lower_doc.split()
        for word in words:
            # Remove punctuation from the word for more accurate matching
            cleaned_word = word.strip('.,?!')
            if keyword_lower == cleaned_word:
                result_indices.append(i)
                break  # Once found in a document, move to the next
    return result_indices

def multi_word_search(doc_list, keywords):
    """
    Takes list of documents (each document is a string) and a list of keywords.
    Returns a dictionary where each key is a keyword, and the value is a list of indices
    (from doc_list) of the documents containing that keyword

    >>> doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
    >>> keywords = ['casino', 'they']
    >>> multi_word_search(doc_list, keywords)
    {'casino': [0, 1], 'they': [1]}
    """
    keyword_to_indices = {}
    for keyword in keywords:
        indices = word_search(doc_list, keyword)
        keyword_to_indices[keyword] = indices
    return keyword_to_indices