# HBNB

This is the console /command interpreter for the Holberton Airbnb clone project. The console can be used to store objects in and retrieve objects from a JSON.

### Supported classes:
* BaseModel
* User
* State
* City
* Amenity
* Place
* Review

### Commands:
* create - create an object
* show - show an object (based on id)
* destroy - destroy an object
* all - show all objects, of one type or all types
* quit/EOF - quit the console
* help - see descriptions of commands

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

* ![GitHub Contributors Image](https://github.com/JDaniel26-Bory/holbertonschool-AirBnB_clone) - <a href="https://github.com/MichiCaballero07" target="_blank"> @MichiCaballero07</a> :genie_woman:![Your Repository's Stats](https://github-readme-stats.vercel.app/api?username=MichiCaballero07&show_icons=true)
