# -------------------------------#
# ========== SETTINGS ========== #
# -------------------------------#

# Relative weights of the materials.
weights = {'wood': 1, 'crystal': 4, 'steel': 16}  # default = {'wood': 1, 'crystal': 4, 'steel': 16}

# Amounts of initial counterbalance materials.
base_counter_materials = {'wood': 4, 'crystal': 0, 'steel': 0}  # default = {'wood': 4, 'crystal': 0, 'steel': 0}

# Amounts of available additional counterbalance materials.
extra_counter_materials = {'wood': 2, 'crystal': 2, 'steel': 2}  # default = {'wood': 2, 'crystal': 2, 'steel': 2}

# Maximum number of counterbalance materials.
counter_max_materials = 8  # default = 8

# Amounts of balance ball materials.
ball_materials = {'wood': 7, 'crystal': 1, 'steel': 0}  # default = {'wood': 7, 'crystal': 1, 'steel': 0}

# Positions of the fulcrum and their moment multipliers for the counterbalance and balance ball weights, respectively.
fulcrum_positions = {'left': (1, 2), 'middle': (1, 1), 'right': (2, 1)}  # default = {'left': (1, 2), 'middle': (1, 1), 'right': (2, 1)}

# -------------------------------#
# ========== INTERNAL ========== #
# -------------------------------#


def main():
    def weight_sum(mats):
        return sum(weights[k] * v for k, v in mats.items())

    start_counter_weight = weight_sum(base_counter_materials)
    base_ball_weight = weight_sum(ball_materials)

    counter_max_extra_mats = counter_max_materials - sum(base_counter_materials.values())

    def extra_mats_range():
        return range(1 + counter_max_extra_mats)

    import itertools
    counter_mat_combos = [list(itertools.combinations_with_replacement(weights, i)) for i in extra_mats_range()]

    for pos, multipliers in fulcrum_positions.items():
        counter_mult, ball_mult = multipliers
        for i in extra_mats_range():
            for combo in counter_mat_combos[i]:
                if any(combo.count(k) > v for k, v in extra_counter_materials.items()):
                    continue

                base_counter_weight = start_counter_weight + sum(weights[x] for x in combo)

                if counter_mult * base_counter_weight == ball_mult * base_ball_weight:
                    print(f'Fulcrum: {pos}')
                    print(f'Materials: {list(combo)}')
                    print(f'Moments: {counter_mult} * {base_counter_weight} == {ball_mult} * {base_ball_weight}\n')


if __name__ == '__main__':
    main()
