from abc import ABC, abstractmethod
from enum import Enum


class Material(Enum):
    """
    Enum for arcade machine materials.

    This enum defines the different types of materials available
    for the construction of arcade machines.

    """
    
    
    WOOD = "Wood"
    ALUMINUM = "Aluminum"
    CARBON_FIBER = "Carbon Fiber"


class Color(Enum):
    """
    Enum for arcade machine colors.

    This enum defines the different colors that can be applied to arcade machines.
    applied to arcade machines and their lights.
    """
    BLACK = "Black"
    WHITE = "White"
    RED = "Red"
    BLUE = "Blue"
    GREEN = "Green"
    YELLOW = "Yellow"
    PURPLE = "Purple"
    NONE = "No color"


class ArcadeMachine(ABC):
    """This class represents the behavior of an Arcade Machine"""
    

    def __init__(self, material: Material, color: Color, lights: Color, sound: str):
        """
        Initializes the Arcade Machine with material, color, lights, and sound.
          Parameters:
        -----------
        material : Material
            The material of the arcade machine (e.g., wood, aluminum).
        color : Color
            The color of the arcade machine.
        lights : Color
            The color of the arcade machine's lights.
        sound : str
            The sound system used in the arcade machine.
        """
        self._material = material  # Encapsulation (protected attribute)
        self._color = color
        self._lights = lights
        self._sound = sound
        self._games = []  # List for the games added to the machine

    # Abstract method (Abstraction)
    @abstractmethod
    def show_available_games(self):
        """
        Abstract method to display the available games for the arcade machine.
        This method must be implemented by concrete subclasses.
        """

    # Abstract method to verify if a game is valid for this type of machine
    @abstractmethod
    def is_game_valid(self, game):
        """
        Abstract method to verify if a game is valid for this type of arcade machine.
        This method must be implemented by concrete subclasses.

        Parameters:
        -----------
        game : object
            The game object to verify.
        """

    # Add game (Encapsulation)
    def add_game(self, game):
        """
        Adds a game to the list of games installed on the arcade machine.

        Parameters:
        -----------
        game : object
            The game object to add.
        """
        self._games.append(game)

    # Show machine information
    def show_info(self):
        """
        Displays detailed information about the arcade machine, including material, color,
        lights, sound system, and the number of games added.

        Returns:
        --------
        str : A string containing the material, color, lights, sound, and 
        the number of games installed.
        """
        return (f"Material: {self._material.value}, Color: {self._color.value}, "
                f"Lights: {self._lights.value}, Sound: {self._sound}, "
                f"Games: {len(self._games)}")


class ModernArcadeMachine(ArcadeMachine):
    """Concrete class representing a modern arcade machine.
    
    Inherits from:
    --------------
    ArcadeMachine : Abstract base class representing the general behavior of an arcade machine.
    """
    def __init__(self, material: Material, color: Color, lights: Color, sound: str):
        """Initializes the modern arcade machine with material, color, lights, and sound system. 
        inheritance from abstract class"""

        super().__init__(material, color, lights, sound)
        self._controls = "Modern Controls" # Additional attribute for modern controls

    def show_available_games(self):
        """
        Returns a list of available modern games that can be played on the modern arcade machine.
        """
        return ["Fortnite", "Rocket League", "Minecraft", "Call of Duty", "FIFA 22"]

    def is_game_valid(self, game):
        """This method checks if a game is valid for this arcade machine based on its type.
        and return true if the game is modern"""
        return game.type.lower() == "modern"

    def show_info(self):
        """
        Returns a string representation of the object's information, including the controls.
        Returns:
            str: A string representation of the object's information, including the controls.
        """
        return super().show_info() + f", Controls: {self._controls}"


