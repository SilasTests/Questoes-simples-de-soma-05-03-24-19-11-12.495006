import subprocess

def test_case_0():
    input_data = "2 2"
    expected_result = "4"
    cast_type = type(expected_result)

    result = subprocess.run(
        "./main",
        input=input_data.encode(),
        stdout=subprocess.PIPE,  
    )
    assert cast_type(result.stdout.decode()) == expected_result
    