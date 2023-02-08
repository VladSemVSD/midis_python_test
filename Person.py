import datetime
import base64

"""
Abstract person class. Conatnis methods both Volunteer an Administrator should have.
"""


class Person():
    def __init__(self, last_name, first_name=None, birth_year=None, email=None, mobile=None, adress=None, profile_picture=None):
        self.first_name = self._is_valid_name(first_name)
        self.last_name = last_name
        self.birth_year = self._is_valid_birth_year(birth_year)
        self.email = self._is_valid_email(email)
        self.mobile = self._clean_number(mobile)
        self.adress = adress
        self.profile_picture = self._encode_picture(profile_picture)
        self._created_at = datetime.datetime.now()

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if value == "":
            print("Provide last name")
        self._last_name = value

    # Method that gets user input for class attributes

    @classmethod
    def user_create(cls):
        return cls(
            input('Last name: '),
            input('Name: '),
            int(input('Birth year: ')),
            input('Email: '),
            input('Mobile: '),
            input('Address: '),
            input('Profile picture path: '),
        )

    def set_last_name(self, last_name):
        while True:
            try:
                last_name.isalpha()
                return last_name
            except ValueError:
                print('Incorrect format')

    # Check if provided name has alphabetical symbols only
    def _is_valid_name(self, first_name):
        if not first_name.isalpha():
            raise ValueError("Provide letters only")
        return first_name

    # Check if provided birt year is > 0, otherwise return 2000
    def _is_valid_birth_year(self, birth_year):
        if birth_year != '':
            if int(birth_year) > 0:
                return int(birth_year)
            else:
                return 2000

    # Check if email contains "@", appends "@gmail.com" if not
    def _is_valid_email(self, email):
        if "@" in email:
            return email
        else:
            return email + "@gmail.com"

    # Clears provided string from aplhabetical chars and returns numbers only
    def _clean_number(self, mobile):
        cleared_mobile = ''.join(ch for ch in mobile if ch.isdigit())
        return cleared_mobile

    # If path provided encodes image to base64
    def _encode_picture(self, filepath):
        if filepath != '':
            with open(filepath, "rb") as img_file:
                base64_enocded = base64.b64encode(
                    img_file.read()).decode('utf-8')
                return base64_enocded

    # Prints persons date as Name + Surname + Email
    def get_full_name(self):
        print(self.name+self.surname+self.email)

    # Sets a profile_pcture attribute to base64 encoded image from provided path
    def add_profile_photo(self, path):
        picture = self._encode_picture(path)
        pattern = "/9j/4"
        try:
            picture.startswith(pattern)
            self.profile_picture = picture
        except Exception:
            raise Exception('File is not a .jpg image')

    # Create foto.jpg in directory from profile_picture attribute
    def write_photo_in_directory(self):
        with open('foto.jpg', 'wb') as f:
            f.write(base64.decodebytes(self.profile_picture.encode('utf-8')))

    def print_data(self):
        print(self.adress)
        print(self.first_name)
        print(self.last_name)


"""
Volunteer class. Inherits from Person class. Has volunterr specific methods and __is_admin attribute set to False
"""


