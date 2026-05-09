def statistika(*args):
    return {
        "ortacha": sum(args) / len(args),
        "min": min(args),
        "max": max(args)
    }

print(statistika(3, 7, 2, 9, 1))
# {'ortacha': 4.4, 'min': 1, 'max': 9}
