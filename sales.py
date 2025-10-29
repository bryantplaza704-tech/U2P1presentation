peaklist = []

def number_of_peak():
    try:
        anime_number = int(input("How many peak animes would you like to add? "))
    except ValueError:
        print("Please enter a valid number.")
        return

    while len(peaklist) < anime_number:
        peak_anime = input("What is a peak anime? ")
        anime_rating = int(input("What do you rate this anime from 1-10? "))
        print("Added:", peak_anime)
        peaklist.append(peak_anime)
        print("Current list:", peaklist)

    print("You've reached your limit of", anime_number, "peak animes!")
    print("Final list:", peaklist)


number_of_peak()
