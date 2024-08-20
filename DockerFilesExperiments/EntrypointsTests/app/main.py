import datetime
import time


def main(data):
    with open("test_file", 'w') as file:
        file.write(data)


if __name__ == '__main__':
    # main('Some_Test_Data3')
    main(str(datetime.datetime.now()))
    time.sleep(60)
