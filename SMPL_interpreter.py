class evaluate:
    def __init__(self):
        self.variablesDict = {}

    def run(self, code):
        lines = code
        for line in lines:
            if line == "":
                continue
            self.EvaluateLine(line)
    
    def EvaluateLine(self, line):
        command = line.split(" ")[0]

        for char in range(len(line)):

            if line[char] == "(":
                open = char

            elif line[char] == ")":
                close = char
                break

        try:
            data = line[open:close]

        except:
            print(f"error no brackets on line {line}")

        if command == "say_my_name":
            
            self.say_my_name(data)
        
        elif command == "calc":
            self.calcFunc(data)
        
        elif command == "arr":
            self.variableAssignments(data)

    def variableAssignments(self, data):

        line = line.split(" ")
        variable = line[1]
        dataType = line[2]
        operation = line[5]

        if "calc" in operation:
            value = self.calcFunc(line[5])

        self.variablesDict[variable] = [dataType,value]


    def say_my_name(self, data):
            string = False
            for char in range(len(line)):
                if "\"" in line:
                    string = True 

                if line[char] == "(":
                    open = char
                elif line[char] == ")":
                    close = char
                    break

            if string:
                output = line[open+2:close-1]
            
            else:
                output = line[open+1:close]
                #check for variable
                print(f"Output = {output}")

                try:
                    output = self.variablesDict[output]

                except:
                    output = self.calcFunc(output)

            print(output)

    def calcFunc(self, line):
        try:
            for char in range(len(line)):

                if line[char] == "(":
                    open = char

                elif line[char] == ")":
                    close = char
                    break

            equation = line[open+1:close]

            equation = list(equation)

        except:
            equation = line
            
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
