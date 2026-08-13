import json
import os

purpose = None

domain = None

preference = None

def set_profile():
    global purpose, domain, preference

    purpose = input("What do you want to use Omnix for (Purpose)? ").strip()
    domain = input("Which domains or topics should Omnix prepare for (Topics)? ").split(",")
    domain = [item.strip() for item in domain]
    preference = input("How should Omnix respond to you (Response)? ").strip()
    return purpose, domain, preference

def get_profile():
   return purpose, domain, preference
   
def update_profile():
    global purpose, domain, preference

    choice = input("choose any one for updating profile:\n 1. purpose\n 2. domain\n 3. preference\n 4. everything\n")

    if choice == "1":
       purpose = input("What is your new purpose? ").strip()
       save_profile()
       return purpose
    
    elif choice == "2":
       domain = input("What is your new domain? ").split(",")
       domain = [item.strip() for item in domain]
       save_profile()
       return domain
    
    elif choice == "3":
      preference = input("What is your new preference ").strip()
      save_profile()
      return preference
    
    elif choice == "4":
      purpose = input("What is your new purpose? ").strip()
      domain = input("What is your new domain? ").split(",")
      domain = [item.strip() for item in domain]
      preference = input("What is your new preference ").strip()
      save_profile()
      return purpose, domain, preference
    
    else:
       raise ValueError(f"Invalid choice 'update_profile()'. choose '1', '2', '3', or '4'")

def save_profile():
    with open("profile.json", "w") as file:

     profile_data = {
        "purpose": purpose ,
        "domain": domain ,
        "preference": preference
     }
     json.dump(profile_data, file)

def load_profile():
   with open("profile.json", "r") as file:
      profile = json.load(file)

   global purpose, domain, preference

   purpose = profile["purpose"]
   domain = profile["domain"]
   preference = profile["preference"]

   return purpose, domain, preference

def profile_exists():
   return os.path.exists("profile.json")

