# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def augmenter_qualite(self, item):
        if item.quality < 50:
            item.quality += 1

    def diminuer_qualite(self, item):
        if item.quality > 0:
            item.quality -= 1

    def update_quality(self):
        for item in self.items:

            if item.name == "Sulfuras, Hand of Ragnaros":
                continue

            if item.name == "Aged Brie":
                self.augmenter_qualite(item)

            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                self.augmenter_qualite(item)

                if item.sell_in < 11:
                    self.augmenter_qualite(item)

                if item.sell_in < 6:
                    self.augmenter_qualite(item)

            else:
                self.diminuer_qualite(item)

            item.sell_in -= 1



class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
