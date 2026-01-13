#Created a program that generate box office reports using lists. (functions.py)
#Mariah Mitchell
#CSC-121
#5 Oct 2025


def cal_total_rev(tickets_sold, ticket_price):
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
    return tickets_sold * ticket_price

def display_report(movie_titles, tickets_sold, ticket_prices, total_revenues):
    """
    Display a formatted table wit mive name, tickets sold, price, and revenue
    
    Parameters
    ----------
    movie_titles : str list
        A list of movie titles.
    tickets_sold : int list
        A list of the amount of tickets sold for each movie.
    ticket_prices : float list
        A list of the ticket price for each movie.
    total_revenues : float list
         A list of the total revenue for each movie.

    Returns
    -------
    None.

    """
    print("\nBox Office Report")
    print('-'*65)
    print(f"{'Movie':<18}{'Tickets Sold':>10}{'$Price':>10}{'Revenue':>15}")
    print('-'*65)
    # For loop that goes through each movie
    for i in range(len(movie_titles)):
        print(f"{movie_titles[i]:<20}{tickets_sold[i]:>10,}${ticket_prices[i]:>10.2f}${total_revenues[i]:>15,.2f}")
    
def get_top_two_movies(movie_titles, total_revenues):
    """
    Finds the two movies with the highest revenues.

    Parameters
    ----------
    movie_titles : str list
        The list of movie titles.
    total_revenues : float list
        The list of total revenues per movie.

    Returns
    -------
    top_two : tuple list
        A list of two tuples, containing movie_title and total_revenue.

    """
    # Copy the lists to avoid modifying
    titles = movie_titles[:]
    revenues = total_revenues[:]
    top_two = []
    # For Loop to find the two highest revenues
    for _ in range(2):
        # Find the maximum revenue
        max_index = revenues.index(max(revenues))
        # Append the movie and revenue to top_two
        top_two.append((titles[max_index], revenues[max_index]))
        # Remove the selected movie and revenue so the next max is found
        titles.pop(max_index)
        revenues.pop(max_index)

    return top_two

def show_sorted_by_revenue(movie_titles, total_revenues):
    """
    Displays all movies and their revenues in descending order.

    Parameters
    ----------
    movie_titles : str list
        The list of movie titles.
    total_revenues : float list
        The total revenue of each movie.

    Returns
    -------
    None.

    """
    #Copy the lists to avoid modifying
    titles = movie_titles[:]
    revenues = total_revenues[:]
    #Display the header
    print("\nMovies Sorted by Revenue (High to Low)")
    print('-'*50)
    print(f"{'Movie':<25}{'Revenue':>10}")
    print('-'*50)

    # Loop until all movies are displayed
    while titles:
        # Find the index of the highest revenue
        max_index = 0
        for i in range(1, len(revenues)):
            if revenues[i] > revenues[max_index]:
                max_index = i

        # Print that movie
        print(f"{titles[max_index]:<25}${revenues[max_index]:>10,.2f}")

        # Remove it from the lists
        titles.pop(max_index)
        revenues.pop(max_index)