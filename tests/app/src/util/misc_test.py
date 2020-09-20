from app.src.util import shuffle_lists


def test_shuffle_list_function_works_properly_for_two_equal_sized_lists():
    # GIVEN
    sample_list_a = ["a", "b", "c"]
    sample_list_b = ["x", "y", "z"]
    expected_shuffled_lists = ["a", "x", "b", "y", "c", "z"]

    # WHEN
    shuffled_lists = shuffle_lists([sample_list_a, sample_list_b])

    # THEN
    assert shuffled_lists == expected_shuffled_lists


def test_shuffle_list_function_works_properly_for_two_not_equal_sized_lists():
    # GIVEN
    sample_list_a = ["a", "b", "c"]
    sample_list_b = ["x", "y"]
    expected_shuffled_lists = ["a", "x", "b", "y", "c"]

    # WHEN
    shuffled_lists = shuffle_lists([sample_list_a, sample_list_b])

    # THEN
    assert shuffled_lists == expected_shuffled_lists
