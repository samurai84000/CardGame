from CardHierarchy.Card import Card


class SpellCard(Card):
    def __init__(self, name, description, cost, image_path, effect):
        super().__init__(name, description, cost, image_path)
        self.effect = effect