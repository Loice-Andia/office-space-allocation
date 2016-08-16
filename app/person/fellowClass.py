from personClass import Person


class Fellow(Person):
    """
    Fellow
    """

    def __init__(self, person_role, office_allocated, living_space_allocated):
        self.person_role = person_role
        self.office_allocated = office_allocated
        self.living_space_allocated = living_space_allocated
