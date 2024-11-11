import Lab2 as lab
def test_min_max():
    input_arr=[1,2,3,4,5,6,7,8,9,10]
    test_answer=(1,10)
    result=lab.find_min_max(input_arr)
    assert result==test_answer
def test_calc_average():
    input_arr=[1,2,3,4,5]
    test_answer=3
    result=lab.calc_average(input_arr)
    assert result==test_answer
def test_median_temperature():
    input_arr=[1,643,5,6,7,8,2,4,10]
    test__answer=6
    result=lab.calc_median_temperature(input_arr)
    assert result==test__answer