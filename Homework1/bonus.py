import random
import timeit

""" Proof that multiplication is more expensive that addition """


print(timeit.timeit("a*b",
                    setup="""import random
import sys
max_float = sys.float_info.max
a= random.getrandbits(1024)
b= random.getrandbits(1024)
              """,
                    number=1000
                    ))

print(timeit.timeit("a+b",
                    setup="""import random
import sys
max_float = sys.float_info.max
a= random.getrandbits(1024)
b= random.getrandbits(1024)
              """,
                    number=1000
                    ))
