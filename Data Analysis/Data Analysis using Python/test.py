class dog:
    a = ''
    def __init__(self):
        self.a = 'init'
    def display(self):
        print(self.a)

@(lambda f: setattr(dog, "on_leash", f))
def test_fn():
    print('bark, bark')

print(dog.on_leash())