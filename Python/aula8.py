try:
    pass
except Exception, e:
    raise
else: # Else means no exception
    pass
finally: # It will always execute
    pass

# Python 3
try:
 1/0
except (Exception, ZeroDivisionError) as e:
   print(e)
else:
   print('No exception')
finally:
   print('Finally')