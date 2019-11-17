# -*- coding: utf-8 -*-

def increase_quality(item, value):
    for _ in range(value):
        if item.quality < 50:
            item.quality += 1

def decrease_quality(item, value):
    if item.sell_in < 0:
        value *= 2
    for _ in range(value):
        if item.quality > 0:
            item.quality -= 1

def backstage_update(item):
    if item.sell_in < 0:
        item.quality = 0
    elif item.sell_in < 5:
        increase_quality(item,3)
    elif item.sell_in < 10:
        increase_quality(item,2)
    else:
        increase_quality(item,1)

def aged_update(item):
    if item.sell_in < 0:
        increase_quality(item,2)
    else:
        increase_quality(item,1)

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue
            item.sell_in -= 1
            if item.name == "Backstage passes to a TAFKAL80ETC concert":
                backstage_update(item)
            elif item.name == "Aged Brie":
                aged_update(item)
            elif item.name == "Conjured Mana Cake":
                decrease_quality(item, 2)
            else:
                decrease_quality(item, 1)

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


# name, sellIn, quality
# +5 Dexterity Vest, 4, 14
# Aged Brie, -4, 10
# Elixir of the Mongoose, -1, 0
# Sulfuras, Hand of Ragnaros, 0, 80
# Sulfuras, Hand of Ragnaros, -1, 80
# Backstage passes to a TAFKAL80ETC concert, 9, 27
# Backstage passes to a TAFKAL80ETC concert, 4, 50
# Backstage passes to a TAFKAL80ETC concert, -1, 0
# Conjured Mana Cake, -3, 0