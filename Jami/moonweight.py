def moon_weight(starting_earth_weight, increasing_weight, num_of_years):

    for i in range(num_of_years):
        earth_weight = starting_earth_weight + (increasing_weight * i)
        moon_weight =round( earth_weight * .165, 2)
        print(f"Year {i + 1}, Earth weight = {earth_weight}, moon weght = {moon_weight} ")


moon_weight(100, 2, 15)
