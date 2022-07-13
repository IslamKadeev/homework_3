def cache(func):
    result_cache: dict = {}

    def update_cache(*args) -> dict:
        key = args
        if key in result_cache:
            return result_cache.get(key)
        else:
            return_value: int = func(*args)
            result_cache[key] = return_value
        return result_cache.get(key)

    return update_cache


@cache
def multiplier(number: int) -> int:
    return number * 2


if __name__ == "__main__":
    print(multiplier(2))
    print(multiplier(2))
