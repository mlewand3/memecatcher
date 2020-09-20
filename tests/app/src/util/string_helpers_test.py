from app.src.util import add_prefix, filter_string


def test_add_prefix_function_returns_base_strings_if_prefix_is_not_given():
    # GIVEN
    sample_string_list = ["a", "b", "c"]
    expected_string_list_with_prefix = sample_string_list

    # WHEN
    strings_with_prefix = add_prefix(sample_string_list, prefix=None)

    # THEN
    assert strings_with_prefix == expected_string_list_with_prefix


def test_add_prefix_function_adds_prefix_to_all_elements_in_list():
    # GIVEN
    sample_string_list = ["a", "b", "c"]
    sample_prefix = "1"
    expected_string_list_with_prefix = ["1a", "1b", "1c"]

    # WHEN
    strings_with_prefix = add_prefix(sample_string_list, sample_prefix)

    # THEN
    assert strings_with_prefix == expected_string_list_with_prefix


def test_filter_string_works_properly():
    # GIVEN
    sample_string_list = ["a", "b", "c"]
    sample_filter = "b"
    expected_string_list_with_prefix = ["a", "c"]

    # WHEN
    strings_with_prefix = filter_string(sample_string_list, sample_filter)

    # THEN
    assert strings_with_prefix == expected_string_list_with_prefix
