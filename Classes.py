class Ailment:
    def __init__(self, name: str, symptoms: list[str], cures: list[str]):
        self.name = name
        self.sypmtoms = symptoms
        self.cure = cures

class Fever(Ailment):
    def __init__(self, name: str, symptoms: list[str], cures: list[str], temperature: float):
        super().__init__(name, symptoms, cures)
        self.temperature = temperature

        def is_fever(self) -> bool:
            return self.temperature > 37.5
        
        def fever_severity(self) -> str:
            if self.temperature < 37.5:
                return  "No fever"
            elif self.temperature <= 39.0:
                return "Mild fever"
            else:
                return "High fever"

class UserSymptoms:
    def __init__(self, raw_input: str):
        self.symptoms = self._clean(raw_input)

    def _clean(self, raw_input: str) -> list[str]:
        standardised_input = raw_input.replace(",", " ")
        split_symptoms = [
            s.strip().lower() for s in standardised_input.split() if s.strip()
        ]

        return list(set(split_symptoms))