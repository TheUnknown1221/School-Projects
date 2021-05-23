class people:
    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def user_lookup(self):
        print(f"name: {self.name}, age: {self.age}")


class manager(people):
    def __init__(self, name, age, company_branch):
        super().__init__(name, age)
        self.company_branch = company_branch

    def branch_lookup(self):
        return self.company_branch


p1 = people("bob", 29)
m1 = manager("sam", 23, "paper machine")
p1.user_lookup()
print(m1.branch_lookup)
