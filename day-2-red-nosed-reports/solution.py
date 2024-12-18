def check_conditions(previous_difference, difference):
  difference_conditions = abs(difference) >= 1 and abs(difference) <= 3
  
  if not previous_difference: return difference_conditions
  
  descending = previous_difference > 0 and difference > 0
  ascending = previous_difference < 0 and difference < 0
  
  return (descending or ascending) and difference_conditions

def report_without(report, index):
  return [number for i, number in enumerate(report) if i != index]

def is_safe(report, alternative_report = False):
  previous_difference = None
  
  for i in range(1, len(report)):
    difference = report[i-1] - report[i]
    if check_conditions(previous_difference, difference):
      previous_difference = difference
    else:
      if alternative_report:
        return False
      
      for i in range(0, len(report)):
        alternative_report = report_without(report, i)
        if is_safe(alternative_report, True):
          return True
      
      return False
  
  return True

def read_input(file_name = 'input.txt'):
  reports = []
  
  with open(file_name, 'r') as file:
    for line in file:
      numbers = [int(number) for number in line.strip().split(" ")]
      reports.append(numbers)
      
  return reports

reports = read_input()
safe_count = sum([1 for report in reports if is_safe(report)])
print(safe_count)
