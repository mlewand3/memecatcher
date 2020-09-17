def find_in_results(results, tag_to_find: str, tag_label: str = "src"):
    """Finds in BeutifulSoup result for given tag."""

    find_results = []

    for result in results:
        try:
            find_results.append({tag_label: result[tag_to_find]})
        except KeyError:
            pass

    return find_results


def extract_tag_content(result, tag: str):
    """Extracts tag content from BeautifulSoup result."""

    return result[0][tag]
