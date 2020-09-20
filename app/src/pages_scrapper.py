from typing import List

from .pages_data import pages_data
from .util import (
    add_prefix,
    create_soup,
    filter_string,
    find_page_number,
    find_tag_in_results,
    get_url_content,
    search_in_soup,
    shuffle_lists,
)


class PagesScrapper:
    """ Class holding all methods for scrapping pages in search for memes."""

    pages_data = pages_data

    def scrap_pages(self, pages_names: List[str], page_number: int) -> List[str]:
        """Scraps all given pages for given page number.

        Algorithm is simple:
            1. For every page given url is generated taking page number into consideration, if
                page number is equal to 2, and page url is "www.sample.pl" scrapper will use
                "www.sample.pl/2"
            2. Such generated url are then scrapped looking for memes.

        Attrs:
            pages_names: list of string representing pages to be scrapped, eg.: ["JBZD", "kwejk"]
            page_number: integer number representing which page number should be scrapped

        Returns:
            List of memes urls.

        Example Result:
            ["www.kwejk.pl/image/09089.jpg", "www.jbzd.pl/obrazek/8989jkjk.png"]

        """

        urls = self._get_pages_urls(pages_names, page_number)
        memes = self._scrap_pages_for_memes(pages_names, urls)
        shuffled_memes = shuffle_lists(memes)

        return shuffled_memes

    def _get_pages_urls(self, pages_names: List[str], page_number: int) -> List[str]:
        """Returns given pages urls for given page number.

        Attrs:
            pages_names: list of string representing pages to be scrapped, eg.: ["JBZD", "kwejk"]
            page_number: integer number representing which page number should be scrapped

        Returns:
            List of urls representing urls to be scrapped for memes.

        Example Result:
            ["www.sample1.com/strona/1", "www.sample2.com/page/3"]

        """

        return [self._get_page_url(page, page_number) for page in pages_names]

    def _get_page_url(self, page_name: str, page_number: int) -> str:
        """Returns given page url for given page number.

        Attrs:
            page_name: list of string representing pages to be scrapped, eg.: ["JBZD", "kwejk"]
            page_number: integer number representing which page number should be scrapped

        Returns:
            List of urls representing urls to be scrapped for memes.

        Example Result:
            ["www.sample1.com/strona/1", "www.sample2.com/page/3"]

        Function checks if url with added page number is decreasing or increasing and perform
        all needed correction due to this characteristics.
        """

        page_data = self.pages_data[page_name]

        if page_data["page_direction"] == "increasing":
            number = str(page_number)

        elif page_data["page_direction"] == "decreasing":
            number = self._find_starting_page_number(page_data) - page_number + 1

        return page_data["url"] + page_data["page_prefix"] + str(number)

    def _scrap_pages_for_memes(self, pages_names: List[str], urls: List[dict]) -> List[str]:
        """Scraps given pages for memes.

        Attrs:
            pages_names: list of string representing pages to be scrapped, eg.: ["JBZD", "kwejk"]
            url: list of pages urls to be scrapped (with page number added already)

        Returns:
            List of memes urls.

        Example Result:
            ["www.kwejk.pl/image/09089.jpg", "www.jbzd.pl/obrazek/8989jkjk.png"]

        """

        memes = []

        for page, url in zip(pages_names, urls):
            new_images = self._scrap_page_for_memes(pages_data[page], url)
            memes.append(new_images)

        return memes

    def _scrap_page_for_memes(self, page_data: str, url: str) -> List[str]:
        """Scraps single given page for memes.

        Attrs:
            page_data: dict containing all additional data needed (base url, prefixes, tag to be
                searched and so on).
            url: list of pages urls to be scrapped (with page number added already)

        Returns:
            List of memes urls.

        Example Result:
            ["www.kwejk.pl/image/09089.jpg", "www.jbzd.pl/obrazek/8989jkjk.png"]

        """
        page_content = get_url_content(url=url)
        soup = create_soup(page_content=page_content)

        search_result = search_in_soup(soup=soup, pattern=page_data["img_pattern"])
        images = find_tag_in_results(results=search_result, tag_to_find=page_data["img_tag"])

        if page_data.get("img_prefix"):
            filtered_images = filter_string(images, "http")
            images_with_prefix = add_prefix(filtered_images, page_data.get("img_prefix"))
            return images_with_prefix

        return images

    def _find_starting_page_number(self, page_data: dict) -> int:
        """Finds base page number which occurs at index page.

        This function is used if given page uses "decreasing" page number system. For example,
        going to page www.sample1.pl redirects us to www.sample1.pl/page/1999, where 1999 is the
        latest page. This function search fo such number for being able to calculate which page
        is requested if we need "second", "third" and so on page os site.

        Attrs:
            page_data: dict containing all additional data needed (base url, prefixes, tag to be
                searched and so on).

        Returns:
            single integer number representing main page number.
        """
        page_content = get_url_content(url=page_data["url"])
        soup = create_soup(page_content=page_content)
        results = search_in_soup(soup, page_data["page_pattern"])

        number = find_page_number(results)

        return number

    @property
    def get_all_pages_available(self):
        return list(self.pages_data.keys())
