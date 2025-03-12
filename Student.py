class Student:
    def __init__(self,name):
        self.name=name
        
    def getName(self):
        print(self.name)

    def __init__(self, name, age, grades):
        # 初始化學生的姓名、年齡和成績
        self.name = name
        self.age = age
        self.grades = grades  # 假設成績是一個包含數字的列表

    def add_grade(self, grade):
        # 新增一個成績
        self.grades.append(grade)

    def get_average(self):
        # 計算並返回平均成績
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

    def display_info(self):
        # 顯示學生的基本資訊
        print(f"學生姓名: {self.name}")
        print(f"年齡: {self.age}")
        print(f"成績: {self.grades}")
        print(f"平均成績: {self.get_average():.2f}")

# 範例使用
student1 = Student("小明", 18, [90, 85, 88, 92])
student1.display_info()

student2 = Student("小華", 17, [78, 85, 80])
student2.add_grade(90)
student2.display_info()
