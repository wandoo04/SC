import numpy as np

class ART1:
    def __init__(self, input_size, categories, vigilance=0.8):
        self.input_size = input_size
        self.categories = categories
        self.vigilance = vigilance
        self.weights = np.ones((categories, input_size))  # Initialize weights with ones

    def complement_coding(self, input_pattern):
        return np.concatenate((input_pattern, 1 - input_pattern))  # Adds complement coding

    def match_category(self, input_pattern):
        input_coded = self.complement_coding(input_pattern)
        for j in range(self.categories):
            match = np.sum(np.minimum(input_coded, self.weights[j])) / np.sum(input_coded)
            if match >= self.vigilance:
                return j  # Category matched
        return -1  # No match found (new category needed)

    def train(self, input_pattern):
        input_coded = self.complement_coding(input_pattern)
        category = self.match_category(input_pattern)

        if category == -1:  # No matching category found
            category = len([w for w in self.weights if np.any(w != 1)])  # Find next available category
            if category >= self.categories:
                print("No available category, increase category size!")
                return
            self.weights[category] = input_coded  # Assign new pattern

        else:  # Update weight for the matched category
            self.weights[category] = np.minimum(self.weights[category], input_coded)
        
        print(f"Pattern {input_pattern} stored in category {category}")

    def classify(self, input_pattern):
        category = self.match_category(input_pattern)
        return category if category != -1 else "Unknown Pattern"

# Example Usage
art = ART1(input_size=4, categories=3, vigilance=0.8)

# Training with binary inputs
patterns = [
    np.array([1, 0, 0, 1]),
    np.array([1, 1, 0, 0]),
    np.array([0, 0, 1, 1]),
]

for pattern in patterns:
    art.train(pattern)

# Classify a new pattern
test_pattern = np.array([1, 0, 0, 1])
print("Classified as Category:", art.classify(test_pattern))
