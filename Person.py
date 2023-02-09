import datetime
import base64

"""
Abstract person class. Conatnis methods both Volunteer an Administrator should have.
"""
#first_name=None, birth_year=None, email=None, mobile=None, adress=None, profile_picture=None
class Person():
    def __init__(self, last_name, first_name=None, birth_year=None, email=None, mobile=None, adress=None, profile_picture=None):
        self.last_name = last_name
        self.first_name = first_name
        self.birth_year = birth_year
        self.email = email
        self.mobile = mobile
        self.adress = adress
        self.profile_picture = profile_picture
        self._created_at = datetime.datetime.now()

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if value == "":
            print("Provide last name")
        if not value.isalpha():
            raise ValueError("Provide letters only")
        self._last_name = value

    @property
    def first_name(self):
        return self._first_name

    # Check if provided name has alphabetical symbols only
    @first_name.setter
    def first_name(self, value):
        if value and not value.isalpha():
            raise ValueError("Provide letters only")
        self._first_name = value

    @property
    def birth_year(self):
        return self._birth_year

    # Check if provided birt year is > 0, otherwise return 2000
    @birth_year.setter
    def birth_year(self, value):
        if value and value != '':
            if int(value) > 0:
                self._birth_year = int(value)
            else:
                self._birth_year = 2000

    @property
    def email(self):
        return self._email

    # Check if email contains "@", appends "@gmail.com" if not
    @email.setter
    def email(self, value):
        if value and "@" in value:
            self._email = value
        else:
            self.email = value + "@gmail.com"

    @property
    def mobile(self):
        return self._mobile

    # Clears provided string from aplhabetical chars and returns numbers only
    @mobile.setter
    def mobile(self, value):
        if value:
            cleared_mobile = ''.join(ch for ch in value if ch.isdigit())
            self._mobile = cleared_mobile

    @property
    def profile_picture(self):
        return self._prifile_picture

    # Takes image from provided path, encodes it to base64 and saves it in attribute
    @profile_picture.setter
    def profile_picture(self, value):
        if value and value != '':
                self._prifile_picture = self.encode_picture(value)

    # # Method that gets user input for class attributes
    # @classmethod
    # def user_create(cls):
    #     return cls(
    #         input('Last name: '),
    #         input('Name: '),
    #         int(input('Birth year: ')),
    #         input('Email: '),
    #         input('Mobile: '),
    #         input('Address: '),
    #         input('Profile picture path: '),
    #     )

    # Prints persons date as Name + Surname + Email
    def get_full_name(self):
        print(self.first_name+self.last_name+self.email)

    # Sets a profile_pcture attribute to base64 encoded image from provided path
    def add_profile_photo(self, path):
        picture = self.encode_picture(path)
        pattern = '/9j/4'
        try:
            picture.startswith(pattern)
            self._profile_picture = picture
        except Exception:
            raise Exception('File is not a .jpg image')

    # Create foto.jpg in directory from profile_picture attribute
    def write_photo_in_directory(self):
        with open('foto.jpg', 'wb') as f:
            f.write(base64.decodebytes(self.profile_picture.encode('utf-8')))

    def encode_picture(self, path):
        with open(path, "rb") as img_file:
                base64_enocded = base64.b64encode(
                    img_file.read()).decode('utf-8')
                return base64_enocded


    def print_data(self):
        print('Adress: ' + self.adress)
        print('First name: ' + self.first_name)
        print('Last name: ' + self.last_name)
        print('Birth year: ' + str(self.birth_year))
        #print(self.profile_picture)
        print('Moble: ' + self.mobile)
        print('Created: ' + str(self._created_at))
        print('\n')

