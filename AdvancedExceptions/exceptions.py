import logging

values = [10, 5, 6, 0, 9, 8, 'Hello',2]

for value in values:
    try:
        print(10 / int(value))
    # Handling multiple exceptions in one except block
    except ZeroDivisionError as e:
        # print(str(e))
        pass
    except ValueError as e:
        print(f'Catching exception {e}')
        raise
    # Not recommended - use logging instead printing it
    except Exception as e:
        logging.exception(f'Unexpected exception {e}')
    # The opposite of except,
    # will run only if no exception was raised in the try block,
    # and will not run if an exception was raised and handled in the except block
    else:
        print('No exception was raised')
    # Will run whether an exception is raised or not,
    # and will run before any exception is propagated up the call stack
    finally:
        print(f'Finished processing value: {value}')
