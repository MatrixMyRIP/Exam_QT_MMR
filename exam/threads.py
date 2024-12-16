from PySide6 import QtCore
import cpuinfo
import psutil
import win32com.client
import time


class SystemInfo(QtCore.QThread):
    systemInfoReceived = QtCore.Signal(list)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.delay = None

    def run(self) -> None:
        if self.delay is None:
            self.delay = 1
        while True:
            cpu_name = cpuinfo.get_cpu_info()
            cpu_cores = psutil.cpu_count()
            cpu_value = psutil.cpu_percent()
            ram_total = psutil.virtual_memory().total / (1024.0 ** 3)
            ram_used = psutil.virtual_memory().used / (1024.0 ** 3)
            processes = [item.name() for item in psutil.process_iter()]
            services = [service.name() for service in psutil.win_service_iter()]
            scheduler = self.scheduler_list()
            self.systemInfoReceived.emit([cpu_name['brand_raw'], cpu_cores, cpu_value, round(ram_total, 2),
                                          round(ram_used, 2), processes, services, scheduler])
            time.sleep(self.delay)

    def setDelay(self, delay):
        self.delay = delay

    def scheduler_list(self):
        scheduler = win32com.client.Dispatch('Schedule.Service')
        scheduler.Connect()
        tasks = scheduler.GetFolder('\\').GetTasks(0)
        tasks_list = ""
        for task in tasks:
            tsk = task.Name
            pr = str(task.Path)
            state = task.State
            if state == 1:
                state = "Выполняется"
            if state == 2:
                state = "Готова"
            if state == 3:
                state = "Приостановлена"
            last_run = task.LastRunTime
            next_run = task.NextRunTime
            enb = task.Enabled
            if enb:
                enb = "Включена"
            if not enb:
                enb = "Выключена"
            tasks_list += (f"Название задачи:{tsk}\nМестоположение задачи:{pr}\nСостояние задачи:{state}\n"
                          f"Последнее время выполнения:{last_run}\nСледующее время выполнения:{next_run}\n"
                          f"Статус задачи:{enb}\n---\n")
        return tasks_list