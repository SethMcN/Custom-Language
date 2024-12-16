class evaluate:
    def __init__(self):
        self.variablesDict = {}

    def run(self, code):
        lines = code
        for line in lines:
            if line == "":
                continue
            self.EvaluateLine(line)


    def getData(self, line):
        try:
            for i in range(len(line)):
                if line[i] == "(":
                    open = i

                elif line[i] == ")":
                    close = i

                    break
            return line[open+1:close]

        except:
            print(f"error no brackets on data {data}")      

    def Getinput(self, data):
        userData = input(data)
        return userData

    def EvaluateLine(self, line):
        command = line.split(" ")[0]
        if command == "BTW":
            return None 

        if command == "say_my_name":
            data = self.getData(line)
            self.say_my_name(data)
        
        elif command == "calc":
            data = self.getData(line)
            self.calcFunc(data)
        
        elif command == "arr":
            self.variableAssignments(line)

    def variableAssignments(self, data):

        dataSplit = data.split(" ")
        variable = dataSplit[1]
        dataType = dataSplit[2]
        operation = dataSplit[5]


        if "calc" in operation:
            value = self.calcFunc(dataSplit[5])

        elif operation == "skib_input":
            value = input(self.getData(data))

        else:
            value = dataSplit[5]

        self.variablesDict[variable] = [dataType,value]


    def say_my_name(self, data):

        for i in range(list(data).count("{")):

            for i in range(len(data)):
                if data[i] == "{":
                    variableOpen = i
                
                elif data[i] == "}":
                    variableClose = i
                    variableFound = True
                    break
        
        if variableFound:
            variable = self.variablesDict[data[variableOpen+1:variableClose]][1]
            output = f"{data[:variableOpen]} {variable} {data[variableClose+1:]}"
        

        print(output)

    def calcFunc(self, data):
        try:
            for char in range(len(data)):

                if data[char] == "(":
                    open = char

                elif data[char] == ")":
                    close = char
                    break

            equation = data[open+1:close]

            equation = list(equation)

        except:
            equation = data
            
        try:
            nums = []
            num = ""
            for i in range(len(equation)):
                if equation[i].isdigit():
                    num += (equation[i])
                else:
                    nums.append(num)
                    nums.append(equation[i])
                    num = ""
            
            nums.append(num)


            result = int(nums[0])
            for i in range(len(nums)):
                if nums[i] == "+":
                    result += int(nums[i+1])
                elif nums[i] == "-":
                    result -= int(nums[i+1])
                elif nums[i] == "*":
                    result *= int(nums[i+1])
                elif nums[i] == "/":
                    result /= int(nums[i+1])
                

            return result

        except:
            print("sumting wong in calc") 


    

if __name__ == "__main__":
    import sys
    file = "firstCode.smpl"
    with open(file, "r") as file:
        code = list(file.read().split("\n"))
        evaluator = evaluate()
        evaluator.run(code)
