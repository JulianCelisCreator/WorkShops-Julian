"""
The code in the given module is an interactive program that allows users to interact
with an arcade machine catalog. It starts by prompting the user to select the type 
of arcade machine (modern or retro). 
Then, it displays the available games in the catalog. The user can choose to add 
games to the machine. Finally, the program asks for customer information 
(name, address, phone number)
and completes the purchase. The module also defines a `Game` class and creates 
instances of it to represent the available games in the catalog.

Author: Julian David Celis Giraldo <jdcelisg@udistrital.edu.co>

This file is part of ArcadeMachine.

ArcadeMachine is free software: you can redistribute it and/or 
modify it under the terms of the GNU General Public License as 
published by the Free Software Foundation, either version 3 of 
the License, or (at your option) any later version.

ArcadeMAchine is distributed in the hope that it will be useful, 
but WITHOUT ANY WARRANTY; without even the implied warranty of 
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
General Public License for more details.

You should have received a copy of the GNU General Public License 
along with ArcadeMachine If not, see <https://www.gnu.org/licenses/>. 
"""

# Google Doc Python: python documentation style guide
# Doc String
from ArcadeMachine import ArcadeMachineBuilder, ArcadeCatalog, Game, ArcadeMachineFactory


def main():
    """
    Main function to interact with the arcade catalog.
    This function allows the user to select a machine type,
    view available games, add games to the machine,
    and complete the purchase by entering customer details.
    """
    
    catalog = ArcadeCatalog()
    
    # Default attributes for various machine types
    defaults = {
        "modern": {
            'base_price': 1600,
            'dimensions': '1.70mx0.8mx0.8m',
            'weight': 80.0,  # kg as float
            'power_consumption': 600,  # W as int
            'memory': '8GB',
            'processor': 'Intel Core i5'
        },
        "retro": {
            'base_price': 1200,
            'dimensions': '1.60mx0.7mx0.7m',
            'weight': 70.0,
            'power_consumption': 500,
            'memory': '4GB',
            'processor': 'Intel Core i3'
        },
        "dance": {
            'base_price': 1800,
            'dimensions': '1.80mx0.9mx0.9m',
            'weight': 90.0,
            'power_consumption': 700,
            'memory': '16GB',
            'processor': 'Intel Core i7'
        },
        "classical": {
            'base_price': 1400,
            'dimensions': '1.65mx0.75mx0.75m',
            'weight': 75.0,
            'power_consumption': 550,
            'memory': '6GB',
            'processor': 'Intel Core i4'
        },
        "shooter": {
            'base_price': 2000,
            'dimensions': '1.85mx0.95mx0.95m',
            'weight': 95.0,
            'power_consumption': 750,
            'memory': '12GB',
            'processor': 'Intel Core i7'
        },
        "racing": {
            'base_price': 2200,
            'dimensions': '2.00mx1.00mx1.00m',
            'weight': 100.0,
            'power_consumption': 800,
            'memory': '16GB',
            'processor': 'Intel Core i9'
        },
        "vr": {
            'base_price': 2500,
            'dimensions': '2.10mx1.10mx1.10m',
            'weight': 110.0,
            'power_consumption': 900,
            'memory': '32GB',
            'processor': 'Intel Core i9'
        }
    }

    builder = ArcadeMachineBuilder()

    print("Welcome to the Arcade Machine Catalog.")

    while True:
        try:
            # Prompt for machine type selection
            machine_type = input("Enter the type of machine you want to build (modern, retro, dance, classical, shooter, racing, vr): ").lower()
            if machine_type in defaults:
                builder.set_attributes(defaults[machine_type])

                while True:
                    # Prompt for material selection
                    material_option = input("Choose the material for the machine (wood/aluminum/fiber): ").lower()
                    if material_option in ["wood", "aluminum", "fiber"]:
                        break
                    else:
                        print("Invalid material. Please enter a valid material.")

                # Customize material
                material = catalog.customize_material(material_option)
                builder.set_material(material)

                # Adjust attributes based on material
                if material.value.lower() == "wood":
                    increase_weight = 1.1
                    increase_price = 1.05
                    increase_power = 1.15
                elif material.value.lower() == "aluminum":
                    increase_weight = 0.95
                    increase_price = 1.10
                    increase_power = 1.0
                elif material.value.lower() == "fiber":
                    increase_weight = 0.85
                    increase_price = 1.20
                    increase_power = 0.9
                else:
                    raise ValueError("Invalid material selected.")

                # Set increases for the machine attributes
                builder.set_increases(increase_weight, increase_power, increase_price)

                # Customize color and lights
                builder.set_color(catalog.customize_color(catalog.color_options()))
                builder.set_lights(catalog.customize_light_color(catalog.light_options()))

                # Create the arcade machine
                arcade_machine = ArcadeMachineFactory.create_arcade_machine(machine_type, builder)
                catalog._cart = arcade_machine  # Add the machine to the cart

                print("\nYour machine has been customized and added to your cart!")
                print(arcade_machine)
                Game.show_available_games(machine_type)
                

        except ValueError:
            print("Invalid input. Please try again.")

    # Complete the purchase
    name = input("\nEnter your name: ")
    address = input("Enter your address: ")
    phone = input("Enter your phone number: ")

    catalog.complete_purchase(name, address, phone)


