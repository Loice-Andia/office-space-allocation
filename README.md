[![Build Status](https://travis-ci.org/andela-lolo/office-space-allocation.svg?branch=dev)](https://travis-ci.org/andela-lolo/office-space-allocation)
[![Coverage Status](https://coveralls.io/repos/github/andela-lolo/office-space-allocation/badge.svg?branch=dev)](https://coveralls.io/github/andela-lolo/office-space-allocation?branch=dev)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/32d1e69c23fa419083d6fea338af7a7b)](https://www.codacy.com/app/loice-andia/office-space-allocation?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=andela-lolo/office-space-allocation&amp;utm_campaign=Badge_Grade)

# Amity Room Allocation

Amity has rooms which can be offices or living spaces. An office can occupy a maximum of 6 people. A living space can inhabit a maximum of 4 people.

This is a console application that allocates offices and living spaces at Amity to Andela employees

## Installation

Clone this repo 

```
git clone https://github.com/andela-lolo/office-space-allocation.git
```

Navigate to the folder

```cd office_space_allocation```

Set up a virtualenv then Install packages required

```pip install  -r requirements.txt```

## Launching the Program

```python app.py -i```

## Running the tests

Run ``` tox ```


## Usage

1. ```create_room <room_name>...``` Create a new room or several new rooms. You must specify whether it is a living space or an office as well as the room name. You may add several rooms of the same type at once. Example: ``` create_room Hogwarts Valhalla Krypton ```

2. ```add_person < first_name> <last_name> (Fellow|Staff)``` Add a new person. You must specify their first name, last name and whether they are a fellow or staff member. Optionally, you can indicate whether or not they want space with "Y" or "N". If you indicate that the person wants space, they are automatically allocated a room. Staff members can only be allocated an office while fellows can only be allocated a living space using this command. If there are no rooms in the system, the person will not be added. Example: ```add_person Ada Lovelace Fellow Y```

3. ```reallocate_person <person_name> <new_room_name>``` Using this command, you can allocate an already allocated person another room, or allocate a previously unallocated person a room. You must specify the person's employee ID as well as the room to be allocated. Note that staff members cannot be allocated living spaces, while fellows can be allocated offices using this command. Example: ```reallocate_person Ada Hogwarts```

4. ```remove_peron <person_name>``` This command removes a person completely from the system. Example: ```remove_person Ada```

5. ```load_people <filename>``` This command allows the user to specify a text file containing people's information. The people are then added to the system. See ```try.txt``` for sample data.

6. ```print_allocations [-o <filename>]``` Print a list of occupants per room to the screen, and optionally to a text file.

7. ```print_unallocated [-o <filename>]``` Print a list of unallocated people to the screen, and optionally to a text file.

8. ```print_room <room_name>``` Print a list of people occupying a particular room. Example: ```print_room Hogwarts```

9. ```save_state [--db=sqlite_database]``` Save all the data stored in the application in a database. Optionally, you can specify the name of the database. Example: ```save_state --db=amity.db```

10. ```load_state <sqlite_database>``` Load data into the application from a specified database. Example: ```load_state amity.db```
