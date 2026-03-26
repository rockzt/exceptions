import sys

print(sys.platform)


# Creating  exception class
class WrongPlatformError(Exception):
    """Custom exception for wrong platform"""
    pass

'''
if not sys.platform.startswith('linux'):
    raise WrongPlatformError('Wrong OS!')
'''
#raise Exception("Raising custom exception for testing purposes")


# Using the assert Keyword
assert sys.platform.startswith('linux'), "Wrong OS!"

'''
if not sys.platform.startswith('linux'):
    raise AssertionError('Wrong OS!')
'''