from faker import Faker
from operator import itemgetter

data = []
generator = Faker('ko-KR')

for i in range(20):
    name_score = (
        generator.name(),
        generator.pyint() % 8 + 10 + (generator.pyint() % 100) / 100)

    data.append(name_score)

result = sorted(data, key=itemgetter(1))

print(result)