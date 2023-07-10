# ![image](https://github.com/YanielRamos/holbertonschool-AirBnB_clone/assets/122760700/9517fe9f-a64d-4418-99dc-cfd2687fc350)


### Contents

- [Description](#Description)
- [Environment](#Environment)
- [Requirements](#Requirements)
- [Repo Contents](#Repo)
- [Installation](#Installation)
- [Usage](#Usage)
- [Built with](#Built-with)
- [Acknowledgements](#Acknowledgements)

## **Description**
* This is the first phase of a four phase project, to create a basic clone of the AirBnB web app. In this first phase a basic console was created using the Cmd Python module, to manage the objects of the whole project, being able to implement the methods create, show, update, all, and destroy to the existing classes and subclasses.


### **Environment**
  - Language: Python
  - OS: Ubuntu 20.04
  - Compiler: python3 (version 3.8.5)
  - Style guideines: pycodestyle (version 2.7.*)


## **Requirements**
* Knowledge in python3, how to use a command line interpreter, a computer with Ubuntu 20.04, python3 and pep8 style corrector.

## **Repo Contents**
* This repository constains the following files:

|   **File**   |   **Description**   |
| -------------- | --------------------- |
|[AUTHORS](./AUTHORS) | Contains info about authors of the project |
|[base_model.py](./models/base_model.py) | Defines BaseModel class (parent class), and methods |
|[user.py](./models/user.py) | Defines subclass User |
|[amenity.py](./models/amenity.py) | Defines subclass Amenity |
|[city.py](./models/city.py)| Defines subclass City |
|[place.py](./models/place.py)| Defines subclass Place |
|[review.py](./models/review.py) | Defines subclass Review |
|[state.py](./models/state.py) | Defines subclass State |
|[file_storage.py](./models/engine/file_storage.py) | Creates new instance of class, serializes and deserializes data |
|[console.py](./console.py) | creates object, retrieves object from file, does operations on objects, updates attributes of object and destroys object |


## Usage :wrench:

|   **Method**   |   **Description**   |
| -------------- | --------------------- |
|[create](./console.py) | Creates object of given class |
|[show](./console.py) | Prints the string representation of an instance based on the class name and id |
|[all](./console.py) | Prints all string representation of all instances based or not on the class name |
|[update](./console.py) | Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file) |
|[destroy](./console.py)| Deletes an instance based on the class name and id (save the change into the JSON file) |
|[count](./console.py)| Retrieve the number of instances of a class |
|[help](./console.py)| Prints information about specific command |
|[quit/ EOF](./console.py)| Exit the program |


### Acknowledgements :raised_hands:
To all the peers that contribuited with their knowledge

### Authors :fountain_pen:
* Yaniel Ramos
* Jose Alvarez
