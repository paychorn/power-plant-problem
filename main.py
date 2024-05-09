from ortools.sat.python import cp_model
import sys

def power_plant_placement(n, e):
  sl = [1 for _ in range(n)]
  m = cp_model.CpModel()
  cs = [m.NewBoolVar(f'C_{i}') for i in range(n)]
  m.Minimize(sum(cs))
  for i in range(n):
    a = e[i]
    m.Add(sum(cs[i] + cs[n] for n in a) >= 1)
  s = cp_model.CpSolver()
  st = s.Solve(m)
  if st == cp_model.OPTIMAL:
    sl = [int(s.Value(c)) for c in cs]
    return sl
  else:
    print("No optimal solution found.")
    return sl

def parse_input_file(input_file):
  with open(input_file, 'r') as file:
    n = int(file.readline().strip())
    e = int(file.readline().strip())
    es = [[] for _ in range(n)]
    for _ in range(e):
      p = file.readline().split()
      if len(p) == 2:
        es[int(p[1])].append(int(p[0]))
        es[int(p[0])].append(int(p[1]))
  return n, es

def generate_output_file(solution, output_file):
  with open(output_file, 'w') as file:
    file.write("".join(map(str, solution)) + '\n')

def main():
  input_file = sys.argv[1]
  output_file = sys.argv[2]
  n, es = parse_input_file(input_file)
  sl = power_plant_placement(n, es)
  generate_output_file(sl, output_file)
  
if __name__ == "__main__":
  main()
