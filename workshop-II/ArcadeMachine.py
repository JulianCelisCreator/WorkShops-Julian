"""
This module contains class definitions for arcade machines, including abstract and concrete classes.
It also includes a class for games and a class for managing the arcade catalog.
The module provides functionality for customizing arcade machines, adding games, and completing purchases.


Author: Julian David Celis Giraldo <jdcelisg@udistrital.edu.co>

This file is part of PyCalculator-UD.

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
    
class Glasses(Enum):
    """
    Enum for glasses of VirtualRealityMachine.

    This enum defines the different types of glasses available
    for glasses of VirtualRealityMachine.

    """

    OCULUS_RIFT = "Oculus Rift"
    HTC_Vive = "HTC Vive"
    VALVE_INDEX = "Valve Index"

class Resolution(Enum):
    """
    Enum for arcade machine materials.

    This enum defines the different types of materials available
    for the construction of arcade machines.

    """

    FULLHD = "1920x1080"
    QHD = "2560x1440"
    UHD = "3840x2160"

class Sound(Enum):
    """
    Enum for arcade machine materials.

    This enum defines the different types of materials available
    for the construction of arcade machines.

    """

    MONO = "mono"
    ESTEREO = "Estereo"
    SURROUND = "Surround"
    
class SimRacing(Enum):
    """
    Enum for arcade machine materials.

    This enum defines the different types of simRacing available
    for the construction of Racing machines.

    """

    PROFESIONAL = "forcefeedback steering wheel and pedals"
    AMATEUR = "digital stering wheel and pedals"
    STARTER = "analog stering wheel and pedals"


class Color(Enum):
    """
    Enum for arcade machine colors.

    This enum defines the different colors that can be applied to arcade machines.
    applied to arcade machines and their lights.
    """
    MULTICOLOR = "Multicolor"
    WHITE = "White"
    RED = "Red"
    BLUE = "Blue"
    GREEN = "Green"
    YELLOW = "Yellow"
    PURPLE = "Purple"
    DEFAULT = "Default"


class ArcadeMachine(ABC):
    """This class represents the behavior of an Arcade Machine"""
    
    def __init__(self, material: Material, color: Color, lights: Color,
                 sound: Sound, controls: str, dimensions: str,
                 weight: float, power_consumption: float,
                 memory: str, processor: str, base_price: float):
        self._material = material  # Encapsulation (protected attribute)
        self._color = color
        self._lights = lights
        self._sound = sound
        self._games = []  # List for the games added to the machine
        self._controls = controls
        self._dimensions = dimensions
        self._weight = weight
        self._power_consumption = power_consumption
        self._memory = memory
        self._processor = processor
        self._base_price = base_price
        
    @abstractmethod
    def show_available_games(self):
        """ Abstract method to display the available games for the arcade machine. """

    @abstractmethod
    def is_game_valid(self, game):
        """ Abstract method to verify if a game is valid for this type of arcade machine. """

    def add_game(self, game):
        """ Adds a game to the list of games installed on the arcade machine. """
        self._games.append(game)

    def show_info(self):
        return (f"Máquina Arcade:\n"
                f"Material: {self._material.value}\n"
                f"Color: {self._color.value}\n"
                f"Luces: {self._lights.value}\n"
                f"Sonido: {self._sound}\n"
                f"Controles: {self._controls}\n"
                f"Dimensiones: {self._dimensions}\n"
                f"Peso: {self._weight}\n"
                f"Consumo de energía: {self._power_consumption}\n"
                f"Memoria: {self._memory}\n"
                f"Procesador: {self._processor}\n"
                f"Precio base: ${self._base_price:.2f}")

class ModernArcadeMachine(ArcadeMachine):
    """Concrete class representing a modern arcade machine.
    
    Inherits from:
    --------------
    ArcadeMachine : Abstract base class representing the general behavior of an arcade machine.
    """
    def __init__(self, material: Material, color: Color, lights: Color,
                 sound: Sound, dimensions: str, weight: float,
                 power_consumption: float, memory: str, processor: str,
                 base_price: float):
        """Initializes the modern arcade machine with material, color, lights, and sound system."""
        
        # Llamar al constructor de la clase base (ArcadeMachine)
        super().__init__(material, color, lights, sound, controls="Modern Controls",
                         dimensions=dimensions, weight=weight,
                         power_consumption=power_consumption,
                         memory=memory, processor=processor, base_price=base_price)

    def show_available_games(self):
        """
        Returns a list of available modern games that can be played on the modern arcade machine.
        Automatically filters the available games from the Game class by type 'modern'.
        """
        # Filter type games 'modern'
        modern_games = [game.title for game in Game.available_games if game.type.lower() == "modern"]
        return modern_games

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
    
    def __str__(self):
        return (f"Modern Arcade Machine:\n"
                f"Material: {self._material.value}\n"
                f"controls: {self._controls}\n"
                f"Color: {self._color.value}\n"
                f"Lights: {self._lights.value}\n"
                f"Sound: {self._sound.value}\n"
                f"Dimensions: {self._dimensions}\n"
                f"Weight: {self._weight}\n"
                f"Power Consumption: {self._power_consumption}\n"
                f"Memory: {self._memory}\n"
                f"Processor: {self._processor}\n"
                f"Base Price: ${self._base_price:.2f}")

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
    def __init__(self, material: Material, color: Color, lights: Color, sound: Sound, power_consumption: float,dimensions: str, weight: float, memory: str, processor: str, base_price: float):
        """Initializes the retro arcade machine with material, color, lights, and sound system."""
        # Llamar al constructor de la clase base (ArcadeMachine)
        super().__init__(material, color, lights, sound, controls="Retro Controls", 
                         dimensions=dimensions, weight=weight, power_consumption=power_consumption, 
                         memory=memory, processor=processor, base_price=base_price)
    def show_available_games(self):
        """
        Returns a list of available modern games that can be played on the modern arcade machine.
        Automatically filters the available games from the Game class by type 'modern'.
        """
        # Filter type games 'modern'
        retro_games = [game.title for game in Game.available_games if game.type.lower() == "retro"]
        return retro_games

    def is_game_valid(self, game):
        return game.type.lower() == "retro"

    def show_info(self):
        return super().show_info() + f", Controls: {self._controls}"
    
class DanceRevolutionMachine(ArcadeMachine):
    """Represents a Dance Revolution arcade machine."""

    def __init__(self, material: Material, color: Color, lights: Color, sound: Sound, 
                 dimensions: str, weight: float, power_consumption: float, 
                 memory: str, processor: str, base_price: float, difficulties: str, 
                 arrow_cardinalities: str, controls_price: float):
        
        super().__init__(material, color, lights, sound, controls="Dance Revolution Controls", 
                         dimensions=dimensions, weight=weight, power_consumption=power_consumption, 
                        memory=memory, processor=processor, 
                         base_price=base_price)

        self._difficulties = difficulties
        self._arrow_cardinalities = arrow_cardinalities
        self._controls_price = controls_price
        
    def show_available_games(self):
        """
        Returns a list of available modern games that can be played on the modern arcade machine.
        Automatically filters the available games from the Game class by type 'modern'.
        """
        # Filter type games 'modern'
        retro_games = [game.title for game in Game.available_games if game.type.lower() == "dance"]
        return retro_games

    def is_game_valid(self, game):
        return game.type.lower() == "dance"

    def show_info(self):
        return super().show_info() + f", Controls: {self._controls}"

class ClassicalArcadeMachine(ArcadeMachine):
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
    def __init__(self, material: Material, color: Color, lights: Color, sound: Sound, dimensions: str, weight: float, power_consumption: float, memory: str, processor: str, base_price: float, make_vibration: bool, sound_record_alert:bool):
        """Initializes the retro arcade machine with material, color, lights, and sound system."""
        # Llamar al constructor de la clase base (ArcadeMachine)
        super().__init__(material, color, lights, sound, controls="Classical Controls", 
                         dimensions=dimensions, weight=weight, power_consumption= power_consumption, 
                         memory=memory, processor=processor, base_price=base_price)
        
        self._make_vibration = make_vibration
        self._sound_record_alert = sound_record_alert
        
    def show_available_games(self):
        """
        Returns a list of available modern games that can be played on the modern arcade machine.
        Automatically filters the available games from the Game class by type 'modern'.
        """
        # Filter type games 'modern'
        retro_games = [game.title for game in Game.available_games if game.type.lower() == "classical"]
        return retro_games

    def is_game_valid(self, game):
        return game.type.lower() == "classical"

    def show_info(self):
        return super().show_info() + f", Controls: {self._controls}"

class ShootingMachine(ArcadeMachine):
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
    def __init__(self, material: Material, color: Color, lights: Color, sound: Sound, dimensions: str, weight: float, power_consumption: float, memory: str, processor: str, base_price: float, gun_color : Color):
        """Initializes the retro arcade machine with material, color, lights, and sound system."""
        # Llamar al constructor de la clase base (ArcadeMachine)
        super().__init__(material, color, lights, sound, controls="Shooting Controls",
                         dimensions=dimensions, weight=weight, power_consumption= power_consumption, 
                         memory=memory, processor=processor, base_price=base_price)
        self._gun_color = gun_color
        
        
    def show_available_games(self):
        """
        Returns a list of available modern games that can be played on the modern arcade machine.
        Automatically filters the available games from the Game class by type 'modern'.
        """
        # Filter type games 'modern'
        retro_games = [game.title for game in Game.available_games if game.type.lower() == "shooter"]
        return retro_games

    def is_game_valid(self, game):
        return game.type.lower() == "shooter"

    def show_info(self):
        return super().show_info() + f", Controls: {self._controls}"


class RacingMachine(ArcadeMachine):
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
    def __init__(self, material: Material, color: Color, lights: Color, sound: Sound, dimensions: str, weight: float, power_consumption: float, memory: str, processor: str, base_price: float, type_sim_racing: SimRacing, add_gearbox: bool):
        """Initializes the retro arcade machine with material, color, lights, and sound system."""
        # Llamar al constructor de la clase base (ArcadeMachine)
        super().__init__(material, color, lights, sound, controls="SimRacing Controls", 
                         dimensions=dimensions, weight=weight, power_consumption=power_consumption, 
                         memory=memory, processor=processor, base_price=base_price)
        self._type_sim_racing = type_sim_racing
        self._add_gearbox = add_gearbox
        
        
    def show_available_games(self):
        """
        Returns a list of available modern games that can be played on the modern arcade machine.
        Automatically filters the available games from the Game class by type 'modern'.
        """
        # Filter type games 'modern'
        retro_games = [game.title for game in Game.available_games if game.type.lower() == "racing"]
        return retro_games

    def is_game_valid(self, game):
        return game.type.lower() == "racing"

    def show_info(self):
        return super().show_info() + f", Controls: {self._controls}"
    
class VirtualRealityMachine(ArcadeMachine):
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
    def __init__(self, material: Material, color: Color, lights: Color, sound: Sound, dimensions: str, weight: float, power_consumption: float, memory: str, processor: str, base_price: float, glasses_type: Glasses, glasses_resolution: Resolution, glasses_price: float):
        """Initializes the retro arcade machine with material, color, lights, and sound system."""
        # Llamar al constructor de la clase base (ArcadeMachine)
        super().__init__(material, color, lights, sound, controls="VR Glasses", 
                         dimensions=dimensions, weight=weight, power_consumption=power_consumption, 
                         memory=memory, processor=processor, base_price=base_price)
        self._glasses_type = glasses_type
        self._glasses_resolution = glasses_resolution
        self._glasses_price = glasses_price
        
        
    def show_available_games(self):
        """
        Returns a list of available modern games that can be played on the modern arcade machine.
        Automatically filters the available games from the Game class by type 'modern'.
        """
        # Filter type games 'modern'
        retro_games = [game.title for game in Game.available_games if game.type.lower() == "vr"]
        return retro_games

    def is_game_valid(self, game):
        return game.type.lower() == "vr"

    def show_info(self):
        return super().show_info() + f", Controls: {self._controls}"
    
class ArcadeMachineBuilder:
    def __init__(self):
        self._material = Material.WOOD
        self._color = Color.DEFAULT
        self._lights = Color.DEFAULT
        self._sound = Sound.MONO
        
        # Inicializar atributos de la máquina
        self._dimensions = ""
        self._weight = 0
        self._power_consumption = 0
        self._memory = ""
        self._processor = ""
        self._base_price = 0
        
    def set_attributes(self, defaults):
        """Configura los atributos de la máquina con los valores predeterminados."""
        self._dimensions = defaults['dimensions']
        self._weight = defaults['weight']
        self._power_consumption = defaults['power_consumption']
        self._memory = defaults['memory']
        self._processor = defaults['processor']
        self._base_price = defaults['base_price']
            
    def set_increases(self, increase_weight: float, increase_power: float, increase_price: float):
        """Configura los atributos de la máquina con los valores predeterminados."""
        self._weight *= increase_weight  # Aumentar el peso
        self._power_consumption *= increase_power  # Aumentar el consumo de energía
        self._base_price *= increase_price  # Aumentar el precio
        return


    def set_material(self, material: Material):
        self._material = material
        return self

    def set_color(self, color: Color):
        self._color = color
        return self

    def set_lights(self, lights: Color):
        self._lights = lights
        return self

    def set_sound(self, sound: Sound):
        self._sound = sound
        return self

    def set_controls(self, controls: str):
        self._controls = controls
        return self

    def set_dimensions(self, dimensions: str):
        self._dimensions = dimensions
        return self

    def set_weight(self, weight: float):
        self._weight = weight
        return self

    def set_power_consumption(self, power_comsumption: float):
        self._power_consumption = power_comsumption
        return self

    def set_memory(self, memory: str):
        self._memory = memory
        return self

    def set_processor(self, processor: str):
        self._processor = processor
        return self

    def set_base_price(self, price: float):
        self._base_price = price
        return self
    
    def build_modern(self) -> ModernArcadeMachine:
        return ModernArcadeMachine(self._material, self._color, self._lights,
                                   self._sound, self._dimensions,
                                   self._weight, self._power_consumption,
                                   self._memory, self._processor, self._base_price)
        
    def build_retro(self) -> RetroArcadeMachine:
        return RetroArcadeMachine(self._material, self._color, self._lights,
                                   self._sound, self._dimensions,
                                   self._weight, self._power_consumption,
                                   self._memory, self._processor, self._base_price)
    # Dance Revolution Machine setter
    def set_difficulties(self, difficulties: str):
        self._difficulties = difficulties
        return self
    
    def set_arrow_cardinalities(self, arrow_cardinalities: str):
        self._arrow_cardinalities = arrow_cardinalities
        return self
    
    def set_controls_price(self, controls_price: float):
        self._controls_price = controls_price
        return self
    
    def build_dance(self) -> DanceRevolutionMachine:
        return DanceRevolutionMachine(self._material, self._color, self._lights,
                                   self._sound, self._dimensions,
                                   self._weight, self._power_consumption,
                                   self._memory, self._processor, self._base_price, self._difficulties, self._arrow_cardinalities , self._controls_price)
    # Classical Machine Setter
    def set_make_vibration(self, make_vibration: bool):
        self._make_vibration = make_vibration
        return self
    def set_sound_record_alert(self, sound_record_alert: bool):
        self._sound_record_alert = sound_record_alert
        return self
    
    def build_classical(self) -> ClassicalArcadeMachine:
        return ClassicalArcadeMachine(self._material, self._color, self._lights,
                                   self._sound, self._dimensions,
                                   self._weight, self._power_consumption,
                                   self._memory, self._processor, self._base_price, self._make_vibration, self._sound_record_alert)
    # Shooting Machine Setter
    
    def set_gun_color(self, gun_color: Color):
        self._gun_color = gun_color
        return self
    
    def build_shooting(self) -> ShootingMachine:
        return ShootingMachine(self._material, self._color, self._lights,
                                   self._sound, self._dimensions,
                                   self._weight, self._power_consumption,
                                   self._memory, self._processor, self._base_price, self._gun_color)
    # Racing Machine Setter
    
    def set_type_sim_racing(self, type_sim_racing: SimRacing):
        self._type_sim_racing = type_sim_racing
        return self
    
    def set_add_gearbox(self, add_gearbox: bool):
        self._add_gearbox = add_gearbox
        return self
    
    def build_racing(self) -> RacingMachine:
        return RacingMachine(self._material, self._color, self._lights,
                                   self._sound, self._dimensions,
                                   self._weight, self._power_consumption,
                                   self._memory, self._processor, self._base_price, self._type_sim_racing, self._add_gearbox)
    # Virtual Reality Machine Setter
    def set_glasses_type(self, glasses_type: Glasses):
        self._glasses_type = glasses_type
        return self
    
    def set_glasses_resolution(self, glasses_resolution: Resolution):
        self._glasses_resolution = glasses_resolution
        return self
    
    def glasses_price(self, glasses_price: float):
        self._glasses_price = glasses_price
        return self
    
    def build_vr(self) -> VirtualRealityMachine:
        return VirtualRealityMachine(self._material, self._color, self._lights,
                                   self._sound, self._dimensions,
                                   self._weight, self._power_consumption,
                                   self._memory, self._processor, self._base_price, self._glasses_type, self._glasses_resolution, self._glasses_price)
    
class ArcadeMachineFactory:
    """Clase Factory para crear máquinas arcade."""
    @staticmethod
    def create_arcade_machine(machine_type, builder):
        if machine_type == "modern":
            return builder.build_modern()
        elif machine_type == "retro":
            return builder.build_retro()
        if machine_type == "classical":
            return builder.build_modern()
        elif machine_type == "dance":
            return builder.build_retro()
        else:
            raise ValueError("Tipo de máquina no válido.")
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

    def __init__(self, title, code, type:str,storytelling_creator:str, graphics_creator:str, category:str, price_game: float, year:str ):
        """Initializes a new game instance and adds it to the class-level 
        list of available games.
        """
        self._title = title
        self._code = code
        self._type = type 
        self._storytelling_creator = storytelling_creator
        self.graphics_creator = graphics_creator
        self._category = category
        self._price_game = price_game
        self._year = year
        Game.available_games.append(self)

    @staticmethod
    def show_available_games(machine_type):
        """Show games compatible with the selected machine type."""
        print(f"\nAvailable games for {machine_type.capitalize()} Machines:")
        for game in Game.available_games:
            if game._type.lower() == machine_type.lower():
                print(f"- Code: {game._code}, Title: {game._title}")
    
    

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
       pass

    def choose_machine(self, machine_type):
        """
        Selects the type of arcade machine and starts customization.
        receive the parameter machine_type (1 for modern, 2 for retro)
        """
        if machine_type == 'modern':
            print("\nYou have selected a Modern Arcade Machine.")
            self.add_to_cart(machine_type)
        elif machine_type == 2:
            print("\nYou have selected a Retro Arcade Machine.")
            self.add_to_cart(machine_type)
        else:
            print("\nInvalid option.")

    def customize_material(self, material_option):
        """Customizes the material of the arcade machine based on the selected option."""
        if material_option == "wood":
            return Material.WOOD
        elif material_option == "aluminum":
            return Material.ALUMINUM
        elif material_option == "fiber":
            return Material.CARBON_FIBER
        else:
            return "Invalid material"
    def color_options(self):
        color_option = self.get_option(
            "Colors",
            [color.value for color in Color]
        )
        return color_option

    def customize_color(self, color_option):
        """
        Customizes the color of the arcade machine based on the selected option.
        """
        colors = {
            1: Color.MULTICOLOR,
            2: Color.WHITE,
            3: Color.RED,
            4: Color.BLUE,
            5: Color.GREEN,
            6: Color.YELLOW,
            7: Color.PURPLE
            
        }
        return colors.get(color_option, "Invalid color")
    def light_options(self):
        lights_option = self.get_option(
            "Light Colors",
            [color.value for color in Color]
        )
        return lights_option
    def customize_light_color(self, lights_option):
        """
        Customizes the color of the arcade machine's lights based on the selected option.
        """
        light_colors = {
            1: Color.MULTICOLOR,
            2: Color.RED,
            3: Color.BLUE,
            4: Color.GREEN,
            5: Color.YELLOW,
            6: Color.PURPLE,
            8: Color.DEFAULT
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

    
    def add_game_by_code(self, game_code):
        """Adds a game to the arcade machine by game code, ensuring compatibility with machine type."""
        if not self._cart:
            print("\nYou need to add a machine to your cart first.")
            return

        for game in Game.available_games:
            if game._code == game_code and game._type == self._machine_type:
                self._cart.add_game(game)
                print(f"\nGame '{game._title}' added to your {self._machine_type} machine.")
                return
        print("\nInvalid game code or incompatible game for this machine type.")

    def complete_purchase(self, name, address, phone):
        """Completes the purchase by saving customer information and displaying final details."""
        self._customer = Customer(name, address, phone)
        print("\nPurchase completed. Machine information:")
        print(self._cart.show_info())
        print("\nCustomer information:")
        print(self._customer)
