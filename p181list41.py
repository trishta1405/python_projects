desserts = ['cheesecake', 'brownie', 'ice cream', 'tiramisu', 'pavlova']

print(len(desserts))

desserts.insert(0, 'macaron')
print(desserts)

desserts.remove('ice cream')
pavlova_index = desserts.index('pavlova')
desserts.insert(pavlova_index + 1, 'ice cream')
print(desserts)
