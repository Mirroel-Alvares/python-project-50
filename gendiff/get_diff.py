def get_diff(file1, file2):
    all_keys = sorted(set(file1.keys()).union(set(file2.keys())))
    result = []

    for key in all_keys:
        value1 = file1.get(key)
        value2 = file2.get(key)

        if value1 is not None and value2 is not None:
            if value1 != value2:
                result.append(f"- {key}: {value1}")
                result.append(f"+ {key}: {value2}")
            else:
                result.append(f"  {key}: {value1}")
        elif value1 is not None:
            result.append(f"- {key}: {value1}")
        elif value2 is not None:
            result.append(f"+ {key}: {value2}")

    return "{\n" + "\n".join(result) + "\n}"
