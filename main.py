import os

import pytest


if __name__ == '__main__':
    pytest.main()
    '''
    os.system('allure generate temp -o reports --clean')
    # 打开报告
    os.system('allure open reports -p 0')
    '''