from database.db import c
from .status import Status


class Employee(object):
    def __init__(self, name, surname, age, status=Status.ACTIVE.value, id=None):
        self.status = status
        self.id = id
        self.name = name
        self.surname = surname
        self.age = age

    @classmethod
    def get(cls, employee_id):
        result = c.execute(
            "SELECT * FROM employee WHERE id = ? AND status=?",
            (employee_id, Status.ACTIVE.value),
        )
        values = result.fetchone()
        if values is None:
            return None
        employee = Employee(
            values["name"],
            values["surname"],
            values["age"],
            values["id"],
            values["status"],
        )
        return employee

    def __repr__(self):
        return f"<Employee: id={self.id}, name={self.name}, surname={self.surname}, age={self.age},status={self.status}>"

    def update(self):
        c.execute(
            "UPDATE employee SET name = ?, surname = ?, age = ? WHERE id = ? AND status=?",
            (self.name, self.surname, self.age, self.id, Status.ACTIVE.value),
        )

    def create(self):
        c.execute(
            "INSERT INTO employee (name, surname, age, status) VALUES (?, ?, ?, ?)",
            (self.name, self.surname, self.age, self.status),
        )

    def save(self):
        if self.id is not None:
            self.update()
        else:
            self.create()
        return self

    def delete(self):
        c.execute(
            "UPDATE employee SET status = ? WHERE id = ? AND status = ?",
            (Status.DELETED.value, self.id, Status.ACTIVE.value),
        )
    # Simple delete method which uses sql delete function
    # def delete(self):
    #     c.execute("DELETE FROM employee WHERE id = ?", (self.id,))
    #     del self

    def __lt__(self, other):
        if isinstance(other, Employee):
            return self.age < other.age
        return False

    def __eq__(self, other):
        if isinstance(other, Employee):
            return self.age == other.age
        return False

    def __ge__(self, other):
        if isinstance(other, Employee):
            return not self.__lt__(other)
        return False

    @classmethod
    def get_list(cls, **kwargs):
        query = "SELECT id, name, surname, age, status FROM employee WHERE status = ?"
        params = [Status.ACTIVE.value]
        conditions = []
        for key, value in kwargs.items():
            if key in ["name", "surname", "age"]:
                conditions.append(f"{key} = ?")
                params.append(value)
        if conditions:
            query += " AND " + " AND ".join(conditions)
        result = c.execute(query, params)
        employees = []
        for row in result.fetchall():
            employee = cls(row[1], row[2], row[3], row[4], row[0])
            employees.append(employee)
        return employees
