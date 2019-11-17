# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def increase_quality(self, item):
        item.quality += 1 if item.quality < 50 else 0

    def update_quality(self):
        for item in self.items:

            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1

            if item.name == "Backstage passes to a TAFKAL80ETC concert":
                self.increase_quality(item)
                if item.sell_in < 10:
                    self.increase_quality(item)
                    if item.sell_in < 5:
                        self.increase_quality(item)

            if item.name == "Aged Brie":
                self.increase_quality(item)
                if item.sell_in < 0:
                    self.increase_quality(item)

            if item.name != "Backstage passes to a TAFKAL80ETC concert" and item.name != "Aged Brie" and item.name != "Sulfuras, Hand of Ragnaros" and item.quality > 0:
                item.quality -= 1

            if item.sell_in < 0:
                if item.name == "Backstage passes to a TAFKAL80ETC concert":
                    item.quality = item.quality - item.quality
                else:
                    if item.quality > 0 and item.name != "Aged Brie" and item.name != "Sulfuras, Hand of Ragnaros":
                        item.quality -= 1


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