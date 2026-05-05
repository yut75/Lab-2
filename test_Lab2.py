import Lab2 as lab2

def test_calc_average():
    data = [10, 20, 30, 40]
    result = lab2.calc_average(data)
    assert result == 25


def test_find_min_max():
    data = [10, 20, 5, 40]
    result = lab2.find_min_max(data)
    assert result == [5, 40]


def test_sort_temperature():
    data = [30, 10, 20]
    result = lab2.sort_temperature(data)
    assert result == [10, 20, 30]


def test_calc_median_temperature():
    result = 0
    input_list = [5, 15, 25, 35, 45]
    expected_result = 25

    result = lab2.calc_median_temperature(input_list)
    assert result == expected_result
   