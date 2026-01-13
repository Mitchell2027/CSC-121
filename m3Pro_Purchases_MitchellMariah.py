#Created a program that generate box office reports using lists. (main.py)
#Mariah Mitchell
#CSC-121
#5 Oct 2025
   
import m3Pro_Purchase_Functions_MitchellMariah as fn

def main():
    #Define lists (movies, sold tickets, and prices)
    movie_titles = ['Transformers', 'Life', 'Avengers', 'The Conjuring',   ]
    tickets_sold = [267, 150, 250, 290]
    ticket_prices = [13.49, 17.49, 10.79, 13.49]
    
    # Calculate total revenues using list comprehension
    total_revenues = [fn.cal_total_rev(tickets_sold[i], ticket_prices[i]) for i in range(len(movie_titles))]
    # While loop that displays menu    
    choice = "0"
    while choice != "5":
        print('\n----------------------Menu------------------------------------')
        print('1) Display name, tickets sold, price and revenue per movie')
        print('2) Identify and display the top-2-earning movie')
        print('3) Display the average revenue across all movies')
        print('4) Display movie name, and revenue in descending order of revenue')
        print('5) Exit')
    
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == "1": # Option 1
           fn.display_report(movie_titles, tickets_sold, ticket_prices, total_revenues)
        elif choice == "2": # Option 2
            top_two = fn.get_top_two_movies(movie_titles, total_revenues)
            print("\nTop 2 Earning Movies:")
            for movie, rev in top_two:
                print(f"  {movie}: ${rev:,.2f}")
        elif choice == "3": # Option 3
            avg_rev = sum(total_revenues) / len(total_revenues)
            print(f"\nAverage Revenue: ${avg_rev:,.2f}")
        elif choice == "4": #Option 4
            fn.show_sorted_by_revenue(movie_titles, total_revenues)
        elif choice == "5": # Option 5
            print("\nExiting Program!")
        else:
            print("\nInvalid choice. Try again.")
        
if __name__ == "__main__":
       main()