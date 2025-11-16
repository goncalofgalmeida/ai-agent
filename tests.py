from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

def run_tests():
    test1_output = get_file_content("calculator", "main.py")
    print("Result for calculator/main.py directory:")
    if test1_output.startswith("Error:"):
        print(f"    {test1_output}")
    else:
        for line in test1_output.splitlines():
            print(f" {line}")
    print()

    test2_output = get_file_content("calculator", "pkg/calculator.py")
    print("Result for 'calculator/pkg/calculator.py' directory:")
    if test2_output.startswith("Error:"):
        print(f"    {test2_output}")
    else:
        for line in test2_output.splitlines():
            print(f" {line}")
    print()

    test3_output = get_file_content("calculator", "/bin/cat")
    print("Result for 'calculator/bin/cat' directory:")
    if test3_output.startswith("Error:"):
        print(f"    {test3_output}")
    else:
        for line in test3_output.splitlines():
            print(f" {line}")
    print()

    test4_output = get_file_content("calculator", "pkg/does_not_exist.py")
    print("Result for 'calculator/pkg/does_not_exist.py' directory:")
    if test4_output.startswith("Error:"):
        print(f"    {test4_output}")
    else:
        for line in test4_output.splitlines():
            print(f" {line}")
    print()

if __name__ == "__main__":
    run_tests()
