class JobTitle:
    def __init__(self, name, weekly_norm):
        self.name = name
        self.weekly_norm = weekly_norm

class Employee:
    def __init__(self, name, job_obj, work_done):
        self.name = name
        self.job = job_obj
        self.work_done = work_done

class FactoryManager:
    def __init__(self):
        self.employees = []
        self.job_titles = []

    def create_job(self, name, norm):
        new_job = JobTitle(name, int(norm))
        self.job_titles.append(new_job)

    def find_job(self, job_name):
        return next((i for i in self.job_titles if i.name == job_name), None)

    def hire_employee(self, name, job_name, work_done):
        job = self.find_job(job_name)
        if job:
            new_emp = Employee(name, job, int(work_done))
            self.employees.append(new_emp)
            return True
        return False

    def fire_employee_by_name(self, name):
        for i in self.employees:
            if i.name == name:
                self.employees.remove(i)
                return True
        return False

    def get_all_employees_info(self):
        return [f"{i.name} — {i.job.name} — Выполнено: {i.work_done}" for i in self.employees]

    def get_underperformers(self):
        result = []
        for i in self.employees:
            if i.work_done < i.job.weekly_norm:
                result.append(f"{i.name} — {i.job.name} ({i.work_done} из {i.job.weekly_norm})")
        return result

def main():
    manager = FactoryManager()
    
    manager.create_job("Сварщик", 40)
    manager.create_job("Сборщик", 35)
    manager.create_job("Упаковщик", 50)

    manager.hire_employee("Иван", "Сварщик", 35)
    manager.hire_employee("Петр", "Упаковщик", 60)
    manager.hire_employee("Алексей", "Сборщик", 20)

    while True:
        print("\n1 — Добавить должность")
        print("2 — Добавить сотрудника")
        print("3 — Уволить сотрудника")
        print("4 — Показать сотрудников")
        print("5 — Сформировать список на увольнение")
        print("0 — Выход")
        
        choice = input("Выбор: ")

        if choice == '1':
            name = input("Название: ")
            norm = input("Норма: ")
            manager.create_job(name, norm)
        elif choice == '2':
            name = input("Имя: ")
            job_name = input("Должность: ")
            work = input("Объем: ")
            manager.hire_employee(name, job_name, work)
        elif choice == '3':
            name = input("Имя: ")
            manager.fire_employee_by_name(name)
        elif choice == '4':
            info = manager.get_all_employees_info()
            print("\n".join(info) if info else "Список пуст")
        elif choice == '5':
            under = manager.get_underperformers()
            print("\nСотрудники на увольнение:")
            print("\n".join(under) if under else "Таких нет")
        elif choice == '0':
            break

if __name__ == "__main__":
    main()