from typing import List


def find_in_results(results, tags: List[str]):
    return [{tag: result[tag] for tag in tags} for result in results]


def extract_tag_content(result, tag: str):
    return result[0][tag]
