class CyclicIterator:
    def __init__(self, container: iter):
        self.obj = container
        self.iter = iter(container)

    def __iter__(self) -> object:
        return self

    def __next__(self) -> object:
        try:
            return next(self.iter)
        except StopIteration:
            self.iter = iter(self.obj)
            return next(self.iter)


if __name__ == "__main__":
    cyclic_iterator = CyclicIterator(range(3))
    for i in cyclic_iterator:
        print(i)