"""
Volunteer class. Inherits from Person class. Has volunterr specific methods and __is_admin attribute set to False
"""
class Volunteer(Person):
    def __init__(self, last_name, first_name=None, birth_year=None, email=None, mobile=None, adress=None, profile_picture=None):
        self._is_admin = False
        # Some sample data for testing
        self.track_records = {
            datetime.date(2023, 2, 6): {'type': 'glass', 'weight': 354.0, 'volume': 345.0, 'density': 1.02},
            datetime.date(2025, 5, 6): {'type': 'paper', 'weight': 45.0, 'volume': 345.0, 'density': 0.13},
            datetime.date(2013, 2, 6): {'type': 'glass', 'weight': 354.0, 'volume': 345.0, 'density': 1.02},
            datetime.date(2022, 5, 6): {'type': 'plastic', 'weight': 45.0, 'volume': 345.0, 'density': 0.13},
            datetime.date(2024, 2, 6): {'type': 'glass', 'weight': 354.0, 'volume': 345.0, 'density': 1.02},
            datetime.date(2025, 11, 6): {'type': 'paper', 'weight': 45.0, 'volume': 345.0, 'density': 0.13},
            datetime.date(2123, 2, 6): {'type': 'glass', 'weight': 354.0, 'volume': 345.0, 'density': 1.02},
            datetime.date(2012, 5, 23): {'type': 'paper', 'weight': 45.0, 'volume': 345.0, 'density': 0.13},
            datetime.date(2013, 2, 6): {'type': 'glass', 'weight': 354.0, 'volume': 345.0, 'density': 1.02},
            datetime.date(2001, 5, 6): {'type': 'plastic', 'weight': 455.0, 'volume': 3445.0, 'density': 0.13},
        }
        super().__init__(last_name, first_name, birth_year, email, mobile, adress, profile_picture)

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
            'density': round(trash_density, 2)
        }

        # Here I'm assuming you can only have on entry per day without the ability to edit entry
        # Thus I'm using dict of dicts to store entries with dates as akeys for record dict
        self.track_records[date] = (record)
        print('\n')

    # Asks use to provide date in console. Will continue until valid date provided
    def get_valid_date(self):
        date_format = '%Y-%m-%d'
        while True:
            date = input('Date (YYYY-MM-DD). Press "Enter" to set as today: ')
            if date == '':
                return datetime.datetime.now().date()

            try:
                date_valid = datetime.datetime.strptime(date, date_format)
            except ValueError:
                print('Incorrect data format, should be YYYY-MM-DD')

            if date_valid.date() not in self.track_records:
                return date_valid.date()
            else:
                print('Entry already exists')

    # Check if provided trash type is one of Glass, Plastic or Paper
    def get_valid_trash_type(self):
        trash_types = ['glass', 'paper', 'plastic']
        while True:
            trash_type = input('Trash type: ')
            if trash_type not in trash_types:
                print('Trash type can only be glass, paper or plasti')
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
        print('\n')

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
    def __init__(self, last_name, **kwargs):
        self._is_admin = True
        super().__init__(last_name, **kwargs)



"""Volunteer specific methods example"""

# Initialize volunterr instance. First argument last_nmae is required. All others are optional.
vol_1 = Volunteer("Sem", first_name='Vlad', birth_year=1856, email='vsd', mobile='523dde434234', adress='tur 8 - 24', profile_picture='Smiley_Face.jpg')

# Print person data (for testing)
#vol_1.print_data()

# Add entry to person track records
vol_1.add_garbage_data()

# Outputs volunteers data to console. 1 entry per line.
vol_1.get_garbage_data()

# Outputs all valunteer data to console. First for each trash type. Than totals
vol_1.get_all_time_stats()

# Takes two dates, trash type and metric as an arguments. Returns sum data fitered by them
vol_1.get_stats('2000-03-11', '2100-09-12', 'glass', 'volume')

"""Any user methods example"""

adm_1 = Administrator("Deen", first_name='Vlad', email='vsd', mobile='523dde434234', profile_picture='Smiley_Face.jpg')
print('Is admin for Administrator: ' + str(adm_1._is_admin))

# Outputs full name to console as firstName+lastName+email
adm_1.get_full_name()

# Sets objects profile_picture attribute to base64 encoded picture from path
adm_1.add_profile_photo('Smiley_Face.jpg')

# Convers base64 store in profile_picture directory to foto.jpg 
adm_1.write_photo_in_directory()