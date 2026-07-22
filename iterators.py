#Using iter() and next()

numbers = [10, 20, 30]

it = iter(numbers)

print(next(it))
print(next(it))
print(next(it))


#Custom Iterator

class Count:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 5:
            x = self.num
            self.num += 1
            return x
        else:
            raise StopIteration

obj = Count()

for i in obj:
    print(i)
