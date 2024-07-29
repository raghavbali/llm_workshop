# source: https://stackoverflow.com/a/31631711
def humanbytes(B):
    """Return the given bytes as a human friendly KB, MB, GB, or TB string."""
    UNIT = 1000
    B = float(B)
    KB = float(UNIT)
    MB = float(KB ** 2) # 1,048,576
    GB = float(KB ** 3) # 1,073,741,824
    TB = float(KB ** 4) # 1,099,511,627,776

    if B < KB:
        return '{0} {1}'.format(B,'Bytes' if 0 == B > 1 else 'Byte')
    elif KB <= B < MB:
        return '{0:.2f} KB'.format(B / KB)
    elif MB <= B < GB:
        return '{0:.2f} MB'.format(B / MB)
    elif GB <= B < TB:
        return '{0:.2f} GB'.format(B / GB)
    elif TB <= B:
        return '{0:.2f} TB'.format(B / TB)


def memory_fit(req_memory,cpu_ram, gpu_ram):
    if req_memory<=cpu_ram or req_memory<=gpu_ram:
        return "Yes, fits either CPU or GPU"
    elif req_memory<= cpu_ram + gpu_ram:
        return "Yes, but fit needs both CPU and GPU"
    else:
        return "Nope, does not fit available memory"