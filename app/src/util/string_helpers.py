from typing import List


def filter_string(_strings: List[str], filter: str = "http") -> List[str]:
    """Filters list of strings from unwanted string

    Attrs:
        _strings - list of strings to be prefixed,
        filter - string to be filtered from list.

    Returns:
        List of strings with filtered values.
    """
    filtered_list = []

    for _string in _strings:
        if filter in _string:
            pass
        else:
            filtered_list.append(_string)

    return filtered_list


def add_prefix(_strings: List[str], prefix: str) -> List[str]:
    """Iterates through list of image tags, and add prefix (if needed).

    Some of the results can be ad which are caught by accident, presuming it is those image which
    have complete url (with "http") already.

    Attrs:
        _strings - list of strings to be prefixed,
        prefix - string representing prefix value,

    Returns:
        List of strings with added prefix.
    """
    pages_with_prefix_added = []

    if not prefix:
        return _strings

    for _string in _strings:
        pages_with_prefix_added.append(prefix + _string)

    return pages_with_prefix_added
