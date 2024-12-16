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

        data = data.split(" ")
        variable = data[1]
        dataType = data[2]
        operation = data[5]

        if "calc" in operation:
            value = self.calcFunc(data[5])
        
        else:
            value = data[5]

        self.variablesDict[variable] = [dataType,value]


    def say_my_name(self, data):
            string = False
            if "\"" in data:
                string = True

            if string:
                output = str(data)
            
            else:
                output = str(data)
                #check for variable

                try:
                    output = self.variablesDict[output][1]
                    
                except:
                    output = self.calcFunc(output)

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