# Games available in the catalog (Added directly)

# Retro Arcade Machine Games
# Retro Games
game1 = Game(title="Pac-Man", code="1", type="retro", storytelling_creator="Toru Iwatani", graphics_creator="Namco", category="classical", price_game=0.25, year="1980")
game2 = Game(title="Donkey Kong", code="2", type="retro", storytelling_creator="Shigeru Miyamoto", graphics_creator="Nintendo", category="platform", price_game=0.50, year="1981")
game3 = Game(title="Frogger", code="3", type="retro", storytelling_creator="Konami", graphics_creator="Sega", category="puzzle", price_game=0.25, year="1981")
game4 = Game(title="Galaga", code="4", type="retro", storytelling_creator="Shigeru Yokoyama", graphics_creator="Namco", category="shooter", price_game=0.30, year="1981")
game5 = Game(title="Asteroids", code="5", type="retro", storytelling_creator="Ed Logg", graphics_creator="Atari", category="shooter", price_game=0.20, year="1979")

# Modern Games
game6 = Game(title="Injustice", code="26", type="modern", storytelling_creator="Ed Boon", graphics_creator="NetherRealm Studios", category="fighting", price_game=1.00, year="2013")
game7 = Game(title="Guitar Hero Arcade", code="27", type="modern", storytelling_creator="Harmonix", graphics_creator="Raw Thrills", category="music", price_game=1.25, year="2009")
game8 = Game(title="Super Smash Bros. Arcade", code="28", type="modern", storytelling_creator="Masahiro Sakurai", graphics_creator="Nintendo", category="fighting", price_game=1.50, year="2019")
game9 = Game(title="Dance Central", code="29", type="modern", storytelling_creator="Harmonix", graphics_creator="Microsoft", category="dance", price_game=1.20, year="2010")
game10 = Game(title="Rock Band Arcade", code="30", type="modern", storytelling_creator="Alex Rigopulos", graphics_creator="Harmonix", category="music", price_game=1.50, year="2011")

# Dance Games
game11 = Game(title="Dance Party Revolution", code="6", type="dance", storytelling_creator="Naomi Carter", graphics_creator="Rhythm Games Inc.", category="rhythm", price_game=3.50, year="2021")
game12 = Game(title="Step Master", code="7", type="dance", storytelling_creator="Kendra Lee", graphics_creator="Step Games Ltd.", category="rhythm", price_game=2.99, year="2020")
game13 = Game(title="Beat Fever", code="8", type="dance", storytelling_creator="Alex Thompson", graphics_creator="Groove Studios", category="rhythm", price_game=4.00, year="2019")
game14 = Game(title="Rhythm Nation", code="9", type="dance", storytelling_creator="Jason Wu", graphics_creator="Arcade Beat Co.", category="rhythm", price_game=3.75, year="2022")
game15 = Game(title="Disco Frenzy", code="10", type="dance", storytelling_creator="Linda Zhang", graphics_creator="Disco Fun LLC", category="rhythm", price_game=3.25, year="2018")

