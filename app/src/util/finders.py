import bs4


def find_tag_in_results(results: bs4.element.ResultSet, tag_to_find: str):
    """Finds in BeutifulSoup result for given tag.

    Attrs:
        results: bs4.element.ResultSet object
        tag: string representing tag to be found on results.

    Returns:
        Tag object which fits given condition.
    """

    find_results = []

    for result in results:
        try:
            find_results.append(result[tag_to_find])
        except KeyError:
            pass

    return find_results


def find_page_number(results: bs4.element.ResultSet) -> int:
    """
    Search for the page number in page patterns and return first result which can be
    intrepreted as page number (we assume that the first result will be these with highest number).

    Attrs:
        results: bs4.element.ResultSet object

    Returns:
        Single integer number representing page number.
    """

    for result in results[0]:
        try:
            number = result.text
            return int(number)

        except AttributeError:
            pass

    return 0
