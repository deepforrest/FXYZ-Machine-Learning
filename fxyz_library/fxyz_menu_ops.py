from fxyz_menu_staples import *

def fxyz_select_division(division_number: int) -> None:

    match division_number:
        
        case 1: fxyz_organization_menu()
        case 2: fxyz_physical_menu()
        case 3: fxyz_mental_menu()
        case 4: fxyz_spiritual_menu()
        case 5: fxyz_chronological_menu()
        case 6: fxyz_financial_menu()
        case 7: fxyz_material_menu()
        case 8: fxyz_knowledge_menu()
        case 9: fxyz_skillsets_menu()
        case 10: fxyz_creative_menu()
        case 11: fxyz_social_menu()
        case 12: fxyz_business_menu()
        case _: print(f'Division {division_number} is not a valid entry.  Please try again.')

    return None

def fxyz_select_organization_branch(branch_number: int) -> None:

    match branch_number:

        case 1: fxyz_architecture_branch()
        case 2: fxyz_development_branch()
        case 3: fxyz_personal_success_branch()
        case 4: fxyz_document_management_branch()
        case _: print(f'Branch {branch_number} does not exist.')

    return None