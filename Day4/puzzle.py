import re

class Passport:
    def __init__(self, raw_text):
        self.properties = {}
        self.required_fields = 'byr iyr eyr hgt hcl ecl pid'.split()
        self.eye_colors = 'amb blu brn gry grn hzl oth'.split()
        self.hair_regex = re.compile(r'#([a-f]|[0-9]){6}')
        self.passport_regex = re.compile(r'^\d{9}$')
        self.update_props(raw_text)

    def update_props(self, raw_text):
        for rt in raw_text.split():
            split = rt.split(':')
            self.properties[split[0]] = split[1]

    def __getitem__(self, prop):
        return self.properties[prop]

    def has_valid_fields(self):
        all_filled_keys = self.properties.keys()
        return all([rf in all_filled_keys for rf in self.required_fields])

    def has_valid_data(self):
        return self.birth_is_valid() & self.issue_is_valid() & \
        self.expiration_is_valid() & self.height_is_valid() & \
        self.hair_is_valid() & self.eye_is_valid() & \
        self.passport_id_valid()

    def birth_is_valid(self):
        return 1920 <= int(self['byr']) <= 2002

    def issue_is_valid(self):
        return 2010 <= int(self['iyr']) <= 2020

    def expiration_is_valid(self):
        return 2020 <= int(self['eyr']) <= 2030

    def hair_is_valid(self):
        return self.hair_regex.search(self['hcl']) != None

    def eye_is_valid(self):
        return self['ecl'] in self.eye_colors

    def passport_id_valid(self):
        return self.passport_regex.search(self['pid']) != None

    def height_is_valid(self):
        if self['hgt'].endswith('cm'):
            return 150 <= int(self['hgt'].replace('cm', '')) <= 193
        elif self['hgt'].endswith('in'):
            return 59 <= int(self['hgt'].replace('in', '')) <= 76
        else:
            return False


def parse_passports(input_file):
    with open(input_file, 'r') as f:
        input = f.read()

    return [Passport(p) for p in input.split('\n\n')]


def main1(input_file):
    passports = parse_passports(input_file)
    return sum([ppt.has_valid_fields() for ppt in passports])


def main2(input_file):
    passports = parse_passports(input_file)
    passports = [ppt for ppt in passports if ppt.has_valid_fields()]
    return sum([ppt.has_valid_data() for ppt in passports])


if __name__ == '__main__':
    input_file = './input.txt'

    print(main1(input_file))
    print(main2(input_file))
