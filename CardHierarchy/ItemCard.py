import pygame

from CardHierarchy.Card import Card


class ItemCard(Card):
    def __init__(self, name, description, cost, image_path, effect, healthEffect, attackEffect):
        super().__init__(name, description, cost, image_path)
        self.effect = effect
        self.healthEffect = healthEffect
        self.attackEffect = attackEffect;
        self.attached_to = None

    def attach_to_unit(self, unit_card):
        self.attached_to = unit_card

    def detach_from_unit(self):
        if self.attached_to:
            self.attached_to.remove_item(self)
            self.attached_to = None
