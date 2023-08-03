# holbertonschool-AirBnB_clone2
![65f4a1dd9c51265f49d0](https://user-images.githubusercontent.com/98162365/176899920-64b889dc-9e43-4413-b0a4-b1821b53dc2b.png)
## Welcome to the AirBnB clone 2 project!

This is the console /command interpreter for the Holberton Airbnb clone project. The console can be used to store objects in and retrieve objects from a JSON.

<center><h3>Repository Contents by Project Task</h3> </center>

| Tasks | Files | Description |
| ----- | ----- | ------ |
| 0: Authors/README File | [AUTHORS](./AUTHORS) | Project authors |
| 1: Pep8 | N/A | All code is pep8 compliant|
| 2: Unit Testing | [/tests](./tests) | All class-defining modules are unittested |
| 3. Make BaseModel | [/models/base_model.py](./models/base_model.py) | Defines a parent class to be inherited by all model classes|
| 4. Update BaseModel w/ kwargs | [/models/base_model.py](./models/base_model.py) | Add functionality to recreate an instance of a class from a dictionary representation|
| 5. Create FileStorage class | [/models/engine/file_storage.py](./models/engine/file_storage.py) [/models/__init__.py](./models/__init__.py) [/models/base_model.py](./models/base_model.py) | Defines a class to manage persistent file storage system|
| 6. Console 0.0.1 | [console.py](./console.py) | Add basic functionality to console program, allowing it to quit, handle empty lines and ^D |
| 7. Console 0.1 | [console.py](./console.py) | Update the console with methods allowing the user to create, destroy, show, and update stored data |
| 8. Create User class | [console.py](./console.py) [/models/engine/file_storage.py](./models/engine/file_storage.py) [/models/user.py](./models/user.py) | Dynamically implements a user class |
| 9. More Classes | [/models/user.py](./models/user.py) [/models/place.py](./models/place.py) [/models/city.py](./models/city.py) [/models/amenity.py](./models/amenity.py) [/models/state.py](./models/state.py) [/models/review.py](./models/review.py) | Dynamically implements more classes |
| 10. Console 1.0 | [console.py](./console.py) [/models/engine/file_storage.py](./models/engine/file_storage.py) | Update the console and file storage system to work dynamically with all  classes update file storage |
<br>
### Supported classes:
* BaseModel
* User
* State
* City
* Amenity
* Place
* Review

##### Commands
    * create - Creates an instance based on given class

    * destroy - Destroys an object based on class and UUID

    * show - Shows an object based on class and UUID

    * all - Shows all objects the program has access to, or all objects of a given class

    * update - Updates existing attributes an object based on class name and UUID

    * quit - Exits the program (EOF will as well)


##### Alternative Syntax
Users are able to issue a number of console command using an alternative syntax:

	Usage: <class_name>.<command>([<id>[name_arg value_arg]|[kwargs]])
Advanced syntax is implemented for the following commands: 

    * all - Shows all objects the program has access to, or all objects of a given class

	* count - Return number of object instances by class

    * show - Shows an object based on class and UUID

	* destroy - Destroys an object based on class and UUID

    * update - Updates existing attributes an object based on class name and UUID

<br>
To start, navigate to the project folder and enter `./console.py` in the shell.

#### Create
`create <class name>`
Ex:
`create BaseModel`

#### Show
`show <class name> <object id>`
Ex:
`show User my_id`

#### Destroy
`destroy <class name> <object id>`
Ex:
`destroy Place my_place_id`

#### All
`all` or `all <class name>`
Ex:
`all` or `all State`

#### Quit
`quit` or `EOF`

#### Help
`help` or `help <command>`
Ex:
`help` or `help quit`

Additionally, the console supports `<class name>.<command>(<parameters>)` syntax.
Ex:
`City.show(my_city_id)`

* ![GitHub Contributors Image](https://contrib.rocks/image?repo=sandro132/holbertonschool-low_level_programming) 
Miguel Angel Velez Ocampo - <a href="https://github.com/sandro132" target="_blank"> @sandro132</a>
* ![Your Repository's Stats](https://github-readme-stats.vercel.app/api?username=sandro132&show_icons=true)

* ![GitHub Contributors Image](https://contrib.rocks/image?repo=MichiCaballero07/holbertonschool-higher_level_programming) Michel Caballero Granado - <a href="https://github.com/MichiCaballero07" target="_blank"> @MichiCaballero07</a> :genie_woman:![Your Repository's Stats](https://github-readme-stats.vercel.app/api?username=MichiCaballero07&show_icons=true)
