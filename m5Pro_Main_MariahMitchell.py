#Created a program that generate box office reports using lists. (functions.py)
#Mariah Mitchell
#CSC-121
#9 November 2025

import m5Pro_Functions_MariahMitchell as fn

def main():
    file = "movie_sales-2.csv"
    choice = ""
    
   
    while choice != "3":
        print("\n---------------------Menu----------------------------")
        print("1) Read Data and Calculate Revenue (Display results)")
        print("2) Identify and display the top-2-earning movie")
        print("3) Exit")
    
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == "1":
            movies = fn.read_movie_sales(file)
            if movies:
                fn.cal_total_rev(movies)
                fn.display_results(movies)

        elif choice == "2":
            movies = fn.read_movie_sales(file)
            if movies:
                fn.cal_total_rev(movies)
                fn.write_updated_csv("updated_movie_sales.csv", movies)
                fn.write_updated_txt("updated_movie_sales.txt", movies)
                print("\nFiles written successfully: updated_movie_sales.csv and updated_movie_sales.txt")

        elif choice == "3": # Option 3
             print("\nExiting Program!")
        else:
             print("\nInvalid choice. Try again.")
             
if __name__ == "__main__":
       main()