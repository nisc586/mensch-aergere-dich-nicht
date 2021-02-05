class Field():
    def __init__(self, val, access=""):
        self.value = val
        self.access = access
        self.identifier = f"{val}{access}"
        self.is_end_field = (val > 0) and (access != "")
        return


    def __str__(self):
        return self.identifier

    def __eq__(self, other):
        return self.__str__() == str(other)

    def __hash__(self):
        return hash(self.identifier)
