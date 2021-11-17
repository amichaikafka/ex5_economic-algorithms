class Agent():
    """
    Basic implementation of Agent class.
    The constructor gets a list with values, each index of the list represent an item
    and the value of this index its how much the agent think this item worth.
    """

    def __init__(self, lst_val: list = []) -> None:
        self.lst_val = lst_val

    def item_value(self, item_index: int) -> float:
        return self.lst_val[item_index]


def sum_val(items: list = [], agent: Agent = None):
    """
    Compute the sum of all the values of the items according to this agent's evaluation
    :param items:
    :param agent:
    :return:
    """
    sum = 0
    for i in items:
        sum += agent.item_value(i)
    return sum


def is_EF1(agents: list[Agent], bundles: list[list[int]]) -> bool:
    """
    Check if this division  is EF1
    :param agents:
    :param bundles:
    :return:
    >>> a = Agent([1, 2, 3, 4, 5, 6, 7, 8, 9])
    >>> b = Agent([9, 8, 7, 6, 5, 4, 3, 2, 1])
    >>> c = Agent([9, 2, 7, 4, 5, 6, 3, 8, 1])
    >>> is_EF1([a, b], [[0, 1, 2, 3, 4], [5, 6, 7, 8]])
    False
    >>> is_EF1([a, b], [[5, 6, 7, 8], [0, 1, 2, 3, 4]])
    True
    >>> is_EF1([a, b,c], [[6, 7, 8], [0, 1, 2],[3,4,5]])
    True
    >>> is_EF1([a, b, c], [[6, 7, 8], [3, 1, 2], [0, 4, 5]])
    True
    >>> is_EF1([a, b, c], [[6, 7, 8], [4, 1, 2], [0, 3, 5]])
    True
    >>> is_EF1([a, b, c], [[6, 7, 8], [1, 3], [2,0, 4, 5]])
    False
    >>> is_EF1([a, b, c], [[6, 7, 8], [4, 1, 2], [0, 3, 5]])
    True
    >>> is_EF1([a, b, c], [[6, 4], [1, 3], [2, 0, 7, 5,8]])
    False
    >>> is_EF1([a, b, c], [[], [], [0,1,2,3,4,5,6,7,8]])
    False
    >>> is_EF1([a, b, c], [ [0,1,2,3], [],[4,5,6,7,8]])
    False
    >>> is_EF1([a, b, c], [ [], [],[4]])
    True
    >>> is_EF1([a, b], [ [4],[]])
    True
    """
    # for i in range(len(agents)):
    #     for j in range(len(agents)):
    #         if len(bundles[i]) == 0 and len(bundles[j]) > 1:
    #             return False
    for i in range(len(agents)):
        sum = sum_val(bundles[i], agents[i])
        for j in range(len(agents)):
            if i != j and len(bundles[j]) > 0:
                max_val = max(bundles[j], key=lambda item: agents[i].item_value(item))
                bundles[j].remove(max_val)
                j_sum_val = sum_val(bundles[j], agents[i])
                if sum < j_sum_val:
                    return False
                bundles[j].append(max_val)
    return True


if __name__ == '__main__':
    import doctest

    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))
