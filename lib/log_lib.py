import os
import logging
import time

"""
自定义日志工具类:单例模式-----希望每次执行生成一个日志文件 如何实现
1、os.path.split(path)方法:作用：将文件路径和文件名分隔开，并以元组返回,可根据下标取文件名
"""


def create_log(log_name):
    date_time = time.strftime('%Y%m%d', time.localtime(time.time()))

    # 1. 创建日志对象
    log_path = '../log/{}_{}.txt'.format(date_time, log_name)
    logger = logging.getLogger(os.path.split(log_path)[1])

    # 2. 设置日志级别    级别依次增高：DEBUG\INFO\WARNING\ERROR\CRITICAL
    logger.setLevel(logging.DEBUG)  # 只记录所设置级别及以上级别的信息
    # 3. 打开指定的文件log_path并将其用作日志记录流
    fh = logging.FileHandler(log_path, encoding='utf-8')

    # 4. 自定义日志输出格式
    formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s\t%(message)s')
    fh.setFormatter(formatter)
    # 5. 往logger中添加输出方式
    logger.addHandler(fh)
    return logger


class LogLib:
    _logger = None

    def __new__(cls):
        if not cls._logger:
            cls._logger = create_log('auto_test_log')

        return super().__new__(cls)  # 调用父类object的new方法

    def write_to_log_debug(self, content):
        self._logger.debug('\t' + content)

    def write_to_log_info(self, content):
        self._logger.info('\t' + content)

    def write_to_log_warning(self, content):
        self._logger.warning('\t' + content)

    def write_to_log_error(self, content):
        self._logger.error('\t' + content)

    def write_to_log_critical(self, content):
        self._logger.critical(content)





if __name__ == '__main__':
    LogLib().write_to_log_debug('debug-----------')
