
# Division III Classes
class Affirmation:
    def __init__(self, id_num: int, affirmation: str, tags:str):

        self.id_num = id_num
        self.affirmation = affirmation
        self.tags = tags

    def display_affirmation(self) -> str:

        return f"{self.affirmation}"


class Prayer:
    def __init__(self, id_num: int, prayer: str, status: str

        self.id_num = id_num
        self.affirmation = affirmation
        self.tags = tags

    def display_affirmation(self) -> str:

        return f"{self.affirmation}"


class Quotation:
    def __init__(self, id_num: int, quotation: str, attributor: str, tags: str):
        
        self.id_num = id_num
        self.quotation = quotation
        self.attributor = attributor
        self.tags = tags

    def display_quotation(self) -> str:
        """Return the formatted quotation."""
        return f'"{self.quotation}" - {self.attributor}'


class Wisdom_Nugget:
    def __init__(self, id_num: int, wisdom_nugget: str, tags:str):

        self.id_num = id_num
        self.wisdom_nugget = wisdom_nugget
        self.tags = tags

    def display_wisdom_nugget(self) -> str:

        return f"{self.wisdom_nugget}"