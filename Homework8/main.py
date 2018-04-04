from Polynomial import Polynomial

p = Polynomial('../test/poli.txt')
print(p.approximate_roots(0.1, retries=10, kmax=100, epsilon=0.000000001, f=p.get_result_horner))
print([x if p.get_second_derivative_value(float(x)) > 0 else None for x in p.approximate_roots(0.1, retries=2, kmax=100, epsilon=0.000000001, f=p.get_derivative_value1)])
print([x if p.get_second_derivative_value(float(x)) > 0 else None for x in p.approximate_roots(0.1, retries=2, kmax=100, epsilon=0.000000001, f=p.get_derivative_value2)])

