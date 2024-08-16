import json
import os

from data_pipeline.health import HealthKitData


def main():
    root_path = '../data/raw/'
    save_path = '../data/processed/'
    input_file = root_path + 'export.xml'

    if not os.path.exists(root_path):
        os.makedirs(root_path)

    if not os.path.exists(save_path):
        os.makedirs(save_path)

    hkd = HealthKitData(input_file)
    hkd.save(save_path)
    print('Done')

if __name__ == '__main__':
    main()