from math_library.fund_comp import *
from fundamentals_library.constants import *

# This serves as a template of which all divisions inherit these class properties
class UniversalProperties:

    def __init__(self, id_num: int, data: str, tags: str, updated: str):

        self.id_num = id_num
        self.data = data
        self.tags = tags
        self.updated = updated

    def display_universal_data(self):

        return f'Entry {self.id_num} contains "{self.data}", last modified on {self.updated}.'

    def display_universal_tags(self):

        return f'Entry {self.data} contains the tags {self.tags}.'

#-----------------------DIVISION--CLASSES--------------------------------#

# Division 1: Organization Class Template
class OrganizationalData(UniversalProperties):
    
    def __init__(self, id_num, data, tags, updated):
        
        super().__init__(id_num, data, tags, updated)


# Division 2: Physical
class PhysicalData(UniversalProperties):
    
    def __init__(self, id_num, data, tags, updated):
        
        super().__init__(id_num, data, tags, updated)


# Division 3: Mental Class Template
class MentalData(UniversalProperties):
    
    def __init__(self, id_num: int, data: str, notes: str = None, tags: str = None, updated: str = None):
        super().__init__(id_num, data, updated)


    def display_content(self) -> str:
        """Display the main content."""
        return f"{self.content}"

# Division 4: Spiritual Class Template
# This class may not get touched for a long time.
class SpiritualData(UniversalProperties):
    
    def __init__(self, id_num, data, tags, updated):
        
        super().__init__(id_num, data, tags, updated)

# Division 5: Chronological Class Template
class ChronologicalData(UniversalProperties):
    
    def __init__(self, id_num, data, tags, updated):
        
        super().__init__(id_num, data, tags, updated)

# Division 6: Financial Class Template
class FinancialData(UniversalProperties):
    
    def __init__(self, id_num, data, tags, updated):
        
        super().__init__(id_num, data, tags, updated)

# Division 7: Materials Class Template:
class MaterialData(UniversalProperties):

    def __init__(self, id_num, data, tags, updated, appraised_value: float, status: float):
        super().__init__(id_num, data, tags, updated)

        self.appraised_value = appraised_value
        self.status = status

# Division 8: Knowledge Class Template
class KnowledgeData(UniversalProperties):

    def __init__(self, id_num, data, tags, updated):
        
        super().__init__(id_num, data, tags, updated)


# Division 9: Skills Class Template

class SkillsData(UniversalProperties):

    def __init__(self, id_num, data, tags, updated):
        
        super().__init__(id_num, data, tags, updated)


# Division 10: Creative Class Template
class CreativeData(UniversalProperties):
  
    def __init__(self, id_num, data, tags, updated, 
                 abbr: str, summary: str, series: str, version: int, status: str, save_point: str, 
                 next_steps: str, created: str):

        super().__init__(id_num, data, tags, updated)

        self.abbr = abbr
        self.summary = summary
        self.series = series
        self.version = version
        self.status = status
        self.save_point = save_point
        self.next_steps = next_steps
        self.created = created
    
    def get_status(self):

        return f'{self.abbr}{self.id_num}: {self.title} is marked as {self.status} on {self.modified}.'


# Division 11: Social Class Template
class SocialData(UniversalProperties):
    
    def __init__(self, id_num, data, tags, updated):
        
        super().__init__(id_num, data, tags, updated)

# Division 12: Business Class Template
class BusinessData(UniversalProperties):
    
    def __init__(self, id_num, data, tags, updated):
        
        super().__init__(id_num, data, tags, updated)

#----------------------------UNIT-DIVISION--INHERITANCE----------------------------------#

# DIVISION 3 UNIT CLASSES
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
    pass


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

# Division 11 Unit Classes

class SocialIndividuals(SocialData):

    def __init__(self, id_num, data, tags, updated, 
        first_name: str, middle_init: str, last_name: str, birth_month: int, birth_day_of_month: int, 
        birth_year: int, gender: str, location: str, status: str):
        
        super().__init__(id_num, data, tags, updated)

        self.first_name = first_name
        self.middle_init = middle_init
        self.last_name = last_name
        self.full_name = f'{first_name} {middle_init}. {last_name}'
        self.birth_month = birth_month
        self.birth_day_of_month = birth_day_of_month
        self.birth_year = birth_year
        self.birthday: str = f'{birth_month} / {birth_day_of_month} / {birth_year}'