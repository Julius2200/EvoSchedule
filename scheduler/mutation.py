import random


def group_blocks(chromo):
    chromosome = chromo.copy()
    """Return blocks of consecutive genes, preserving pair blocks and the final single gene."""
    blocks = []
    i = 0
    while i < len(chromosome):
        t1 = chromosome[i]
        block = []

        if i + 1 < len(chromosome):
            t2 = chromosome[i + 1]
            # check if they are a double period block
            is_double = (t1[:5] == t2[:5] and t2[5] == t1[5] + 1)
            if is_double:
                block.append(t1)
                block.append(t2)
                i += 2
            else:
                block.append(t1)
                i += 1
        else:
            block.append(t1)
            i += 1

        blocks.append(block)
    return blocks

def mutate(ch1, ch2, day, m_rate=0.1, assignments=None, valid_rooms=None):
    blocked1 = group_blocks(ch1)
    blocked2 = group_blocks(ch2)
    l1 = len(ch1)
    l2 = len(ch2)

    mutated1 = []
    mutated2 = []

    for block in blocked1:
        if len(block) > 1:
            entry1 = block[0]
            entry2 = block[1]

            check = random.random()
            if check <= m_rate:
                mutation_type = random.random()
                c, l, r, lvl, d, t = entry1
                if mutation_type < 0.5:  # 50% chance: change day
                    new_day = random.randint(0, day - 1)
                    new_entry = (c, l, r, lvl, new_day, t)
                    mutated1.append(new_entry)

                    c, l, r, lvl, d, t = entry2
                    new_entry = (c, l, r, lvl, new_day, t)
                    mutated1.append(new_entry)
                elif valid_rooms is not None and c in valid_rooms and valid_rooms[c]:  # 50% chance: change room
                    new_r = random.choice(valid_rooms[c])
                    new_entry = (c, l, new_r, lvl, d, t)
                    mutated1.append(new_entry)

                    c, l, r, lvl, d, t = entry2
                    new_entry = (c, l, new_r, lvl, d, t)
                    mutated1.append(new_entry)
                else:
                    mutated1.append(entry1)
                    mutated1.append(entry2)
            else:
                mutated1.append(entry1)
                mutated1.append(entry2)

        else:
            entry = block[0]
            check = random.random()
            if check <= m_rate:
                mutation_type = random.random()
                c, l, r, lvl, d, t = entry
                if mutation_type < 0.5:  # 50% chance: change day and time
                    new_day = random.randint(0, day - 1)
                    new_time = random.randint(0, 9)
                    new_entry = (c, l, r, lvl, new_day, new_time)
                    mutated1.append(new_entry)
                elif valid_rooms is not None and c in valid_rooms and valid_rooms[c]:  # 50% chance: change room
                    new_r = random.choice(valid_rooms[c])
                    new_entry = (c, l, new_r, lvl, d, t)
                    mutated1.append(new_entry)
                else:
                    mutated1.append(entry)
            else:
                mutated1.append(entry)
    
    for block in blocked2:
        if len(block) > 1:
            entry1 = block[0]
            entry2 = block[1]

            check = random.random()
            if check <= m_rate:
                mutation_type = random.random()
                c, l, r, lvl, d, t = entry1
                if mutation_type < 0.5:  # 50% chance: change day
                    new_day = random.randint(0, day - 1)
                    new_entry = (c, l, r, lvl, new_day, t)
                    mutated2.append(new_entry)

                    c, l, r, lvl, d, t = entry2
                    new_entry = (c, l, r, lvl, new_day, t)
                    mutated2.append(new_entry)
                elif valid_rooms is not None and c in valid_rooms and valid_rooms[c]:  # 50% chance: change room
                    new_r = random.choice(valid_rooms[c])
                    new_entry = (c, l, new_r, lvl, d, t)
                    mutated2.append(new_entry)

                    c, l, r, lvl, d, t = entry2
                    new_entry = (c, l, new_r, lvl, d, t)
                    mutated2.append(new_entry)
                else:
                    mutated2.append(entry1)
                    mutated2.append(entry2)
            else:
                mutated2.append(entry1)
                mutated2.append(entry2)
        else:
            entry = block[0]
            check = random.random()
            if check <= m_rate:
                mutation_type = random.random()
                c, l, r, lvl, d, t = entry
                if mutation_type < 0.5:  # 50% chance: change day and time
                    new_day = random.randint(0, day - 1)
                    new_time = random.randint(0, 9)
                    new_entry = (c, l, r, lvl, new_day, new_time)
                    mutated2.append(new_entry)
                elif valid_rooms is not None and c in valid_rooms and valid_rooms[c]:  # 50% chance: change room
                    new_r = random.choice(valid_rooms[c])
                    new_entry = (c, l, new_r, lvl, d, t)
                    mutated2.append(new_entry)
                else:
                    mutated2.append(entry)
            else:
                mutated2.append(entry)

    return mutated1, mutated2