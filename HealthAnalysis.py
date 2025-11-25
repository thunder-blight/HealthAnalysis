from Classes import Ailment, Fever, UserSymptoms

def main():
    raw_input_symptoms = input("Enter your symptoms (you can use commas, spaces, or both): ")
    user_symptoms = UserSymptoms(raw_input_symptoms)

    if "fever" in user_symptoms.symptoms:
        temp_input = input("What is your temperatiure in Celsius? ")
        try:
            temperature = float(temp_input)
        except ValueError:
            print("Invalid temperature input. Using default temperature of 37.5°C.")
            return 37.5
        fever_case = Fever("Fever", user_symptoms.symptoms, temperature)
        print(f"Fever detected? {fever_case.is_fever()}")
        print(f"Fever level: {fever_case.fever_severity()}")
    else:
        ailment = Ailment("General Ailment", user_symptoms.symptoms)
        print(f"Symptoms recorded: {ailment.symptoms}")

if __name__ == "__main__":
    main()