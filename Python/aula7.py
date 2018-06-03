# Python 3
try:
 1/0
except (RuntimeError, ZeroDivisionError) as e:
   print(e)
else:
   print('No exception')
finally:
   print('Finally')