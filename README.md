# checkpoint1
Office Space Allocation

Amity has rooms which can be offices or living spaces. An office can occupy a maximum of 6 people. A living space can inhabit a maximum of 4 people.

A person to be allocated could be a fellow or staff. Staff cannot be allocated living spaces. Fellows have a choice to choose a living space or not.

This system will be used to automatically allocate spaces to people at random.

## Launching the Program
Run ```python setup.py -i```

## Usage
1. ```create_room (Living|Office) <room_name>...``` Create a new room or several new rooms. You must specify whether it is a living space or an office as well as the room name. You may add several rooms of the same type at once. Example: ``` create_room Office Hogwarts Valhalla Krypton ```

2. ```add_person < first_name> <last_name> (Fellow|Staff)``` Add a new person. You must specify their first name, last name and whether they are a fellow or staff member. Optionally, you can indicate whether or not they want space with "Y" or "N". If you indicate that the person wants space, they are automatically allocated a room. Staff members can only be allocated an office while fellows can only be allocated a living space using this command. If there are no rooms in the system, the person will not be added. Example: ```add_person Ada Lovelace Fellow Y```

3. ```reallocate_person <employee_id> <new_room_name>``` Using this command, you can allocate an already allocated person another room, or allocate a previously unallocated person a room. You must specify the person's employee ID as well as the room to be allocated. Note that staff members cannot be allocated living spaces, while fellows can be allocated offices using this command. Example: ```reallocate_person 123456 Hogwarts```

4. ```load_people <filename>``` This command allows the user to specify a text file containing people's information. The people are then added to the system. See ```people.txt``` for sample data.

5. ```print_allocations [-o <filename>]``` Print a list of occupants per room to the screen, and optionally to a text file.

6. ```print_unallocated [-o <filename>]``` Print a list of unallocated people to the screen, and optionally to a text file.

7. ```print_room <room_name>``` Print a list of people occupying a particular room. Example: ```print_room Hogwarts```

8. ```save_state [--db=sqlite_database]``` Save all the data stored in the application in a database. Optionally, you can specify the name of the database. Example: ```save_state --db=amity.db```

9. ```load_state <sqlite_database>``` Load data into the application from a specified database. Example: ```load_state amity.db```