class Volunteer(Person):
    def __init__(self, last_name, first_name=None, birth_year=None, email=None, mobile=None, adress=None, profile_picture=None):
        self.__is_admin = False
        # Some sample data for testing
        self.track_records = {
            datetime.date(2023, 2, 6): {'type': 'glass', 'weight': 354.0, 'volume': 345.0, 'density': 1.0260869565217392},
            datetime.date(2025, 5, 6): {'type': 'paper', 'weight': 45.0, 'volume': 345.0, 'density': 0.13043478260869565},
            datetime.date(2013, 2, 6): {'type': 'glass', 'weight': 354.0, 'volume': 345.0, 'density': 1.0260869565217392},
            datetime.date(2022, 5, 6): {'type': 'plastic', 'weight': 45.0, 'volume': 345.0, 'density': 0.13043478260869565},
            datetime.date(2024, 2, 6): {'type': 'glass', 'weight': 354.0, 'volume': 345.0, 'density': 1.0260869565217392},
            datetime.date(2025, 11, 6): {'type': 'paper', 'weight': 45.0, 'volume': 345.0, 'density': 0.13043478260869565},
            datetime.date(2123, 2, 6): {'type': 'glass', 'weight': 354.0, 'volume': 345.0, 'density': 1.0260869565217392},
            datetime.date(2012, 5, 23): {'type': 'paper', 'weight': 45.0, 'volume': 345.0, 'density': 0.13043478260869565},
            datetime.date(2013, 2, 6): {'type': 'glass', 'weight': 354.0, 'volume': 345.0, 'density': 1.0260869565217392},
            datetime.date(2001, 5, 6): {'type': 'plastic', 'weight': 455.0, 'volume': 3445.0, 'density': 0.13043478260869565},
        }
        super().__init__(last_name, first_name, birth_year, email,
                         mobile, adress, profile_picture)

    # Takes weight, volume, trash type and date to create an entry in track_record attribute
    def add_garbage_data(self):
        date = self.get_valid_date()
        collected_weight = float(input('Weight collected: '))
        collected_volume = float(input("Volume: "))
        trash_density = collected_weight / collected_volume
        trash_type = self.get_valid_trash_type()

        record = {
            "type": trash_type,
            'weight': collected_weight,
            'volume': collected_volume,
            'density': trash_density
        }

        self.track_records[date] = (record)
        print(self.track_records)

    # Asks use to provide date in console. Will continue until valid date provided
    def get_valid_date(self):
        date_format = '%Y-%m-%d'
        while True:
            date = input('Date (YYYY-MM-DD). Press "Enter" to set as today: ')
            if date == '':
                return datetime.datetime.now().date()
            try:
                date_valid = datetime.datetime.strptime(date, date_format)
                return date_valid.date()
            except ValueError:
                print("Incorrect data format, should be YYYY-MM-DD")

    # Check if provided trash type is one of Glass, Plastic or Paper
    def get_valid_trash_type(self):
        trash_types = ['glass', 'paper', 'plastic']
        while True:
            trash_type = input('Trash type: ')
            if trash_type not in trash_types:
                print("Trash type can only be glass, paper or plastic")
                continue
            else:
                return trash_type

    # Print valunteer track_record date for each day
    def get_garbage_data(self):
        volonteer_data = self.track_records
        for key, value in volonteer_data.items():
            print(key, end=": ")
            print(value['type'], end=" ")
            print(value['weight'], end=" ")
            print(value['volume'], end=" ")
            print(value['density'], end=" ")
            print("\n")

    def get_stats(self, date_from, date_to, type, metric):
        # print("Provide date from: ")
        # date1 = self.get_valid_date()
        # print("Provide date to: ")
        # date2 = self.get_valid_date()
        # type = self.get_valid_trash_type()
        date_format = '%Y-%m-%d'
        date_from_obj = datetime.datetime.strptime(
            date_from, date_format).date()
        date_to_obj = datetime.datetime.strptime(date_to, date_format).date()
        volunteer_data = self.track_records
        filtered_data = {
            k: v[metric] for (k, v) in volunteer_data.items() if k >= date_from_obj if k <= date_to_obj if v['type'] == type}
        print(sum(filtered_data.values()))

    def get_all_time_stats(self):
        volunteer_data = self.track_records
        glass_sum = {'volume': 0, 'weight': 0}
        paper_sum = {'volume': 0, 'weight': 0}
        plastic_sum = {'volume': 0, 'weight': 0}
        totals = {'volume': 0, 'weight': 0}
        for key, value in volunteer_data.items():
            if value['type'] == 'glass':
                glass_sum['volume'] += value['volume']
                glass_sum['weight'] += value['weight']
            if value['type'] == 'paper':
                paper_sum['volume'] += value['volume']
                paper_sum['weight'] += value['weight']
            if value['type'] == 'plastic':
                plastic_sum['volume'] += value['volume']
                plastic_sum['weight'] += value['weight']
            totals['volume'] += value['volume']
            totals['weight'] += value['weight']
        print(
            f'Glass   \t Weight: {glass_sum["weight"]}   \t| Volume: {glass_sum["volume"]}   \t| Density: {round((glass_sum["weight"] / glass_sum["volume"]), 2)} \n'
            f'Paper   \t Weight: {paper_sum["weight"]}   \t| Volume: {paper_sum["volume"]}   \t| Density: {round((paper_sum["weight"] / paper_sum["volume"]), 2)} \n'
            f'Plastic \t Weight: {plastic_sum["weight"]}  \t| Volume: {plastic_sum["volume"]}  \t| Density: {round((plastic_sum["weight"] / plastic_sum["volume"]), 2)} \n'
            f'All     \t Weight: {totals["weight"]}      \t| Volume: {totals["volume"]}      \t| Density: {round((totals["weight"] / totals["volume"]), 2)} \n')


"""
Administrator class. Inherits from Person class. Has __is_admin attribute set to True by default
"""


class Administrator(Person):
    def __init__(self, last_name, birth_year=None, email=None, mobile=None, adress=None, profile_picture=None, first_name=None):
        self.__is_admin = True
        super().__init__(last_name, birth_year, email,
                         mobile, adress, profile_picture, first_name)


vlad = Volunteer.user_create()
vlad.get_stats('2020-03-11', '2030-09-12', 'glass', 'weight')
vlad.print_data()
vlad.get_all_time_stats()
