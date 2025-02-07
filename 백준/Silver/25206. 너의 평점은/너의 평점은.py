# input : 수업명 학점 등급 
# output : 평점
# sum(학점*등급)/len(수업명)

# bin = [list(row.split()) for row in """ObjectOrientedProgramming1 3.0 A+
# IntroductiontoComputerEngineering 3.0 A+
# ObjectOrientedProgramming2 3.0 A0
# CreativeComputerEngineeringDesign 3.0 A+
# AssemblyLanguage 3.0 A+
# InternetProgramming 3.0 B0
# ApplicationProgramminginJava 3.0 A0
# SystemProgramming 3.0 B0
# OperatingSystem 3.0 B0
# WirelessCommunicationsandNetworking 3.0 C+
# LogicCircuits 3.0 B0
# DataStructure 4.0 A+
# MicroprocessorApplication 3.0 B+
# EmbeddedSoftware 3.0 C0
# ComputerSecurity 3.0 D+
# Database 3.0 C+
# Algorithm 3.0 B0
# CapstoneDesigninCSE 3.0 B+
# CompilerDesign 3.0 D0
# ProblemSolving 4.0 P""".split("\n")]
bin = []

for _ in range(20):
  bin.append(input().split())

grade_dict = {"A+" : 4.5, "A0" : 4.0, "B+" : 3.5, "B0" : 3.0, "C+" : 2.5, "C0" : 2.0,
              "D+" : 1.5, "D0" : 1.0, "F" : 0.0}

result = 0 
cnt = 0 

for name, num, grade in bin:
  #print(num, grade)
  if grade == "P":
    continue

  result += float(num) * grade_dict[grade]
  cnt += float(num)

# print(result)
# print(cnt)
print(f"{result/cnt:.6f}")

