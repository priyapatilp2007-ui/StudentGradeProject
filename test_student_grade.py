from student_grade import average, grade, is_pass, highest, lowest

# Test 1: Average calculation
def test_average():
    assert average([80, 90, 70]) == 80

# Test 2: Grade A+
def test_grade_a_plus():
    assert grade(95) == "A+"

# Test 3: Grade A
def test_grade_a():
    assert grade(85) == "A"

# Test 4: Grade F
def test_grade_f():
    assert grade(40) == "F"

# Test 5: Pass result
def test_is_pass():
    assert is_pass([80, 75, 90]) == True

# Test 6: Fail result
def test_is_fail():
    assert is_pass([80, 30, 90]) == False

# Test 7: Highest marks
def test_highest():
    assert highest([80, 90, 70]) == 90

# Test 8: Lowest marks
def test_lowest():
    assert lowest([80, 90, 70]) == 70