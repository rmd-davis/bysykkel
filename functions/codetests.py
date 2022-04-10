def codetest_01_header(input_data):
    test_data = '2021-04-07 04:21:06.812000+00:00'
    
    assert input_data == test_data, f"\nYour output did not match the expected output 🙃🥴 \nGot: {input_data} \nExpected: {test_data}"
    print('Test passed, your output matched the expected output!')


def codetest_02_dtypes(input_data):
    dtype_1 = input_data['started_at']
    dtype_2 = input_data['ended_at']
    test_data = 'datetime64[ns, UTC]'
    
    assert dtype_1 == test_data, f"\nYour output for \'started_at\' did not match the expected output 🙃🥴 \nGot: {dtype_1} \nExpected: {test_data}"
    assert dtype_2 == test_data, f"\nYour output for \'ended_at\' did not match the expected output 🙃🥴 \nGot: {dtype_2} \nExpected: {test_data}"
    print('Test passed, your output matched the expected output!')


def codetest_03_merge(input_data):
    test_data = 'start_station_name'
    
    columns = list(input_data.columns)
    expected_cols = 12
    expected_rows = 137160
    
    assert test_data in columns , f"\nLooks like you're missing {test_data} in your merged frame 🙃🥴"
    assert len(columns) == expected_cols, f"\nLooks like you don't have the right number of columns in your merged frame 🙃🥴\nGot: {len(columns)} \nExpected: {expected_cols}"
    assert len(input_data) == expected_rows, f"\nLooks like you changed the number of rows in your merged frame 🙃🥴\nGot: {len(input_data)} \nExpected: {expected_rows}"
    
    print('Test passed, your output matched the expected output!')


def codetest_04_drop(input_data):
    test_1 = 'start_station_description'
    test_2 = 'end_station_description'
    
    columns = list(input_data.columns)
    expected_cols = 10
    expected_rows = 137160
    
    assert test_1 not in columns , f"\nLooks like {test_1} is still in your dataframe 🙃🥴"
    assert test_2 not in columns , f"\nLooks like {test_2} is still in your dataframe 🙃🥴"

    assert len(columns) == expected_cols, f"\nLooks like you don't have the right number of columns in your dataframe 🙃🥴\nGot: {len(columns)} \nExpected: {expected_cols}"
    assert len(input_data) == expected_rows, f"\nLooks like you changed the number of rows in your dataframe 🙃🥴\nGot: {len(input_data)} \nExpected: {expected_rows}"
    
    print('Test passed, your output matched the expected output!')


def codetest_05_duplicates(input_data):
    test_1 = 29143

    columns = list(input_data.columns)
    expected_cols = 10
    expected_rows = 137159
    
    assert test_1 not in input_data.index , f"\nLooks like index {test_1} is still in your dataframe 🙃🥴"
    
    assert len(columns) == expected_cols, f"\nLooks like you don't have the right number of columns in your dataframe 🙃🥴\nGot: {len(columns)} \nExpected: {expected_cols}"
    assert len(input_data) == expected_rows, f"\nLooks like you changed the number of rows in your dataframe 🙃🥴\nGot: {len(input_data)} \nExpected: {expected_rows}"
    
    print('Test passed, your output matched the expected output!')