"""
This module has class definition both abstract and concrete
for calculators.

Author: Julian David Celis Giraldo <jdcelisg@udistrital.edu.co>

This file is part of PyCalculator-UD.

PyCalculator-UD is free software: you can redistribute it and/or 
modify it under the terms of the GNU General Public License as 
published by the Free Software Foundation, either version 3 of 
the License, or (at your option) any later version.

PyCalculator-UD is distributed in the hope that it will be useful, 
but WITHOUT ANY WARRANTY; without even the implied warranty of 
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
General Public License for more details.

You should have received a copy of the GNU General Public License 
along with PyCalculator-UD. If not, see <https://www.gnu.org/licenses/>. 
"""

# Google Doc Python: python documentation style guide
# Doc String
from ArcadeMachine import ArcadeCatalog, Game
    
def main():
    """
    Main function to interact with the arcade catalog.
    This function allows the user to select a machine type,
    view available games, add games to the machine,
    and complete the purchase by entering customer details.
    """
    
    catalog = ArcadeCatalog()

    print("Welcome to the Arcade Machine Catalog.")
    while True:
        try:
            # Prompt user to select the type of arcade machine
            machine_type = int(input("\nSelect the machine type: 1. Modern, 2. Retro: "))
            break
        except ValueError:
            print("Invalid input. Please enter 1 or 2.")

    catalog.choose_machine(machine_type)
    catalog.show_games()

    # Start the process of adding games until the user decides to exit
    catalog.add_games()

    # Get customer information
    name = input("\nEnter your name: ")
    address = input("Enter your address: ")
    phone = input("Enter your phone number: ")

    catalog.complete_purchase(name, address, phone)


# Games available in the catalog (Added directly)
game1 = Game("Pac-Man", 1, "retro")
game2 = Game("Space Invaders", 2, "retro")
game3 = Game("Donkey Kong", 3, "retro")
game4 = Game("Fortnite", 4, "modern")
game5 = Game("Rocket League", 5, "modern")
game6 = Game("Minecraft", 6, "modern")
game7 = Game("Call of Duty", 7, "modern")
game8 = Game("FIFA 22", 8, "modern")
game9 = Game("Super Mario Bros", 9, "retro")
game10 = Game("Tetris", 10, "retro")

# call the method main(), start here
if __name__ == "__main__":
    main()
