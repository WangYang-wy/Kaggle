class PATH:
    base_path = '~/.kaggle/competitions/'

    def __init__(self, competitions_name):
        self.competitions_name = competitions_name

    def train_path(self, file_name):
        return self.base_path + file_name

    def test_path(self, file_name):
        return self.base_path + file_name

    def submit_path(self, file_name):
        return self.base_path + file_name


if __name__ == '__main__':
    pass
