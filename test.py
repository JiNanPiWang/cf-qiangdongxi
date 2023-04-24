class Parent:
    def __init__(self):
        self.name = "Parent"

    def greet(self):
        print(f"Hello, I'm {self.name}")

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.name = "Child"

    def say_hello(self):
        # 不需要传递 self 参数
        super().greet()

child = Child()
child.say_hello()  # 输出：Hello, I'm C