# AirBnB Console
The AirBnB Console is a command-line application designed to manage AirBnB-like objects. It provides a user-friendly interface for creating, displaying, updating, and deleting instances of various classes such as BaseModel, User, State, City, Amenity, Place, and Review.

Features
Create Instances: You can create new instances of different classes and save them to the JSON file.
Display Information: The console allows you to view detailed information about specific instances based on their class name and ID.
Delete Instances: You can delete instances by specifying their class name and ID, with the changes being automatically saved to the JSON file.
Listing Instances: The console provides the option to list all instances or filter them by class name.
Update Attributes: You can update the attributes of instances by specifying their class name, ID, attribute name, and new value. The changes are saved to the JSON file.

## Description

This project implements a console-based application for managing AirBnB-like objects. It provides functionalities such as creating instances, displaying information, updating attributes, and deleting instances. The data is stored in JSON files.

## Installation

1. Clone the repository:

- `$ git clone https://github.com/TheWhiteMachine/holbertonschool-AirBnB_clone.git`

2. Navigate to the project directory:

## Usage
To start the AirBnB console, run the following command: ./console.py

Once the console is running, you can use the following commands:

- `quit`: Exits the program.
- `create <class_name>`: Creates a new instance of the specified class and saves it to the JSON file.
- `show <class_name> <id>`: Displays the string representation of an instance based on the class name and ID.
- `destroy <class_name> <id>`: Deletes an instance based on the class name and ID and saves the changes to the JSON file.
- `all` or `all <class_name>`: Displays the string representation of all instances or all instances of a specific class.
- `update <class_name> <id> <attribute_name> "<attribute_value>"`: Updates the attribute of an instance based on the class name and ID. The changes are saved to the JSON file.

## Available Classes
- `BaseModel`
- `User`
- `State`
- `City`
- `Amenity`
- `Place`
- `Review`

## Project Structure
The project follows the following structure:

- console.py: The main entry point of the console application.
- models/: Contains the classes representing AirBnB objects.
- models/base_model.py: Defines the BaseModel class, from which other classes inherit.
- models/state.py: Defines the State class.
- models/city.py: Defines the City class.
- models/amenity.py: Defines the Amenity class.
- models/place.py: Defines the Place class.
- models/review.py: Defines the Review class.
- models/user.py: Defines the User class.
- models/engine/: Contains the storage engine for persisting data.
- models/engine/file_storage.py: Implements the FileStorage class for storing data in JSON files.
- tests/: Contains unit tests for the project.
