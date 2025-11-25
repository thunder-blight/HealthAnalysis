from Classes import UserSymptoms, Symptom
from Ailments import ALL_AILMENTS

def main():
    raw_input_symptoms = input("Enter your symptoms (separated by commas/spaces): ")
    user_symptoms = UserSymptoms(raw_input_symptoms)

    if "fever" in user_symptoms.symptoms:
        temp_input = input("You mentioned fever. Please enter your temperature in Celsius: ")
        try:
            user_temp  = float(temp_input)
        except ValueError:
            user_temp = 37.5

        for ailment in ALL_AILMENTS:
            for symptom in ailment.symptoms:
                if symptom.name == "fever":
                    symptom.value = user_temp

    results = []
    for ailment in ALL_AILMENTS:
        matches = []
        for s in ailment.symptoms:
            if s.name in user_symptoms.symptoms:
                if s.name == "fever" and s.value is not None and s.value <= 37.5:
                    continue
                matches.append(s)
        probability = (len(matches) / len(ailment.symptoms)) * 100
        results.append((ailment, probability, matches))

    results.sort(key=lambda x: x[1], reverse=True)
    top_results = results[:3]

    print("\nTop 3 possible ailments based on your symptoms:")
    for ailment, prob, matches in top_results:
        print(f"{ailment.name}: {prob:.2f}% match (matching symptoms: {[s.name for s in matches]})")

        for s in matches:
            if s.name == "fever" and s.value is not None:
                if s.value > 37.5:
                    severity = "Mild fever" if s.value <= 39 else "High fever"
                    print(f"  Fever detected! Severity: {severity}")
                else:
                    print(f"  No fever detected.")

        print(f"  Recommended cures: {', '.join(ailment.cure)}\n")


if __name__ == "__main__":
    main()
