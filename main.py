"""stress tester"""

import time
import os
import hashlib
import faker

def test():
  """one test, hashing a string"""
  start = time.time()
  # fake data
  fake = faker.Faker()
  data = fake.text()
  # hashing
  hash = hashlib.sha256(data.encode()).hexdigest()
  end = time.time()
  print(f"{data}: {hash} ({end - start}s)")
  elapsed = end - start
  return elapsed

def stress(stime: int = 60):
  score = 0
  elapsed_list = []
  # for X seconds, do as many tests as possible
  s = time.time()
  while time.time() - s < stime:
    elapsed = test()
    elapsed_list.append(elapsed)
    score += 1

  # average
  avg = sum(elapsed_list) / len(elapsed_list)

  return score, avg, elapsed_list

def main():
  """main function"""
  # stress test
  score, avg, list = stress()
  # check for term variable
  if "TERM" in os.environ:
    os.system('cls' if os.name == 'nt' else 'clear')
  else:
    print("\n" * 100)  # backup plan
  # print results
  print(f"score: {score}, avg: {avg}")

if __name__ == "__main__":
  main()
