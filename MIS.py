class employee:
    def __init__(self):
        self.name = input("enter name of employee :")
        self.emp_id = input("enter employee id :")
        self.contact = input("enter contact number of employee :")
        self.address = input("enter address of employee :")
        self.department = input("enter department : ")
        
    def show_detail(self):
        print("employee ID : ", self.emp_id)
        print("name : ", self.name)
        print("contact", self.contact)
        print("address : ", self.address)
        
    def dwrite(self):
        f = open("employee.txt", "a")
        data = self.emp_id + ","+self.name+"," +self.contact+ "," +self.address+"," +self.department+"\n"
        f.write(data)
        print("data entered successfully")
class manager(employee):
                # employee().__init__()
    def dept_employee_details(self):
        f = open("employee.txt","r")
        data = f.read()
        data_row = data.split("\n")
        data_row.pop()
        valid_row=[]
        
        for i in data_row:
            x=i.split(",")
            if self.department == x[len(x)-1]:
                valid_row.append(i)

class owner(manager,employee):
    def show_all(self):
        f = open("employee.txt", "r")
        data = f.read()
        data_row = data.split("\n")
        data_row.pop()
        for i in data_row:
            x = i.split(",")
            print("-----------------------------")
            print("employe ID :", x[0])
            print("Name :", x[1])        
            print("contact:", x[2])
            print("address :", x[3])
            print("Department:", x[4])
    print("----------------")

s1 = employee()
s2 = manager()
s3 = owner()
s1.dwrite()
s2.dwrite()
s3.dwrite()

s1.show_detail()
s2.show_detail()
s2.dept_employee_details()
s3.show_detail()
s3.dept_employee_details()
s3.show_all()
