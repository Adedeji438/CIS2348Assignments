# Adedeji Akingbola
# 1793979
def get_age():
    age = int(input())
    if age < 18 or age > 75:  
        raise ValueError("Invalid age.")
    return age

# TODO: Complete fat_burning_heart_rate() function
def fat_burning_heart_rate(age):
    heart_rate = (220 - age) * 0.7
    return heart_rate

if __name__ == "__main__":
    # TODO: Modify to call get_age() and fat_burning_heart_rate()
    #       and handle the exception
    try:
        age = get_age()
        rate = fat_burning_heart_rate(age)
        print("Fat burning heart rate for a", age, "year-old:", rate, "bpm")
    except ValueError as e:
        print(e)
        print('Could not calculate heart rate info.')
        print()
