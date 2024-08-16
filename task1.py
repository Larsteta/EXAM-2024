# Flow-løbenummer: 8
# 1. Functions and FlowControl

# a) Employee Performance Rating (15%)

def evaluate_performance(data):
    # Sales Target Achievement
    if data['salesTarget'] < 80:
        salesTarget = 'Poor'
    elif 80 <= data['salesTarget'] < 100:
        salesTarget = 'Average'
    elif 100 <= data['salesTarget'] < 120:
        salesTarget = 'Good'
    else:
        salesTarget = 'Excellent'

    # Customer Satisfaction Score
    if data['customerSatisfaction'] < 6:
        customerSatisfaction = 'Poor'
    elif 6 <= data['customerSatisfaction'] <= 7:
        customerSatisfaction = 'Average'
    elif 8 <= data['customerSatisfaction'] <= 9:
        customerSatisfaction = 'Good'
    else:
        customerSatisfaction = 'Excellent'

    # Attendance Record
    if data['attendance'] < 20:
        attendance = 'Poor'
    elif 20 <= data['attendance'] <= 24:
        attendance = 'Average'
    elif 25 <= data['attendance'] <= 27:
        attendance = 'Good'
    else:
        attendance = 'Excellent'

    # Peer Feedback Score
    if data['peerFeedback'] < 4:
        peerFeedback = 'Poor'
    elif 4 <= data['peerFeedback'] <= 6:
        peerFeedback = 'Average'
    elif 7 <= data['peerFeedback'] <= 8:
        peerFeedback = 'Good'
    else:
        peerFeedback = 'Excellent'

    # Performance Ratings
    ratings = [salesTarget, customerSatisfaction, attendance, peerFeedback] 

    # Overall Performance Rating
    if ratings.count('Excellent') == 4:
        return 'Outstanding'
    elif ratings.count('Poor') >= 2:
        return 'Needs Improvement'
    elif ratings.count('Good') + ratings.count('Excellent') >= 3:
        return 'Strong Performer'
    else:
        return 'Satisfactory'

# Test Cases
def task_A_test_cases(): 
    test_cases = [
        {'data': {'salesTarget': 120, 'customerSatisfaction': 10, 'attendance': 30, 'peerFeedback': 10}, 'expected': 'Outstanding'},
        {'data': {'salesTarget': 0, 'customerSatisfaction': 0, 'attendance': 30, 'peerFeedback': 10}, 'expected': 'Needs Improvement'},
        {'data': {'salesTarget': 120, 'customerSatisfaction': 10, 'attendance': 25, 'peerFeedback': 0}, 'expected': 'Strong Performer'},
        {'data': {'salesTarget': 120, 'customerSatisfaction': 10, 'attendance': 25, 'peerFeedback': 8}, 'expected': 'Strong Performer'},
        {'data': {'salesTarget': 120, 'customerSatisfaction': 10, 'attendance': 24, 'peerFeedback': 6}, 'expected': 'Satisfactory'},
    ]

    # Loop through test cases
    for test in test_cases:
        result = evaluate_performance(test['data']) # Get result
        if result == test['expected']: # Compare result with expected
            print(f"Test Passed - Expected: {test['expected']}, Got: {result}")
        else:
            print(f"Test Failed - Expected: {test['expected']}, Got: {result}")

# Run Test Cases
print("Task 1.A Test Cases:")
print("-"*100)
task_A_test_cases()
print("-"*100)

# b) EmployeeBonusCalculator(15%)

def calculate_bonus(data):
    # Performance Rating
    if data['performanceRating'] == 'Outstanding':
        baseBonus = 1000
    elif data['performanceRating'] == 'Strong Performer':
        baseBonus = 800
    elif data['performanceRating'] == 'Satisfactory':
        baseBonus = 500
    else:
        baseBonus = 200

    # Years of Service Multiplier
    if data['yearsOfService'] < 2:
        multiplier = 1
    elif 2 <= data['yearsOfService'] <= 5:
        multiplier = 1.5
    else:
        multiplier = 2

    return baseBonus * multiplier

# Test Cases
def task_B_test_cases(): 
    test_cases = [
        {'data': {'performanceRating': 'Outstanding', 'yearsOfService': 1}, 'expected': 1000}, 
        {'data': {'performanceRating': 'Strong Performer', 'yearsOfService': 2}, 'expected': 1200},
        {'data': {'performanceRating': 'Satisfactory', 'yearsOfService': 5}, 'expected': 750},
        {'data': {'performanceRating': 'Needs Improvement', 'yearsOfService': 10}, 'expected': 400},
    ]

    # Loop through test cases
    for test in test_cases: 
        result = calculate_bonus(test['data'])
        if result == test['expected']:
            print(f"Test Passed - Expected: {test['expected']}, Got: {result}")
        else:
            print(f"Test Failed - Expected: {test['expected']}, Got: {result}")

# Run Test Cases
print("Task 1.B Test Cases:")
print("-"*100)
task_B_test_cases()
print("-"*100)