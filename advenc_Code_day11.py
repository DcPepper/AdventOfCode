from types import MethodType

#Goal: https://adventofcode.com/2022/day/11 UNFINISHED

data ="""
Monkey 0:
  Starting items: 64
  Operation: new = old * 7
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 1:
  Starting items: 60, 84, 84, 65
  Operation: new = old + 7
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 7

Monkey 2:
  Starting items: 52, 67, 74, 88, 51, 61
  Operation: new = old * 3
  Test: divisible by 5
    If true: throw to monkey 5
    If false: throw to monkey 7

Monkey 3:
  Starting items: 67, 72
  Operation: new = old + 3
  Test: divisible by 2
    If true: throw to monkey 1
    If false: throw to monkey 2

Monkey 4:
  Starting items: 80, 79, 58, 77, 68, 74, 98, 64
  Operation: new = old * old
  Test: divisible by 17
    If true: throw to monkey 6
    If false: throw to monkey 0

Monkey 5:
  Starting items: 62, 53, 61, 89, 86
  Operation: new = old + 8
  Test: divisible by 11
    If true: throw to monkey 4
    If false: throw to monkey 6

Monkey 6:
  Starting items: 86, 89, 82
  Operation: new = old + 2
  Test: divisible by 7
    If true: throw to monkey 3
    If false: throw to monkey 0

Monkey 7:
  Starting items: 92, 81, 70, 96, 69, 84, 83
  Operation: new = old + 4
  Test: divisible by 3
    If true: throw to monkey 4
    If false: throw to monkey 5"""

class Monkey:

  items = []
  count = 0

  def __init__(self, id, starting_items, true_dest, false_dest):
    self.items = starting_items
    self.id = id
    self.dest_true = true_dest
    self.dest_false = false_dest 

  def inspect(self, items):
    global monkey_list
    self.items = []
    
    self.count+=len(items)
    if self.id == 0:
      items = [item* 7 for item in items]
      good_item = filter(lambda item: item%13 == 0, items)
      bad = filter(lambda item: item%13 != 0, items)
      true_dest = filter(lambda monkey_:monkey_.id == self.dest_true, monkey_list)
      false_dest = filter(lambda monkey_:monkey_.id == self.dest_false, monkey_list)
    elif self.id == 1:
      items = [item+ 7 for item in items]
      good_item = filter(lambda item: item%19 == 0, items)
      bad = filter(lambda item: item%19 != 0, items)
      true_dest = filter(lambda monkey_:monkey_.id == self.dest_true, monkey_list)
      false_dest = filter(lambda monkey_:monkey_.id == self.dest_false, monkey_list)
    elif self.id == 2:
      items = [item*3 for item in items]
      good_item = filter(lambda item: item%5 == 0, items)
      bad = filter(lambda item: item%5 != 0, items)
      true_dest = filter(lambda monkey_:monkey_.id == self.dest_true, monkey_list)
      false_dest = filter(lambda monkey_:monkey_.id == self.dest_false, monkey_list)
    elif self.id == 3:
      items = [item+ 3 for item in items]
      good_item = filter(lambda item: item%2 == 0, items)
      bad = filter(lambda item: item%2 != 0, items)
      true_dest = filter(lambda monkey_:monkey_.id == self.dest_true, monkey_list)
      false_dest = filter(lambda monkey_:monkey_.id == self.dest_false, monkey_list)
    elif self.id == 4:
      items = [item*item for item in items]
      good_item = filter(lambda item: item%17 == 0, items)
      bad = filter(lambda item: item%17 != 0, items)
      true_dest = filter(lambda monkey_:monkey_.id == self.dest_true, monkey_list)
      false_dest = filter(lambda monkey_:monkey_.id == self.dest_false, monkey_list)
    elif self.id == 5:
      items = [item+ 8 for item in items]
      good_item = filter(lambda item: item%11 == 0, items)
      bad = filter(lambda item: item%11 != 0, items)
      true_dest = filter(lambda monkey_:monkey_.id == self.dest_true, monkey_list)
      false_dest = filter(lambda monkey_:monkey_.id == self.dest_false, monkey_list)
    elif self.id == 6:
      items = [item+ 2 for item in items]
      good_item = filter(lambda item: item%7 == 0, items)
      bad = filter(lambda item: item%7 != 0, items)
      true_dest = filter(lambda monkey_:monkey_.id == self.dest_true, monkey_list)
      false_dest = filter(lambda monkey_:monkey_.id == self.dest_false, monkey_list)
    elif self.id == 7:
      items = [item+ 4 for item in items]
      good_item = filter(lambda item: item%3 == 0, items)
      bad = filter(lambda item: item%3 != 0, items)
      true_dest = filter(lambda monkey_:monkey_.id == self.dest_true, monkey_list)
      false_dest = filter(lambda monkey_:monkey_.id == self.dest_false, monkey_list)

    [e for e in true_dest][0].items += good_item
    [e for e in false_dest][0].items += bad

monkey0 = Monkey(0, [64], 1, 3)
monkey1 = Monkey(1, [60, 84, 84, 65], 2, 7)
monkey2 = Monkey(2, [52, 67, 74, 88, 51, 61], 5, 7)
monkey3 = Monkey(3, [67, 72], 1, 2)
monkey4 = Monkey(4, [80, 79, 58, 77, 68, 74, 98, 64], 6, 0)
monkey5 = Monkey(5, [62, 53, 61, 89, 86], 4, 6)
monkey6 = Monkey(6, [86, 89, 82], 3, 0)
monkey7 = Monkey(7, [92, 81, 70, 96, 69, 84, 83], 4, 5)

monkey_list = [monkey0, monkey1, monkey2, monkey3, monkey4, monkey5, monkey6, monkey7]

for _ in range(1000):
    print(_)
    
    for monkey in monkey_list:
        monkey_items = monkey.items.copy()

        monkey.inspect(monkey_items)
        

counts = sorted([e.count for e in monkey_list], reverse=True)
print(counts)
print(counts[0]*counts[1])
            





    