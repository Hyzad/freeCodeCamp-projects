import numpy as np

def calculate(nums):
    if len(nums) < 9 or len(nums) > 9:
        raise ValueError("List must contain nine numbers.")
    array = np.array([
        nums[0:3], 
        nums[3:6],
        nums[6:]
        ])

    calc_dict = {}
    calc_dict["mean"] = [list(array.mean(axis=0)), list(array.mean(axis=1)), array.mean()]
    calc_dict["variance"] = [list(array.var(axis=0)), list(array.var(axis=1)), array.var()]
    calc_dict["standard deviation"] = [list(array.std(axis=0)), list(array.std(axis=1)), array.std()]
    calc_dict["max"] = [list(array.max(axis=0)), list(array.max(axis=1)), array.max()]
    calc_dict["min"] = [list(array.min(axis=0)), list(array.min(axis=1)), array.min()]
    calc_dict["sum"] = [list(array.sum(axis=0)), list(array.sum(axis=1)), array.sum()]
    return calc_dict


