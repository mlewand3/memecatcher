from typing import List


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


def add_src_prefix(images: List[str], img_prefix: str) -> List[str]:
    """Iterates through list of image tags, and add prefix (if needed).

    Some of the results can be ad which are caught by accident, presuming it is those image which
    have complete url (with "http") already.
    """
    pages_with_prefix_added = []

    if not img_prefix:
        return images

    for image in images:
        if "http" in image["src"]:
            pass
        else:
            pages_with_prefix_added.append({"src": img_prefix + image["src"]})

    return pages_with_prefix_added


def add_next_page_prefix(checkpoint: str, checkpoint_prefix: str) -> str:
    """Add next page prefix if needed."""

    if not checkpoint_prefix:
        return checkpoint

    checkpoint_with_prefix = checkpoint_prefix + checkpoint

    return checkpoint_with_prefix
