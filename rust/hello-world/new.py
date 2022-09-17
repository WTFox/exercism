import typing as t


def unique_list_of_dicts(list_of_dicts: t.List[dict]) -> list:
    seen = set()
    unique = []
    for item in list_of_dicts:
        contents = tuple(item.items())
        if contents not in seen:
            seen.add(contents)
            unique.append(item)

    return unique


def main():
    list_of_dicts = [
        {"a": 123, "b": 1234},
        {"a": 3222, "b": 1234},
        {"a": 123, "b": 1234},
    ]

    print([dict(t) for t in {tuple(d.items()) for d in list_of_dicts}])
    print(unique_list_of_dicts(list_of_dicts))
