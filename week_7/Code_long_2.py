import my_functions as func

class YesNoBooleanValueConverter:
    def convert(self,val):
        if val == True:
            return "Yes"
        else:
            return "No"

    def convert_back(self,val):
        val = str(val).upper()
        if val == "Y" or val == "YES":
            return True
        else:
            return False

class Student:

    first_name=""
    last_name=""
    is_graduated=False

student_a=Student()
student_a.first_name="Sivanand"
student_a.last_name="Sista"
student_a.is_graduated=False

vc=YesNoBooleanValueConverter()
grad_status=vc.convert(student_a.is_graduated)
grad_status1=vc.convert_back("Y")
print(student_a.first_name,student_a.last_name,"Is graduted:",vc.convert(grad_status1))