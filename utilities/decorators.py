from functools import wraps
from utilities.sorting import SortUtils
from mysql.connector import Error

def transaction(dictionary=True):
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            conn = self.database_manager.connect()
            if not conn:
                return None
            cursor = conn.cursor(dictionary=dictionary)
            try:
                result = func(self, cursor, conn, *args, **kwargs)
                conn.commit()
                # print(f'Operation: [{func.__name__} successful.]')
                return result
            except Error as e:
                conn.rollback()
                print(f'Database transaction error: {e}')
                return None
            finally:
                cursor.close()
                self.database_manager.close_conn()
        return wrapper
    return decorator


def sorted_by(attr_name, reverse=False):
    """
    Decorator that automatically uses Merge Sort on a list returned by a method.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            # 1. Get the list from the Service/Transaction
            data_list = func(self, *args, **kwargs)

            # 2. If it's a list, sort it using our Merge Sort logic
            if isinstance(data_list, list) and len(data_list) > 1:
                return SortUtils.merge_sort(
                    data_list,
                    key=lambda x: getattr(x, attr_name, ""),
                    reverse=reverse
                )
            return data_list
        return wrapper
    return decorator