# Classical Games
game16 = Game(title="Space Invaders", code="36", type="classical", storytelling_creator="Tomohiro Nishikado", graphics_creator="Taito", category="shooter", price_game=0.20, year="1978")
game17 = Game(title="Pong", code="37", type="classical", storytelling_creator="Nolan Bushnell", graphics_creator="Atari", category="sports", price_game=0.50, year="1972")
game18 = Game(title="Tetris", code="38", type="classical", storytelling_creator="Alexey Pajitnov", graphics_creator="Elorg", category="puzzle", price_game=0.15, year="1984")
game19 = Game(title="Q*bert", code="39", type="classical", storytelling_creator="Garry Kitchen", graphics_creator="Gottlieb", category="puzzle", price_game=0.30, year="1982")
game20 = Game(title="Dig Dug", code="40", type="classical", storytelling_creator="Masahiro Yamamoto", graphics_creator="Namco", category="puzzle", price_game=0.25, year="1982")

# Shooter Games
game21 = Game(title="Time Crisis", code="11", type="shooter", storytelling_creator="Namco", graphics_creator="Namco", category="shooter", price_game=0.75, year="1995")
game22 = Game(title="House of the Dead", code="12", type="shooter", storytelling_creator="Sega", graphics_creator="Sega", category="shooter", price_game=1.00, year="1996")
game23 = Game(title="Virtua Cop", code="13", type="shooter", storytelling_creator="Yu Suzuki", graphics_creator="Sega", category="shooter", price_game=0.85, year="1994")
game24 = Game(title="Silent Scope", code="14", type="shooter", storytelling_creator="Konami", graphics_creator="Konami", category="shooter", price_game=1.00, year="1999")
game25 = Game(title="Point Blank", code="15", type="shooter", storytelling_creator="Namco", graphics_creator="Namco", category="shooter", price_game=0.50, year="1994")

# Racing Games
game26 = Game(title="Daytona USA", code="16", type="racing", storytelling_creator="Yu Suzuki", graphics_creator="Sega", category="racing", price_game=0.75, year="1994")
game27 = Game(title="Out Run", code="17", type="racing", storytelling_creator="Yu Suzuki", graphics_creator="Sega", category="racing", price_game=0.50, year="1986")
game28 = Game(title="Cruis'n USA", code="18", type="racing", storytelling_creator="Eugene Jarvis", graphics_creator="Midway Games", category="racing", price_game=0.60, year="1994")
game29 = Game(title="Ridge Racer", code="19", type="racing", storytelling_creator="Namco", graphics_creator="Namco", category="racing", price_game=0.70, year="1993")
game30 = Game(title="Mario Kart Arcade GP", code="20", type="racing", storytelling_creator="Nintendo", graphics_creator="Nintendo", category="racing", price_game=1.00, year="2005")

# VR Games
game31 = Game(title="Beat Saber", code="31", type="vr", storytelling_creator="Psyche Studios", graphics_creator="Psyche Studios", category="rhythm", price_game=29.99, year="2018")
game32 = Game(title="VR Chat", code="32", type="vr", storytelling_creator="VRChat Inc.", graphics_creator="VRChat Inc.", category="social", price_game=0.00, year="2017")
game33 = Game(title="Rec Room", code="33", type="vr", storytelling_creator="Against Gravity", graphics_creator="Against Gravity", category="social", price_game=0.00, year="2016")
game34 = Game(title="Half-Life: Alyx", code="34", type="vr", storytelling_creator="Valve", graphics_creator="Valve", category="action", price_game=59.99, year="2020")
game35 = Game(title="Boneworks", code="35", type="vr", storytelling_creator="Stress Level Zero", graphics_creator="Stress Level Zero", category="action", price_game=29.99, year="2019")




# call the method main(), start here
if __name__ == "__main__":
    main()
