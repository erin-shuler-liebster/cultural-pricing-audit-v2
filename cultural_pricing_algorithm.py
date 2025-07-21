# cultural_pricing_algorithm.py
class CulturalPricingTranslator:
    def __init__(self, profiles):
        self.profiles = profiles

    def assess_alignment(self, tags, country):
        feedback = {}
        ref = self.profiles[country]
        for dim, val in ref.items():
            if tags.get(dim) and val > 0.5:
                feedback[dim] = "✅ Matches cultural expectations"
            elif tags.get(dim):
                feedback[dim] = "⚠️ Might mismatch cultural tone"
            else:
                feedback[dim] = "❌ No alignment detected"
        return feedback

    def recommend_improvements(self, tags, country):
        improvements = {}
        ref = self.profiles[country]
        for dim, val in ref.items():
            if not tags.get(dim):
                if val > 0.5:
                    improvements[dim] = f"Add strong signals for {dim}"
                else:
                    improvements[dim] = f"Use simple, neutral messaging for {dim}"
        return improvements
