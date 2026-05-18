import random

def initialize_pop(course_map, valid_rooms, assignments, room_cap_map, days, num_timeslots, num_chr):
    """
    Initialize population with reduced hard constraint violations.
    
    Hard constraints:
    1. Lecturer cannot teach multiple classes at same time
    2. Room cannot be used by multiple classes at same time
    3. Level cannot have multiple classes from same dept at same time
    """
    population = []

    for _ in range(0, num_chr):
        chromosome = []
        
        occupied_rooms = set()
        assigned_lecturers = set()
        assigned_levels = set()

        for course in course_map:
            c_index, level, duration, departments, class_size = course
            
            l_index = assignments[c_index]
            
            # Step 1: Select best available room upfront
            r_index = _select_best_room(
                valid_rooms[c_index], 
                room_cap_map, 
                class_size, 
                occupied_rooms,
                days,
                duration,
                num_timeslots
            )
            
            # If no valid room found, pick first valid room
            if r_index is None:
                r_index = valid_rooms[c_index][0] if valid_rooms[c_index] else 0

            # Step 2: Find valid time slot with constraint checking
            if duration > 1:
                # Multi-timeslot courses need consecutive slots
                day, time_1, time_2 = _find_valid_time_slots_duration_2(
                    l_index,
                    r_index,
                    level,
                    departments,
                    day=None,
                    duration=duration,
                    assigned_lecturers=assigned_lecturers,
                    occupied_rooms=occupied_rooms,
                    assigned_levels=assigned_levels,
                    days=days,
                    num_timeslots=num_timeslots,
                    max_retries=100
                )
                
                if day is not None and time_1 is not None and time_2 is not None:
                    # Add to tracking sets
                    assigned_lecturers.add((l_index, day, time_1))
                    assigned_lecturers.add((l_index, day, time_2))
                    occupied_rooms.add((r_index, day, time_1))
                    occupied_rooms.add((r_index, day, time_2))
                    for dept in departments:
                        assigned_levels.add((level, dept, day, time_1))
                        assigned_levels.add((level, dept, day, time_2))
                    
                    # Create genes
                    gene_1 = (c_index, l_index, r_index, level, day, time_1)
                    gene_2 = (c_index, l_index, r_index, level, day, time_2)
                    chromosome.append(gene_1)
                    chromosome.append(gene_2)
                else:
                    # Fallback: just assign to first available slot pair
                    day = random.randint(0, days - 1)
                    time_1 = random.randint(0, num_timeslots - 2)
                    time_2 = time_1 + 1
                    assigned_lecturers.add((l_index, day, time_1))
                    assigned_lecturers.add((l_index, day, time_2))
                    occupied_rooms.add((r_index, day, time_1))
                    occupied_rooms.add((r_index, day, time_2))
                    for dept in departments:
                        assigned_levels.add((level, dept, day, time_1))
                        assigned_levels.add((level, dept, day, time_2))
                    gene_1 = (c_index, l_index, r_index, level, day, time_1)
                    gene_2 = (c_index, l_index, r_index, level, day, time_2)
                    chromosome.append(gene_1)
                    chromosome.append(gene_2)
            else:
                # Single-timeslot courses
                day, time = _find_valid_time_slot(
                    l_index,
                    r_index,
                    level,
                    departments,
                    assigned_lecturers=assigned_lecturers,
                    occupied_rooms=occupied_rooms,
                    assigned_levels=assigned_levels,
                    days=days,
                    num_timeslots=num_timeslots,
                    max_retries=100
                )
                
                if day is not None and time is not None:
                    # Add to tracking sets
                    assigned_lecturers.add((l_index, day, time))
                    occupied_rooms.add((r_index, day, time))
                    for dept in departments:
                        assigned_levels.add((level, dept, day, time))
                    
                    gene = (c_index, l_index, r_index, level, day, time)
                    chromosome.append(gene)
                else:
                    # Fallback: just assign to random slot
                    day = random.randint(0, days - 1)
                    time = random.randint(0, num_timeslots - 1)
                    assigned_lecturers.add((l_index, day, time))
                    occupied_rooms.add((r_index, day, time))
                    for dept in departments:
                        assigned_levels.add((level, dept, day, time))
                    gene = (c_index, l_index, r_index, level, day, time)
                    chromosome.append(gene)
        
        population.append(chromosome)

    return population


def _select_best_room(valid_rooms, room_cap_map, class_size, occupied_rooms, days, duration, num_timeslots):
    """
    Select best room that can accommodate class size, preferring less occupied rooms.
    """
    valid_candidates = []
    
    for rm in valid_rooms:
        capacity = room_cap_map[rm]
        if capacity >= class_size:
            # Count how many times this room is occupied
            occupied_count = sum(1 for (r, _, _) in occupied_rooms if r == rm)
            valid_candidates.append((rm, occupied_count))
    
    if not valid_candidates:
        return None
    
    # Sort by occupancy (prefer less occupied rooms)
    valid_candidates.sort(key=lambda x: x[1])
    return valid_candidates[0][0]


def _find_valid_time_slot(l_index, r_index, level, departments, assigned_lecturers, 
                          occupied_rooms, assigned_levels, days, num_timeslots, max_retries=100):
    """
    Find a valid time slot that satisfies all hard constraints for single-timeslot courses.
    Returns (day, time) or (None, None) if no valid slot found.
    """
    for _ in range(max_retries):
        day = random.randint(0, days - 1)
        time = random.randint(0, num_timeslots - 1)
        
        # Check all hard constraints
        # 1. Lecturer not already assigned at this time
        if (l_index, day, time) in assigned_lecturers:
            continue
        
        # 2. Room not already occupied at this time
        if (r_index, day, time) in occupied_rooms:
            continue
        
        # 3. Level/department not already assigned at this time
        level_conflict = any((level, dept, day, time) in assigned_levels for dept in departments)
        if level_conflict:
            continue
        
        # All constraints satisfied
        return day, time
    
    # If max retries exhausted, return None
    return None, None


def _find_valid_time_slots_duration_2(l_index, r_index, level, departments, day=None, duration=2,
                                      assigned_lecturers=None, occupied_rooms=None, assigned_levels=None,
                                      days=4, num_timeslots=10, max_retries=100):
    """
    Find valid consecutive time slots that satisfy all hard constraints for multi-timeslot courses.
    Returns (day, time_1, time_2) or (None, None, None) if no valid slot found.
    """
    if assigned_lecturers is None:
        assigned_lecturers = set()
    if occupied_rooms is None:
        occupied_rooms = set()
    if assigned_levels is None:
        assigned_levels = set()
    
    for _ in range(max_retries):
        day = random.randint(0, days - 1)
        time_1 = random.randint(0, num_timeslots - 2)
        time_2 = time_1 + 1
        
        # Check all hard constraints for both slots
        # 1. Lecturer not already assigned at either time
        if (l_index, day, time_1) in assigned_lecturers or (l_index, day, time_2) in assigned_lecturers:
            continue
        
        # 2. Room not already occupied at either time
        if (r_index, day, time_1) in occupied_rooms or (r_index, day, time_2) in occupied_rooms:
            continue
        
        # 3. Level/department not already assigned at either time
        level_conflict_1 = any((level, dept, day, time_1) in assigned_levels for dept in departments)
        level_conflict_2 = any((level, dept, day, time_2) in assigned_levels for dept in departments)
        if level_conflict_1 or level_conflict_2:
            continue
        
        # All constraints satisfied
        return day, time_1, time_2
    
    # If max retries exhausted, return None
    return None, None, None
