class Grandparent:
    def foo(self):
        print("Grandparent's foo")

class Parent(Grandparent):
    def foo(self):
        super().foo()
        print("Parent's foo")

class Child(Parent):
    def foo(self):
        super(Parent, self).foo()
        print("Child's foo")

c = Child()
c.foo()
