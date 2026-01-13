#Created a program that generate box office reports using lists. (functions.py)
#Mariah Mitchell
#CSC-121
#5 Oct 2025

import csv

def read_movie_sales(file):
    movies = []
    try:
        with open('movie_sales-2.csv', "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    movie = row["Movie"]
                    tickets_sold = int(row["TicketsSold"])
                    ticket_price = float(row["TicketPrice"])
                    movies.append({
                        "Movie": movie,
                        "TicketsSold": tickets_sold,
                        "TicketPrice": ticket_price
                    })
                except ValueError:
                    # Handles bad numeric data
                    print(f"Data format error in row: {row}")
        return movies

    except FileNotFoundError:
        print(f"Error: File '{file}' not found.")
        return []
    
def cal_total_rev(movies):
    """
    Calculate the total revenue for a movie
    
    Parameters
    ----------
    tickets_sold : int
        The amount of tickets sold for the movie.
    ticket_price : float
        The cost per ticket price.

    Returns
    -------
    float
        The total revenue for the movie.
        """
    for movie in movies:
        movie["Revenue"] = movie["TicketsSold"] * movie["TicketPrice"]


def classify_movie(revenue):
    if revenue >= 3000:
        return "Blockbuster"
    elif revenue >= 2000:
        return "Moderate Hit"
    else:
        return "Low Performer"

def display_results(movies):
    print(f"{'Movie':35s} {'Revenue ($)':>15s}")
    print("-" * 50)
    for movie in movies:
        print(f"{movie['Movie']:35s} ${movie['Revenue']:>10,.2f}")
        
def write_updated_csv(filename, movie_list):
    # Sort by revenue (highest first)
    sorted_movies = sorted(movie_list, key=lambda x: x["Revenue"], reverse=True)

    with open(filename, "w", newline="", encoding="utf-8") as f:
        fieldnames = ["Movie", "TicketsSold", "TicketPrice", "Revenue", "Rating"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for movie in sorted_movies:
            writer.writerow({
                "Movie": movie["Movie"],
                "TicketsSold": f"${movie['TicketsSold']:,}",
                "TicketPrice": f"${movie['TicketPrice']:,.2f}",
                "Revenue": f"${movie['Revenue']:,.2f}",
                "Rating": classify_movie(movie["Revenue"])
            })


def write_updated_txt(file, movies):
    sorted_movies = sorted(movies, key=lambda x: x["Revenue"], reverse=True)

    with open(file, "w", encoding="utf-8") as outfile:
        outfile.write(f"{'Movie':35s} {'TicketsSold':>12s} {'TicketPrice':>12s} {'Revenue':>12s} {'Rating':>15s}\n")
        outfile.write("-" * 90 + "\n")

        for movie in sorted_movies:
            outfile.write(f"{movie['Movie']:35s} "
                          f"{'$'+format(movie['TicketsSold'], ','):>12s} "
                          f"{'$'+format(movie['TicketPrice'], ',.2f'):>12s} "
                          f"{'$'+format(movie['Revenue'], ',.2f'):>12s} "
                          f"{classify_movie(movie['Revenue']):>15s}\n")


