def gen_plain_format(diff, path=''):
    result_string = ''

    for value in diff:
        key = value['key']
        status = value.get('status')
        new_path = f"{path}.{key}" if path else key

        if status == 'nested':
            result_string += gen_plain_format(value['value'], new_path)

        elif status == 'added':
            result_string += (
                f"Property '{new_path}' was added with value: "
                f"{to_str(value['value'])}\n"
            )

        elif status == 'deleted':
            result_string += (
                f"Property '{new_path}' was removed\n"
            )

        elif status == 'changed':
            result_string += (
                f"Property '{new_path}' was updated."
                f" From {to_str(value['old_value'])} "
                f"to {to_str(value['new_value'])}\n"
            )

    return result_string


def to_str(value):
    if isinstance(value, dict) or isinstance(value, list):
        return '[complex value]'
    elif value is None:
        return 'null'
    elif value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif isinstance(value, int):
        return value
    else:
        return f"'{value}'"
