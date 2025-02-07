import openpyxl

def get_locator_from_excel(page_name, element_name):
    # Load the Excel workbook
    workbook = openpyxl.load_workbook('resources/locators.xlsx')
    sheet = workbook.active  # Use the active sheet (assuming single sheet)

    # Find the locator based on page_name and element_name
    for row in sheet.iter_rows(min_row=2, values_only=True):  # Assuming the first row is the header
        if row[0] == page_name and row[1] == element_name:
            locator_type = row[2]  # Locator Type
            locator_value = row[3]  # Locator Value
            return locator_type, locator_value
    return None, None  # Return None if no match is found



