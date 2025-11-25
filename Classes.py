class Symptom:
    def __init__(self, name: str, value=None):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"Symptom(name={self.name}, value={self.value})" if self.value is not None else f"Symptom(name={self.name})"

class Ailment:
    def __init__(self, name: str, symptoms: list[str], cures: list[str] = None):
        self.name = name
        self.symptoms = symptoms
        self.cure = cures if cures else ["Unknown"]

class UserSymptoms:
    def __init__(self, raw_input: str):
        self.symptoms = self._clean(raw_input)

    def _clean(self, raw_input: str) -> list[str]:
        # Handle commas and spaces
        standardized_input = raw_input.replace(",", " ")
        split_symptoms = [
            s.strip().lower() for s in standardized_input.split() if s.strip()
        ]
        return list(set(split_symptoms))
