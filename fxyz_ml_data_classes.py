class BaseEntry:
    """
    A base class for entries with common attributes and methods.
    """
    def __init__(self, id_num: int, content: str, tags: str = None):
        self.id_num = id_num
        self.content = content
        self.tags = tags

    def display_content(self) -> str:
        """Display the main content."""
        return f"{self.content}"


# Specific entry types inheriting from BaseEntry
class MentalAffirmation(BaseEntry):
    pass


class MentalAnalogy(BaseEntry):
    pass


class MentalAspiration(BaseEntry):
    pass


class MentalBehavior(BaseEntry):
    def __init__(self, id_num: int, behavior: str, behavior_type: str, tags: str, status: str):
        super().__init__(id_num, behavior, tags)
        self.behavior_type = behavior_type
        self.status = status


class MentalCharacteristic(BaseEntry):
    def __init__(self, id_num: int, characteristic: str):
        super().__init__(id_num, characteristic)


class MentalDichotomy(BaseEntry):
    pass


class MentalGratitude(BaseEntry):
    pass


class MentalHabit(BaseEntry):
    def __init__(self, id_num: int, habit: str, status: str):
        super().__init__(id_num, habit)
        self.status = status


class MentalHumanEngineering(BaseEntry):
    def __init__(self, id_num: int, name: str, formula: str, status: str):
        super().__init__(id_num, formula)
        self.name = name
        self.status = status

    def display_human_eng_formulae(self):

        return f'{name}: {formula}'


class MentaImpedance(BaseEntry):
    def __init__(self, id_num: int, impedance: str, type:str, status: str, note: str)
        super().__init__(id_num, impedance)
        self.type = type
        self.status = status
        self.note = note


class MentalPrayer(BaseEntry):
    def __init__(self, id_num: int, prayer: str, status: str):
        super().__init__(id_num, prayer)
        self.status = status


class MentalProverb(BaseEntry):
    def __init__(self, id_num: int, proverb: str, origination: str):
        super().__init__(id_num, proverb)
        self.origination = origination

    def display_proverb(self) -> str:
        return f'"{self.content}" - {self.origination}'


class MentalQuotation(BaseEntry):
    def __init__(self, id_num: int, quotation: str, attributor: str, tags: str):
        super().__init__(id_num, quotation, tags)
        self.attributor = attributor

    def display_quotation(self) -> str:
        return f'"{self.content}" - {self.attributor}'


class MentalReflection(BaseEntry):
    pass


class MentalReligious(BaseEntry):
    def __init__(self, id_num: int, passage: str, source: str):
        super().__init__(id_num, passage)
        self.source = source

    def display_passage(self) -> str:
        return f'"{self.content}" - {self.source}'


class MentalStory(BaseEntry):
    def __init__(self, id_num: int, story: str, origination: str):
        super().__init__(id_num, story)
        self.origination = origination


class MentalWisdomNugget(BaseEntry):
    pass