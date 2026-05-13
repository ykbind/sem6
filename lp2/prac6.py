#in exam you have just replace the content of the codes 
#here hospital system is used to but you may use your own topic like travel guide or restaurant or education, etc
#just make sure to ask 5 questions and give suggestions based on the answers

def hospital_expert_system():
    print("Welcome to Hospital Expert System")
    print("Answer the following questions.")
    print("Type 'yes' or 'no'\n")

    fever = input("Do you have fever? ").lower()
    cough = input("Do you have cough? ").lower()
    chest_pain = input("Do you have chest pain? ").lower()
    injury = input("Do you have any injury or fracture? ").lower()
    stomach_pain = input("Do you have stomach pain? ").lower()

    print("\n--- Diagnosis Suggestion ---")

    if fever == "yes" and cough == "yes":
        print("You may have a viral infection or flu.")
        print("Suggested Department: General Medicine")

    elif chest_pain == "yes":
        print("You may need a heart check-up.")
        print("Suggested Department: Cardiology")

    elif injury == "yes":
        print("You may require bone or injury treatment.")
        print("Suggested Department: Orthopedics")

    elif stomach_pain == "yes":
        print("You may have digestive issues.")
        print("Suggested Department: Gastroenterology")

    else:
        print("Please consult a General Physician for further diagnosis.")

    print("\nThank you for using Hospital Expert System.")


hospital_expert_system()