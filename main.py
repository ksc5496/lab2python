# Author: Krish Choudhary ksc5496@psu.edu
# Collaborator: Kieran Murdocca kkm5574@psu.edu 
# Collaborator: Reuben Lee wzl128@psu.edu
# Collaborator: Augustus Perseghin agp5191@psu.edu
# Section: 4
# Breakout: 18

def getletterGrade(percentage):
  if (percentage >= 93.0):
    return "A"
  elif (percentage >= 90.0):
    return "A-"
  elif (percentage >= 87.0):
    return "B+"
  elif (percentage >= 83.0):
    return "B"
  elif (percentage >= 80.0):
    return "B-"
  elif (percentage >= 77.0):
    return "C+"
  elif (percentage >= 70.0):
    return "C"
  elif (percentage >= 60.0):
    return "D"
  else: 
    return "F" 
    

def run():
  percentage = float(input("Enter your CMPSC 131 grade: "))
  print(f"Your letter grade for CMPSC 131 is {getletterGrade(percentage)}.")

if __name__ == "__main__":
  run()

