# Define a nested dictionary for the menus
menus = {
  "main": {
    "prompt": "Welcome to the Debug Helper. Please choose the module:",
    "options": {
      "1": "KAD/ADC/109/C/S1/03",
      "2": "KAD/ADC/114/1V/02",
      "3": "KAD/ADC/116/1V/01",
      "4": "KAD/ADC/136/C/02",
      "5": "KAD/ADC/135/B/02",
      "6": "KAD/ADC/134/B/100M/06",
    }
  },
  "documents": {
    "prompt": "Please select an option to open a specific document, or return to the main menu:",
    "options": {
      "1": "Open Datasheets",
      "2": "Open PTI",
      "3": "Open PTR",
      "4": "Open assembly instructions",
      "5": "Open Schematic for KDD",
      "6": "Open Schematic for KDM",
      "0": "Return to Main Menu",  # Added return option
    }
  }
}

def show_menu(menu_key):
  menu = menus[menu_key]
  print("\n" + menu["prompt"])
  for key, value in menu["options"].items():
    print(f"{key}) {value}")
  choice = input("Enter your choice: ")
  return choice

def open_document(doc_choice):
  actions = {
    "1": "Datasheets opened.",
    "2": "PTI document opened.",
    "3": "PTR document opened.",
    "4": "Assembly instructions opened.",
    "5": "Schematic for KDD opened.",
    "6": "Schematic for KDM opened.",
  }
  # Handle return to main menu
  if doc_choice == "0":
    return True
  else:
    print(actions.get(doc_choice, "Invalid choice."))
    return False

def main():
  while True:
    # Show main menu
    module_choice = show_menu("main")
    if module_choice in menus["main"]["options"]:
      print(f"You have chosen {menus['main']['options'][module_choice]}")
      while True:
        # Show documents menu
        doc_choice = show_menu("documents")
        if open_document(doc_choice):
          break
    else:
      print("Invalid choice, please try again later on")

if __name__ == "__main__":
  main()