# Concrete class: RetroArcadeMachine (Inheritance)
class RetroArcadeMachine(ArcadeMachine):
    """ Represents a retro arcade machine.
    Args:
        material (Material): The material of the arcade machine.
        color (Color): The color of the arcade machine.
        lights (Color): The color of the lights on the arcade machine.
        sound (str): The sound of the arcade machine.
    Attributes:
        _controls (str): The additional attribute for retro controls.
    Methods:
        show_available_games(): Returns a list of available games.
        is_game_valid(game): Checks if a game is valid for the arcade machine.
        show_info(): Returns the information about the arcade machine. """

    def __init__(self, material: Material, color: Color, lights: Color, sound: str):
        super().__init__(material, color, lights, sound)
        self._controls = "Retro Controls"  # Additional attribute for controls

    def show_available_games(self):
        return ["Pac-Man", "Space Invaders", "Donkey Kong", "Super Mario Bros", "Tetris"]

    def is_game_valid(self, game):
        return game.type.lower() == "retro"

    def show_info(self):
        return super().show_info() + f", Controls: {self._controls}"


class Game:
    """Represents a game in the arcade catalog
    
    Represents a game in the arcade catalog.

    Class Attributes:
    ------------------
    available_games : list
        A class-level list that stores all available games in the catalog.

    Instance Attributes:
    ----------------------
    title : str
        The title of the game.
    code : str
        A unique code associated with the game.
    type : str
        The type of the game, either "modern" or "retro".
    """
    available_games = []  # Available games in the catalog (Class attribute)

    def __init__(self, title, code, type):
        """Initializes a new game instance and adds it to the class-level 
        list of available games.
        """
        self.title = title
        self.code = code
        self.type = type  # "modern" or "retro"
        Game.available_games.append(self)

    @classmethod
    def show_available_games(cls, machine_type):
        """Displays a list of available games for a specified type of arcade machine."""
        print(f"\nAvailable games for {machine_type.capitalize()}:")
        compatible = False
        for game in cls.available_games:
            if game.type.lower() == machine_type.lower():
                print(f"{game.code}. {game.title} (Type: {game.type.capitalize()})")
                compatible = True
        if not compatible:
            print("There are no games available for this type of machine.")


# Client Class
class Customer:
    """
    Represents a customer with their personal information.

    Attributes:
    -----------
    name : str
        The name of the customer.
    address : str
        The address of the customer.
    phone : str
        The phone number of the customer.

    """
    def __init__(self, name, address, phone):
        """Initializes a new customer with the specified name, address, and phone number."""
        self.name = name
        self.address = address
        self.phone = phone

    def __str__(self):
        """Returns a string representation of the customer, including their name,
        address, and phone number.
        """
        return f"Customer: {self.name}, Address: {self.address}, Phone: {self.phone}"


