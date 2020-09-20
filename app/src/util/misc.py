from typing import Any, List


def shuffle_lists(_lists: List[Any]) -> List[Any]:
    """
    Merges two (or more lists) into one in a way that elements from those list appears alternately.

    Function also work if length of lists are different.

    Example:
        list1 = ["a", "b", "c"]
        list2 = [ "1", "2", "3"]

        _shuffle_lists([list1, list2])

        >>> ["a", "1", "b", "2", "c", "3"]


        when lists are different lengths, elements from shorter one is ommited later on in merged
        list.

        list1 = ["a", "b", "c", "d", "e"]
        list2 = [ "1", "2", "3"]

        _shuffle_lists([list1, list2])

        >>> ["a", "1", "b", "2", "c", "3", "d", "e"]

    Attrs:
       _lists - lists of lists

    Returns:
        single lists merged from given list of lists.
    """
    result = []

    while any(_lists):
        for _list in _lists:
            if len(_list) == 0:
                pass
            else:
                result.append(_list.pop(0))

    return result
