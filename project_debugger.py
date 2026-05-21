import logging
import sys
from datetime import datetime

class ProjectDebugger:
    def __init__(self, is_debug: bool = False):
        self.is_debug = is_debug
        self.console_logger = logging.getLogger("Debugger")
        
        if not self.console_logger.handlers:
            handler = logging.StreamHandler(sys.stdout)
            formatter = logging.Formatter("[DEBUG] %(asctime)s | %(message)s", datefmt="%H:%M:%S")
            handler.setFormatter(formatter)
            self.console_logger.addHandler(handler)
            self.console_logger.setLevel(logging.INFO)

    def log_step(self, module_name: str, stage: str, data: dict):
        if self.is_debug:
            data_str = ", ".join([f"{k}: {v}" for k, v in data.items()])
            message = f"Модуль: {module_name:15} | Этап: {stage:12} | Данные -> [{data_str}]"
            self.console_logger.info(message)

DEBUG_MODE = False
debugger = ProjectDebugger(is_debug=DEBUG_MODE)