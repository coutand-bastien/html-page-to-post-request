from datetime import datetime, timedelta
import random
import string
import os

class Randomer:
    '''
    Randomer class to generate random value for the html inputs with min and max if they have
    '''
    def __init__(self):
        pass

    def generate_random_value(self, input_type, min_length=8, max_length=12):
        '''
        Generate random value for the html inputs with min and max if they have
        
        Args:
            input_type (str): Type of the input
            min_length (int, optional): Min length of the value. Defaults to 8.
            max_length (int, optional): Max length of the value. Defaults to 12.
            
        Raises:
            ValueError: Invalid input type
            
        Returns:
            str: Random value
        '''
        if input_type in ["checkbox", "radio"]:
            return self.generate_random_checkbox_value()
        elif input_type == "color":
            return self.generate_random_color_value()
        elif input_type == "date":
            return self.generate_random_date_value(min_length, max_length)
        elif input_type == "datetime-local":
            return self.generate_random_datetime_local_value(min_length, max_length)
        elif input_type == "email":
            return self.generate_random_email_value(min_length, max_length)
        elif input_type in ["file", "image"]:
            return self.generate_random_file_value()
        elif input_type in ["hidden", "text", "password"]:
            return self.generate_random_text_value(min_length, max_length)
        elif input_type == "month":
            return self.generate_random_month_value(min_length, max_length)
        elif input_type in ["number", "range"]:
            return self.generate_random_number_value(min_length, max_length)
        elif input_type == "tel":
            return self.generate_random_tel_value(min_length, max_length)
        elif input_type == "time":
            return self.generate_random_time_value(min_length, max_length)
        elif input_type == "url":
            return self.generate_random_url_value(min_length, max_length)
        elif input_type == "week":
            return self.generate_random_week_value(min_length, max_length)
        else:
            raise ValueError("Invalid input type")

    def generate_random_checkbox_value(self):
        '''
        Generate random checkbox value
        
        Returns:
            bool: Random checkbox value
        '''
        return random.choice([True, False])

    def generate_random_color_value(self):
        '''
        Generate random color value
        
        Returns:
            str: Random color value
        '''
        return '#' + ''.join(random.choices(string.hexdigits, k=6))

    def generate_random_date_value(self, min_date=None, max_date=None):
        '''
        Generate random date value with min and max if they have
        
        Args:
            min_date (str, optional): Min date value. Defaults to None.
            max_date (str, optional): Max date value. Defaults to None.
            
        Returns:
            str: Random date value
        '''
        if min_date: min_date = datetime.strptime(min_date, "%Y-%m-%d").date()
        if max_date: max_date = datetime.strptime(max_date, "%Y-%m-%d").date()

        if min_date and max_date:
            delta = max_date - min_date
            random_days = random.randint(0, delta.days)
            random_date = min_date + timedelta(days=random_days)
        elif min_date:
            delta = datetime.today().date() - min_date
            random_days = random.randint(0, delta.days)
            random_date = min_date + timedelta(days=random_days)
        elif max_date:
            today = datetime.today().date()
            delta = max_date - today
            random_days = random.randint(0, delta.days)
            random_date = today + timedelta(days=random_days)
        else:
            year = random.randint(1900, 2100)
            month = random.randint(1, 12)
            day = random.randint(1, 28)
            random_date = datetime(year, month, day).date()

        return random_date.strftime("%Y-%m-%d")

    def generate_random_datetime_local_value(self, min_date=None, max_date=None):
        '''
        Generate random datetime-local value with min and max if they have
        
        Args:
            min_date (str, optional): Min date value. Defaults to None.
            max_date (str, optional): Max date value. Defaults to None.
        
        Returns:
            str: Random datetime-local value
        '''
        if min_date:
            min_date = datetime.strptime(min_date, "%Y-%m-%d").date()
        if max_date:
            max_date = datetime.strptime(max_date, "%Y-%m-%d").date()

        today = datetime.today().date()

        if min_date and max_date:
            delta = max_date - min_date
            random_days = random.randint(0, delta.days)
            random_date = min_date + timedelta(days=random_days)
        elif min_date:
            delta = today - min_date
            random_days = random.randint(0, delta.days)
            random_date = min_date + timedelta(days=random_days)
        elif max_date:
            delta = max_date - today
            random_days = random.randint(0, delta.days)
            random_date = today + timedelta(days=random_days)
        else:
            year = random.randint(1900, 2100)
            month = random.randint(1, 12)
            day = random.randint(1, 28)
            random_date = datetime(year, month, day).date()

        hour = random.randint(0, 23)
        minute = random.randint(0, 59)

        return f"{random_date.strftime('%Y-%m-%d')}T{hour:02}:{minute:02}"

    def generate_random_email_value(self, min_length, max_length):
        '''
        Generate random email value

        Args:
            min_length (int): Min length of email value
            max_length (int): Max length of email value

        Returns:
            str: Random email value
        '''
        email_length = random.randint(min_length, max_length)
        email_name = ''.join(random.choices(string.ascii_lowercase, k=email_length))
        email_domain = ''.join(random.choices(string.ascii_lowercase, k=random.randint(2, 6)))
        return f"{email_name}@{email_domain}.com"

    def generate_random_text_value(self, min_length, max_length):
        '''
        Generate random text value with min and max if they have
        
        Args:
            min_length (int): Min length of text value
            max_length (int): Max length of text value
            
        Returns:
            str: Random text value
        '''
        value_length = random.randint(min_length, max_length)
        return ''.join(random.choices(string.ascii_letters + string.digits, k=value_length))

    def generate_random_file_value(self, file_type="png"):
        '''
        Generate random file value with file type
        
        Args:
            file_type (str, optional): File type. Defaults to "png".
        
        Returns:
            file: Random file value
        '''
        file_path = os.path.join(self.file_folder, f"file.{file_type}")
        return open(file_path, "rb")

    def generate_random_month_value(self, min_month=None, max_month=None):
        '''
        Generate random month value with min and max if they have

        Args:
            min_month (str, optional): Min month value. Defaults to None.
            max_month (str, optional): Max month value. Defaults to None.

        Returns:
            str: Random month value
        '''            
        if min_month:
            min_month = datetime.strptime(min_month, "%Y-%m").date()
        if max_month:
            max_month = datetime.strptime(max_month, "%Y-%m").date()

        today = datetime.today().date()

        if min_month and max_month:
            delta = max_month - min_month
            random_months = random.randint(0, delta.days // 30)  # Approximation de mois à 30 jours
            random_date = min_month + timedelta(days=random_months * 30)
        elif min_month:
            delta = today - min_month
            random_months = random.randint(0, delta.days // 30)  # Approximation de mois à 30 jours
            random_date = min_month + timedelta(days=random_months * 30)
        elif max_month:
            delta = max_month - today
            random_months = random.randint(0, delta.days // 30)  # Approximation de mois à 30 jours
            random_date = today + timedelta(days=random_months * 30)
        else:
            year = random.randint(1900, 2100)
            month = random.randint(1, 12)
            random_date = datetime(year, month, 1).date()

        return random_date.strftime("%Y-%m")

    def generate_random_number_value(self, min_length, max_length):
        '''
        Generate random number value with min and max if they have
        
        Args:
            min_length (int): Min length of number value
            max_length (int): Max length of number value
            
        Returns:
            str: Random number value
        '''
        return random.randint(min_length, max_length)

    def generate_random_tel_value(self, min_length, max_length):
        '''
        Generate random tel value with min and max if they have

        Args:
            min_length (int): Min length of tel value
            max_length (int): Max length of tel value

        Returns:
            str: Random tel value
        '''
        tel_length = random.randint(min_length, max_length)
        return ''.join(random.choices(string.digits, k=tel_length))

    def generate_random_time_value(self, min_time=None, max_time=None):
        '''
        Generate random time value with min and max if they have
        
        Args:
            min_time (str, optional): Min time value. Defaults to None.
            max_time (str, optional): Max time value. Defaults to None.
            
        Returns:
            str: Random time value
        '''
        if min_time:
            min_time = datetime.strptime(min_time, "%H:%M").time()
        if max_time:
            max_time = datetime.strptime(max_time, "%H:%M").time()

        if min_time and max_time:
            min_time_seconds = min_time.hour * 3600 + min_time.minute * 60
            max_time_seconds = max_time.hour * 3600 + max_time.minute * 60
            random_seconds = random.randint(min_time_seconds, max_time_seconds)
        elif min_time:
            min_time_seconds = min_time.hour * 3600 + min_time.minute * 60
            max_time_seconds = 23 * 3600 + 59 * 60
            random_seconds = random.randint(min_time_seconds, max_time_seconds)
        elif max_time:
            min_time_seconds = 0
            max_time_seconds = max_time.hour * 3600 + max_time.minute * 60
            random_seconds = random.randint(min_time_seconds, max_time_seconds)
        else:
            random_seconds = random.randint(0, 23 * 3600 + 59 * 60)

        hours = random_seconds // 3600
        minutes = (random_seconds % 3600) // 60

        return f"{hours:02}:{minutes:02}"

    def generate_random_url_value(self, min_length, max_length):
        '''
        Generate random url value with min and max if they have

        Args:
            min_length (int): Min length of url value
            max_length (int): Max length of url value

        Returns:
            str: Random url value
        '''
        url_length = random.randint(min_length, max_length)
        url = ''.join(random.choices(string.ascii_lowercase + string.digits, k=url_length))
        return f"https://example.com/{url}"

    def generate_random_week_value(self, min_date=None, max_date=None):
        '''
        Generate random week value with min and max if they have

        Args:
            min_date (str, optional): Min date value. Defaults to None.
            max_date (str, optional): Max date value. Defaults to None.

        Returns:
            str: Random week value
        '''
        if min_date:
            min_date = datetime.strptime(min_date, "%Y-W%W").date()
        if max_date:
            max_date = datetime.strptime(max_date, "%Y-W%W").date()

        today = datetime.today().date()

        if min_date and max_date:
            delta = max_date - min_date
            random_weeks = random.randint(0, delta.days // 7)
            random_date = min_date + timedelta(weeks=random_weeks)
        elif min_date:
            delta = today - min_date
            random_weeks = random.randint(0, delta.days // 7)
            random_date = min_date + timedelta(weeks=random_weeks)
        elif max_date:
            delta = max_date - today
            random_weeks = random.randint(0, delta.days // 7)
            random_date = today + timedelta(weeks=random_weeks)
        else:
            year = random.randint(1900, 2100)
            week = random.randint(1, 52)
            random_date = datetime.strptime(f"{year}-W{week:02}", "%Y-W%W").date()

        return random_date.strftime("%Y-W%W")