# holbertonschool-AirBnB_clone
holbertonschool-AirBnB_clone

# AirBnB Console

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
