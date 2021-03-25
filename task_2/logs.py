def get_logs(log):
    text = log.split()
    result = {}
    for i in text:
        if len(i) == 5:
            count = text.count(i)
            result[i] = count
    return result


def print_sorted_result(result):
    sorted_result = [(k, result[k]) for k in sorted(
        result, 
        key=result.get, 
        reverse=True
    )]
    for key, value in sorted_result:
        print(key, value)


if __name__ == '__main__':
    print('Введите путь к лог-файлу')
    path = input()
    log_file = open(path)
    log = log_file.read()
    result = get_logs(log)
    print_sorted_result(result)