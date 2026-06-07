#random
#A Python function that takes a probability between 0.0 and 1.0 and returns True with that probability. 
#For example, if the input probability is 0.3, the function should return True in the 30% of times and False in the 70% of times.

import random

module_name = "random"


def chance(probability):
    if probability < 0 or probability > 1:
        raise ValueError("Probability must be between 0 and 1")
    if random.random() < probability:
        return True
    else:
        return False
    

    from probability_file import chance


    def main():
        try:
            for i in range(10):
                print(chance(0.3))
        except ValueError:
            print("Please enter a number between 0 and 1")


    if __name__ == "__main__":
        main()