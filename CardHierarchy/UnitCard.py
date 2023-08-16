import pygame

from CardHierarchy.Card import Card


class UnitCard(Card):
    def __init__(self, name, description, cost, image_path, attack, health):
        super().__init__(name, description, cost, image_path)
        self.attack = attack
        self.health = health
        self.items = []

    def attach_item(self, item_card):
        self.items.append(item_card)
        item_card.attach_to_unit(self)

    def remove_item(self, item_card):
        self.items.remove(item_card)
        item_card.detach_from_unit()

    def check_attack(self, items):
        if len(items) == 0:
            self.attack = self.attack
        else:
            for i in items:
                self.attack = self.attack + i.attackEffect

    def check_health(self, items):
        if len(items) == 0:
            self.health = self.health
        else:
            for i in items:
                self.health = self.health + i.healthEffect
