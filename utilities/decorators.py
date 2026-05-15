from functools import wraps
from mysql.connector import Error

# Importing a sorting utility for the sorting decorator
from utilities.sorting import SortUtils


def transaction(dictionary=True):
    """
    Decorator handling business logic connecting
    stored procedures and services layer
    """
    def decorator(func):
        # Preserving the original function's data for debugging
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            # Initialise a connection object
            conn = self.database_manager.connect()

            if not conn: # Failed to connect
                return None

            # Initialise a cursor object for database interactions
            # dictionary=True allows for mapping results to
            # Python objects via keys
            cursor = conn.cursor(dictionary=dictionary)

            try:
                # A general pattern for all services methods execution
                result = func(self, cursor, conn, *args, **kwargs)

                # Commit if successful
                conn.commit()
                return result

            # Error handling and data integrity
            except Error as e:
                # Cancel the failed action for preserving
                conn.rollback()
                print(f'Database transaction error: {e}')
                return None

            # Eventually close the connection regardless of the result
            finally:
                cursor.close()
                self.database_manager.close_conn()

        return wrapper
    return decorator


def sorted_by(attr_name, reverse=False):
    """
    Decorator implementing the Merge Sort algorithm on a loaded data
    returned by a method.
    """
    def decorator(func):
        # Preserving the original function's data for debugging
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            # Get the list from the service/transaction
            data_list = func(self, *args, **kwargs)

            # Sort the list using Merge Sort logic
            if isinstance(data_list, list) and len(data_list) > 1:
                # Use getattr to dynamically access properties defined
                # in the Model layer
                return SortUtils.merge_sort(
                    data_list,
                    key=lambda x: getattr(x, attr_name, ""),
                    reverse=reverse
                )
            # Return a sorted list
            return data_list

        return wrapper
    return decorator