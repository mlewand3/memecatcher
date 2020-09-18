def find_tag_in_results(results, tag_to_find: str):
    """Finds in BeutifulSoup result for given tag.

    Attrs:
        results: ?
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


def find_page_number(results) -> int:
    """
    Search for the page number in page patterns and return first result which can be
    intrepreted as page number (we assume that the first result will be these with highest number).

    Attrs:
        results: ???

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
