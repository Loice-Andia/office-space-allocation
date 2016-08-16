from personClass import Person


class Staff(Person):
    """
        Staff
    """

    def __init__(self, person_role, office_allocated):
        self.person_role = person_role
        self.office_allocated = office_allocated
