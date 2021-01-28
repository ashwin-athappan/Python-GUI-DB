def dict_sort():
    d = {'ram': 5, 'ravi': 15, 'rahul': 10, 'Arun': 6}
    print(d)
    d = sorted(d.items(), key=lambda item: item[1])
    print(dict(d))
    d.reverse()
    print(dict(d))


dict_sort()