""" discombobulator.py
Scramble memory banks according to day 6 of advent of code.
"""


def redistribute(memstate):
    """ redistribute(memstate)
    Sweep the memory and redistribute the larges memory pool
    """
    pool_index = memstate.index(max(memstate))
    redistribution_pool = memstate[pool_index]
    memstate[pool_index] = 0

    while redistribution_pool > 0:
        pool_index += 1
        if pool_index == len(memstate):
            pool_index = 0
        memstate[pool_index] += 1
        redistribution_pool -= 1
    return list(memstate)


def shake(membank):
    """ shake(membank)
    Shake the membank until we find an infinite loop. Return the number of
    passes it took to get there.
    """
    iterations = 0
    found_states = [membank]

    while True:
        iterations += 1
        next_state = redistribute(list(found_states[-1]))
        if next_state in found_states:
            return (iterations, iterations - found_states.index(next_state))
        found_states.append(next_state)


def main():
    """ main()
    Get the input and shake it off!
    """
    start = [10, 3, 15, 10, 5, 15, 5, 15, 9, 2, 5, 8, 5, 2, 3, 6]
    print shake(start)


if __name__ == '__main__':
    main()