# Class that manages the arcade catalog
class ArcadeCatalog:
    """ Manages the arcade machine catalog and handles customer interactions."""
    def __init__(self):
        """
        Initializes the catalog with no selected machine, customer, or machine type.
        """
        self._cart = None
        self._customer = None
        self._machine_type = None  # Added this attribute to know the machine type

    def add_to_cart(self, machine_type):
        """
        Customizes the selected arcade machine's features and adds it to the cart.

        Parameters:
        -----------
        machine_type : int
            The type of arcade machine (1 for modern, 2 for retro).
        """
        print("\nCustomize the features of your machine:")
        material_option = self.get_option(
            "Materials",
            ["Wood", "Aluminum", "Carbon Fiber"]
        )
        color_option = self.get_option(
            "Colors",
            ["Black", "White", "Red", "Blue", "Green", "Yellow", "Purple"]
        )
        lights_option = self.get_option(
            "Light Colors",
            ["White", "Red", "Blue", "Green", "Yellow", "Purple", "None"]
        )
        sound = self.get_sound()

        material = self.customize_material(material_option)
        color = self.customize_color(color_option)
        lights = self.customize_light_color(lights_option)

        if machine_type == 1:
            self._cart = ModernArcadeMachine(material, color, lights, sound)
            self._machine_type = "modern"  # Define machine type
        elif machine_type == 2:
            self._cart = RetroArcadeMachine(material, color, lights, sound)
            self._machine_type = "retro"  # Define machine type

    def choose_machine(self, machine_type):
        """
        Selects the type of arcade machine and starts customization.
        receive the parameter machine_type (1 for modern, 2 for retro)
        """
        if machine_type == 1:
            print("\nYou have selected a Modern Arcade Machine.")
            self.add_to_cart(machine_type)
        elif machine_type == 2:
            print("\nYou have selected a Retro Arcade Machine.")
            self.add_to_cart(machine_type)
        else:
            print("\nInvalid option.")

    def customize_material(self, material_option):
        """Customizes the material of the arcade machine based on the selected option."""
        if material_option == 1:
            return Material.WOOD
        elif material_option == 2:
            return Material.ALUMINUM
        elif material_option == 3:
            return Material.CARBON_FIBER
        else:
            return "Invalid material"

    def customize_color(self, color_option):
        """
        Customizes the color of the arcade machine based on the selected option.
        """
        colors = {
            1: Color.BLACK,
            2: Color.WHITE,
            3: Color.RED,
            4: Color.BLUE,
            5: Color.GREEN,
            6: Color.YELLOW,
            7: Color.PURPLE
        }
        return colors.get(color_option, "Invalid color")

    def customize_light_color(self, lights_option):
        """
        Customizes the color of the arcade machine's lights based on the selected option.
        """
        light_colors = {
            1: Color.WHITE,
            2: Color.RED,
            3: Color.BLUE,
            4: Color.GREEN,
            5: Color.YELLOW,
            6: Color.PURPLE,
            7: Color.NONE
        }
        return light_colors.get(lights_option, "Invalid light color")

    def get_option(self, category, options):
        """
        Displays a list of options for a specific category and prompts the user to select one.
        """
        print(f"\n{category}:")
        for idx, option in enumerate(options, start=1):
            print(f"{idx}. {option}")
        while True:
            try:
                selection = int(input(f"Select an option for {category}: "))
                if 1 <= selection <= len(options):
                    return selection
                else:
                    print(f"Please select a number between 1 and {len(options)}.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def get_sound(self):
        """
        Prompts the user to specify whether they want to 
        add sound or speakers to the arcade machine.

        Returns:
        -----------
        str
            "With sound" if the user wants sound, otherwise "Without sound".
        """
        while True:
            sound = input("\nWould you like to add sound or speakers? (y/n): ").lower()
            if sound == 'y':
                return "With sound"
            elif sound == 'n':
                return "Without sound"
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

    def show_games(self):
        """
        Displays the list of available games for the selected arcade machine.

        If no machine is selected, prompts the user to select a machine first.
        """
        if self._cart:
            games = self._cart.show_available_games()
            print("\nAvailable games for this machine:")
            for game in games:
                print(f"- {game}")
        else:
            print("\nYou must first select a machine.")

    def add_game_by_code(self, code):
        """
        Adds a game to the selected arcade machine by its code.

        Parameters:
        -----------
        code : str
            The unique code associated with the game.
        """
        for game in Game.available_games:
            if game.code == code:
                if self._cart.is_game_valid(game):  # Check if the game is valid for the machine
                    self._cart.add_game(game)
                    print(f"\nGame '{game.title}' added to the machine.")
                else:
                    print(f"\nThis game is not valid for a {self._cart.__class__.__name__} machine.")
                return
        print("\nInvalid game code.")

    def add_games(self):
        """
        Allows the user to add games to the selected arcade machine by code.

        Continues to prompt the user to add games until they choose to stop.
        """
        while True:
            add_game = input("\nDo you want to add a game by code? (y/n): ").lower()
            if add_game == "y":
                Game.show_available_games(self._machine_type)
                try:
                    game_code = int(input("Enter the code of the game you want to add: "))
                    self.add_game_by_code(game_code)
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            elif add_game == "n":
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

    def complete_purchase(self, name, address, phone):
        """
        Completes the purchase by saving customer information and displaying the final details.
        """
        self._customer = Customer(name, address, phone)
        print("\nPurchase completed. Machine information:")
        print(self._cart.show_info())
        print("\nCustomer information:")
        print(self._customer)

