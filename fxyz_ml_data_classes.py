class MentalData:
    """
    A base class for entries with common attributes and methods.
    """
    def __init__(self, id_num: int, content: str, notes: str = None, tags: str = None, modified: str = None):
        self.id_num = id_num
        self.content = content
        self.tags = tags

    def display_content(self) -> str:
        """Display the main content."""
        return f"{self.content}"

class CreativeData:
    def __init__(self, id_num:int, abbr: str, int, title: str, summary: str, series: str, word_count: str, tags: str, status: str, save_point: str, next_steps: str, created: str, modified: str):

        self.id_num = id_num
        self.abbr = abbr
        self.title = title
        self.summary = summary
        self.series = series
        self.tags = tags
        self.status = status
        self.save_point = save_point
        self.next_steps = next_steps
        self.created = created
        self.modified = modified
    
    def get_status(self):
        return f'{self.abbr}{self.id_num}: {self.title} is marked as {self.status} on {self.modified}.'

# Specific entry types inheriting from MentalData
class MentalAffirmation(MentalData):
    pass


class MentalAnalogy(MentalData):
    pass


class MentalAspiration(MentalData):
    pass


class MentalBehavior(MentalData):
    def __init__(self, id_num: int, behavior: str, behavior_type: str, tags: str, status: str):
        super().__init__(id_num, behavior, tags)
        self.behavior_type = behavior_type
        self.status = status


class MentalCharacteristic(MentalData):
    def __init__(self, id_num: int, characteristic: str):
        super().__init__(id_num, characteristic)


class MentalDichotomy(MentalData):
    pass


class MentalGratitude(MentalData):
    pass


class MentalHabit(MentalData):
    def __init__(self, id_num: int, habit: str, status: str):
        super().__init__(id_num, habit)
        self.status = status


class MentalHumanEngineering(MentalData):
    def __init__(self, id_num: int, name: str, formula: str, status: str):
        super().__init__(id_num, formula)
        self.name = name
        self.status = status

    def display_human_eng_formulae(self):

        return f'{self.name}: {self.formula}'


class MentalImpedance(MentalData):
    def __init__(self, id_num: int, impedance: str, type:str, status: str, note: str):
        super().__init__(id_num, impedance)
        self.type = type
        self.status = status
        self.note = note


class MentalPrayer(MentalData):
    def __init__(self, id_num: int, prayer: str, status: str):
        super().__init__(id_num, prayer)
        self.status = status


class MentalProverb(MentalData):
    def __init__(self, id_num: int, proverb: str, origination: str):
        super().__init__(id_num, proverb)
        self.origination = origination

    def display_proverb(self) -> str:
        return f'"{self.content}" - {self.origination}'


class MentalQuotation(MentalData):
    def __init__(self, id_num: int, quotation: str, attributor: str, tags: str):
        super().__init__(id_num, quotation, tags)
        self.attributor = attributor

    def display_quotation(self) -> str:
        return f'"{self.content}" - {self.attributor}'


class MentalReflection(MentalData):
    pass


class MentalReligious(MentalData):
    def __init__(self, id_num: int, passage: str, source: str):
        super().__init__(id_num, passage)
        self.source = source

    def display_passage(self) -> str:
        return f'"{self.content}" - {self.source}'


class MentalStory(MentalData):
    def __init__(self, id_num: int, story: str, origination: str):
        super().__init__(id_num, story)
        self.origination = origination


class MentalWisdomNugget(MentalData):
    pass