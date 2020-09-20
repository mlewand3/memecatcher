from app.src.pages_data import pages_data


def get_all_pages_available():
    return list(pages_data.keys())


def get_all_pages_with_decreasing_page_number():
    pages = []

    for page in get_all_pages_available():
        if pages_data[page]["page_direction"] == "decreasing":

            pages.append(page)

    return pages
