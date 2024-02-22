import logging
from loggings_setting import logging_config
from module_1 import main

import logging.config

# Настраиваем базовую конфигурацию логирования
logging.config.dictConfig(logging_config)

# Исполняем функцию `main` из модуля `module_1.py`
main()
