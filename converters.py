def lbs_to_kg(weight):
    return weight * 0.45


def kg_to_lbs(weight):
    return weight / 0.45

def find_max(numbers):
    number_highest = numbers[0]
    for value in numbers:
        if value > number_highest:
            number_highest = value
    return number_highest