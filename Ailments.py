from Classes import Ailment, Symptom

def make_symptoms(symptom_list):
    symptoms = []
    for item in symptom_list:
        if isinstance(item, tuple):
            symptoms.append(Symptom(item[0], item[1]))
        else:
            symptoms.append(Symptom(item))
    return symptoms

# Flu
flu = Ailment(
    "Flu", 
    make_symptoms([("fever", 38.0), "cough", "sore throat", "runny nose", "body pain"]),
    ["rest", "hydration", "paracetamol"]
    )

# Common cold
cold = Ailment(
    "Common Cold", 
    make_symptoms(["sneezing", "cough", "sore throat"]), 
    ["rest", "hydration"]
    )

# Malaria
malaria = Ailment(
    "Malaria", 
    make_symptoms([("fever", 39.0), "chills", "fatigue", "sweating"]),
    cures=["antimalarials"]
    )

# Migraine
migraine = Ailment(
    "Migraine", 
    make_symptoms(["headache", "nausea", "light sensitivity"]), 
    cures=["pain relievers", "rest"]
    )

# Allergy (Pollen Allergy)
allergy = Ailment(
    "Pollen Allergy",
    make_symptoms(["sneezing", "runny nose", "itchy eyes", "nasal congestion"]),
    ["antihistamines", "avoid pollen"]
)

# Stomach Flu / Gastroenteritis
stomach_flu = Ailment(
    "Stomach Flu",
    make_symptoms([("fever", 37.8), "nausea", "vomiting", "diarrhea", "abdominal pain"]),
    ["hydration", "rest", "light diet"]
)

# Dengue
dengue = Ailment(
    "Dengue",
    make_symptoms([("fever", 39.5), "headache", "muscle pain", "joint pain", "rash"]),
    ["hydration", "paracetamol", "rest"]
)

# Food Poisoning
food_poisoning = Ailment(
    "Food Poisoning",
    make_symptoms(["nausea", "vomiting", "diarrhea", "abdominal pain"]),
    ["hydration", "rest", "light diet"]
)

# COVID-19
covid = Ailment(
    "COVID-19",
    make_symptoms([("fever", 37.5), "cough", "fatigue", "loss of taste", "loss of smell", "sore throat"]),
    ["rest", "hydration", "medical attention if severe"]
)

# All ailments list
ALL_AILMENTS = [flu, cold, malaria, migraine, allergy, stomach_flu, dengue, food_poisoning, covid]