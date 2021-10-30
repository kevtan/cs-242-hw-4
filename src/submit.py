# Submission script

# DO NOT EDIT THIS FILE

import tarfile, re, os

solution_filename = "solution.tar.gz"
t = tarfile.open(solution_filename, "w:gz")
error = False


def try_add(f, default_len=0):
    try:
        s = os.stat(f)
        if default_len != 0 and s.st_size == default_len:
            print(f"Warning: did you complete {f}?")
        if f == "README.txt":
            for l in open("README.txt").readlines():
                if re.match("^id:\\s*<?\d{8,9}>?\\s*$", l):
                    break
            else:
                print("Warning: did you put your id in README.txt?")
        t.add(f)
    except FileNotFoundError:
        print(f"Error: missing {f}")
        error = True


try_add("translate.py", 106)
try_add("problem1.pi", 376)
try_add("problem2.pi", 440)
try_add("problem3.pi", 1120)
try_add("problem4.pi", 1705)
try_add("problem5.pi", 1723)
try_add("README.txt")
t.close()

if not error:
    print(f"Wrote '{solution_filename}'. Upload this file to Canvas.")
