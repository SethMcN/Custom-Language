class evaluate:
    def run(self, code):
        lines = code
        for line in lines:
            if line == "":
                continue
            self.EvaluateLine(line)
    
    def EvaluateLine(self, line):
        command = line.split(" ")[0]

        if command == "say_my_name":
            
            self.say_my_name(line)
        
        elif command == "calc":
            self.calcFunc(line)
        
        elif command == "arr":
            self.variableAssignments(line)

    def variableAssignments(self, line):
        pass

    def say_my_name(self, line):
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

            print(output)

    def calcFunc(self, line):

        for char in range(len(line)):

            if line[char] == "(":
                open = char
            elif line[char] == ")":
                close = char
                break

        equation = line[open+1:close]

        equation = list(equation)

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
