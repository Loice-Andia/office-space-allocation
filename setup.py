#!/usr/bin/env python
"""
This example uses docopt with the built in cmd module to demonstrate an
interactive command application.
Usage:
    amity create_room <room_name>...
    amity add_person <first_name> <last_name> (Fellow|Staff) [<wants_accomodation>]
    amity reallocate_person <person_identifier> <new_room_name>
    amity load_people <filename>
    amity print_allocations [-o <filename>]
    amity print_unallocated [-o <filename>]
    amity print_room <room_name>
    amity save_state [--db=sqlite_database]
    amity load_state <sqlite_database>
    amity (-i | --interactive)
    amity (-h | --help)
Options:
    -o, --output  Save to a txt file
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""

import sys
import cmd
from docopt import docopt, DocoptExit
from app.amity import my_amity
from app.person import person
from app.rooms import my_room


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class MyInteractive (cmd.Cmd):
    intro = 'Welcome to Amity office space allocation!\n\n'\
        + 'Usage:\n'\
        + 'amity create_room <room_name>...\n'\
        + 'amity add_person <first_name> <last_name> (Fellow|Staff) [<wants_accomodation>]\n' \
        + 'amity reallocate_person <person_identifier> <new_room_name>\n'\
        + 'amity load_people <filename>\n'\
        + 'amity print_allocations [-o <filename>]\n'\
        + 'amity print_unallocated [-o <filename>]\n'\
        + 'amity print_room <room_name>\n'\
        + 'amity save_state [--db=sqlite_database]\n'\
        + 'amity load_state <sqlite_database>\n'\
        + ' (type help for a list of commands.)'

    prompt = '(amity) '
    file = None

    @docopt_cmd
    def do_create_room(self, args):
        """Usage: create_room <room_name>..."""
        # print args
        my_amity.create_room(args)

    @docopt_cmd
    def do_add_person(self, args):
        """Usage:
        add_person <first_name> <last_name> (Fellow|Staff) [<wants_accomodation>]"""
        person.add_person(args)

    @docopt_cmd
    def do_reallocate_person(self, args):
        """Usage:
        reallocate_person <person_identifier> <new_room_name>"""

        person.reallocate_person(args)

    @docopt_cmd
    def do_load_people(self, args):
        """Usage:
        load_people <filename>

                Sample Input Format:

                OLUWAFEMI SULE FELLOW Y
                DOMINIC WALTERS STAFF
                SIMON PATTERSON FELLOW Y
                MARI LAWRENCE FELLOW Y
                LEIGH RILEY STAFF
                TANA LOPEZ FELLOW Y
                KELLY McGUIRE STAFF N
        """
        person.load_people(args)

    @docopt_cmd
    def do_print_allocations(self, args):
        """Usage:
        print_allocations [-o <filename>]
        """
        my_room.print_allocations(args)

    @docopt_cmd
    def do_print_unallocated(self, args):
        """Usage:
        print_unallocated [-o <filename>]"""
        my_room.print_unallocated(args)

    @docopt_cmd
    def do_print_room(self, args):
        """Usage:
        print_room <room_name>

        """
        my_room.print_room(args)

    @docopt_cmd
    def do_save_state(self, args):
        """Usage:
        save_state [--db=sqlite_database]"""
        print args

    @docopt_cmd
    def do_load_state(self, args):
        """Usage: \
        load_state <sqlite_database>"""
        print args

    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('Good Bye!')
        exit()

opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    MyInteractive().cmdloop()

print(opt)
