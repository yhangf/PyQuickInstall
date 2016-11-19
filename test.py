import easyargs

@easyargs
def main(name, count=1, greeting='Hello'):
    """A simple greeting program"""
    for i in range(count):
        print('{greeting} {name}!'.format(greeting=greeting, name=name))


if __name__ == '__main__':
    main()
