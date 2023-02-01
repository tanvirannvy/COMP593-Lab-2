def main():
    data = {
        "full_name": "SYED TANVIR HASAN",
        "student_id": 10267631,
        "pizza_toppings": ["PEPPERONI", "MUSHROOMS", "ONIONS"],
        "movies": [
            {"title": "the Shawshank redemption", "genre": "drama"},
            {"title": "the godfather", "genre": "crime"}
        ]
    }

    # Step 3: Add another movie to the data structure
    data["movies"].append({"title": "the dark knight", "genre": "action"})

    # Step 4: Use a function to print student name and ID
    def print_student_info(data):
        first_name = data["full_name"].split(" ")[0]
        print(f"My name is {data['full_name']}, but you can call me LORD {first_name}.")
        print(f"My student ID is {data['student_id']}.")
    print_student_info(data)

    # Step 5: Use a function to add pizza toppings to the data structure
    def add_pizza_toppings(data, toppings):
        data["pizza_toppings"] += toppings
        data["pizza_toppings"] = sorted(data["pizza_toppings"])
        data["pizza_toppings"] = [topping.lower() for topping in data["pizza_toppings"]]
    add_pizza_toppings(data, ("BACON", "CHEESE"))

    # Step 6: Use a function to print a bullet list of pizza toppings
    def print_pizza_toppings(data):
        print("My favourite pizza toppings are:")
        for topping in data["pizza_toppings"]:
            print(f"- {topping}")
    print_pizza_toppings(data)
    add_pizza_toppings(data, ("OLIVES", "TOMATOES"))
    print_pizza_toppings(data)

    # Step 7: Use a function to print a comma-separated list of movie genres
    def print_movie_genres(data):
        genres = [movie["genre"] for movie in data["movies"]]
        genres_str = ", ".join(genres)
        print(f"I like to watch {genres_str} movies.")
    print_movie_genres(data)

    # Step 8: Use a function to print a comma-separated list of movie titles
    def print_movie_titles(movies):
        titles = [movie["title"].title() for movie in movies]
        titles_str = ", ".join(titles)
        print(f"Some of my favourite movies are {titles_str}!")
    print_movie_titles(data["movies"])

if __name__ == "__main__":
    main()
