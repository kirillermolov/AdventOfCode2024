
#PART 1
import itertools
import operator

class Node():
    def __init__(self, value, result_value):
        self.value = value
        self.result_value = result_value

    def add_mul(self,level):
        value = self.value * array_numbers[level]
        if value <= self.result_value:
            return Node(value, self.result_value)
        else:
            return None

    def add_sum(self,level):
        value = self.value + array_numbers[level]
        if value <= self.result_value:
            return Node(value, self.result_value)
        else:
            return None

    def get_result_value(self):
        return self.result_value

    def get_value(self):
        return self.value

def prune_exact(array_numbers, result_value):
    mult_all = list(itertools.accumulate(array_numbers, operator.mul))[-1]
    if mult_all == result_value or sum(array_numbers) == result_value:
        return True
    else:
        return False

def go_through_nodes(array_numbers,node_list):
    for level in range(1,len(array_numbers)):
        node_list_new = []
        for node in node_list:
            if node.add_mul(level):
                node_list_new.append(node.add_mul(level))
            if node.add_sum(level):
                node_list_new.append(node.add_sum(level))
        if node_list_new:
            node_list = node_list_new[:]
        else:
            return None
    return node_list


with open('input.txt') as file:
    counter = 0
    for line in file:
        split1 = line.split(':')
        result_value = int(split1[0])
        array_numbers = split1[1].strip().split(" ")
        array_numbers = list(map(int, array_numbers))
        if prune_exact(array_numbers, result_value):
            counter += result_value
            continue
        start_node = Node(array_numbers[0],result_value)
        node_list = [start_node]
        node_list = go_through_nodes(array_numbers,node_list)
        if node_list:
            for node in node_list:
                if node:
                    if node.get_value() == start_node.get_result_value():
                        counter += result_value
                        break

print(counter)



#PART 2

class Node():
    def __init__(self, value, result_value):
        self.value = value
        self.result_value = result_value

    def add_mul(self,level):
        value = self.value * array_numbers[level]
        if value <= self.result_value:
            return Node(value, self.result_value)
        else:
            return None

    def add_sum(self,level):
        value = self.value + array_numbers[level]
        if value <= self.result_value:
            return Node(value, self.result_value)
        else:
            return None

    def add_cat(self, level):
        value = int(f"{self.value}{array_numbers[level]}")
        if value <= self.result_value:
            return Node(value, self.result_value)
        else:
            return None

    def get_result_value(self):
        return self.result_value

    def get_value(self):
        return self.value

def prune_exact(array_numbers, result_value):
    mult_all = list(itertools.accumulate(array_numbers, operator.mul))[-1]
    if mult_all == result_value or sum(array_numbers) == result_value:
        return True
    else:
        return False


def go_through_nodes(array_numbers,node_list):
    for level in range(1,len(array_numbers)):
        node_list_new = []
        for node in node_list:
            if node.add_mul(level):
                node_list_new.append(node.add_mul(level))
            if node.add_sum(level):
                node_list_new.append(node.add_sum(level))
            if node.add_cat(level):
                node_list_new.append(node.add_cat(level))
        if node_list_new:
            node_list = node_list_new[:]
        else:
            return None
    return node_list


with open('input.txt') as file:
    counter = 0
    for line in file:
        split1 = line.split(':')
        result_value = int(split1[0])
        array_numbers = split1[1].strip().split(" ")
        array_numbers = list(map(int, array_numbers))
        if prune_exact(array_numbers, result_value):
            counter += result_value
            continue
        start_node = Node(array_numbers[0],result_value)
        node_list = [start_node]
        node_list = go_through_nodes(array_numbers,node_list)
        if node_list:
            for node in node_list:
                if node:
                    if node.get_value() == start_node.get_result_value():
                        counter += result_value
                        break

print(counter)
