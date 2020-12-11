from utils import FileUtils
import collections
import numpy as np

def get_adapter_chain(adapters, current_jolt = 0):
    valid_adapters = list(filter(lambda adapter: current_jolt < adapter <= current_jolt + 3, adapters))
    if valid_adapters:
        next_adapter = min(valid_adapters)
        return [current_jolt] + get_adapter_chain([ad for ad in adapters if ad != next_adapter], current_jolt=next_adapter)
    else:
        return [current_jolt, current_jolt + 3]

def get_jolt_diff_count(joined_adapters, diff):
    return list(np.diff(joined_adapters)).count(diff)

def get_distinct_list_count(adapters):
    size = len(adapters)
    combos_up_to_index = [1] * size
    for i in range(1, size):
        combos_up_to_index[i] = combos_up_to_index[i - 1]
        if i > 1 and adapters[i] - adapters[i - 2] <= 3:
            combos_up_to_index[i] += combos_up_to_index[i - 2]
        if i > 2 and adapters[i] - adapters[ i - 3] <= 3:
            combos_up_to_index[i] += combos_up_to_index[i - 3]
    return combos_up_to_index[-1]
    pass

if __name__ == "__main__":
    adapter_chain = get_adapter_chain(FileUtils.int_input())
    print( get_jolt_diff_count(adapter_chain, 1) * get_jolt_diff_count(adapter_chain, 3) )
    print( get_distinct_list_count(adapter_chain) )