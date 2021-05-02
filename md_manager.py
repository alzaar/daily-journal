import datetime
import os
from subprocess import call

class MDManager:
    def __init__(self):
        self.file_name = f'{datetime.datetime.now().date()}'
        self.file_path = os.path.join(
            os.path.dirname(__file__),
            'journal',
            self.file_name
        ) + '.md'

    def get_created_file(self):
        try: 
            file = open(self.file_path, 'x')
        except Exception as e:
            print('File already exists!')
            return None
        print('File successfully created!')
        return file

    def write_to_file(self, file):
        if file:
            file.write(f'# {self.file_name}\n')
            headers = [
                'What did I achieve today ?',
                'What lessons did I learn ?',
                'How could I have made today better ?',
                'How did I feel today ?',
            ]
            points = 3
            for header in headers:
                file.write(f'#### {header}\n')
                for i in range(points):
                    file.write('-\n')

            print('Successfully wrote to file!')
        else:
            print('No file present!')

    def complete(self, file):
        file.close()
        call(['code', self.file_path])
        print('File successfully closed!')
