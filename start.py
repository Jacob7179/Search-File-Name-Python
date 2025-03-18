import pkg_resources
import subprocess
import os
import sys

def main():
    os.system('cls')
    print("=============================================================================")
    print("\t\t\tSearch File")
    print("=============================================================================")
    print("0. Exit  \t\t\t\t[EXIT]")
    print("1. Search File Word  \t\t\t[Word]")
    print("2. Search File Excel  \t\t\t[Excel]")
    print("3. Search File PDF  \t\t\t[PDF]")
    try:
        choice = (input("\nEnter your choice here : "))

        current_dir = os.path.dirname(os.path.abspath(__file__))

        if choice == "0":
            sys.exit()

        elif choice == "1":
            print("Running Search_File_Word.py...")
            script_path = os.path.join(current_dir, "resource", "Search_File_Word.py")
            subprocess.run(["python", script_path])
        elif choice == "2":
            print("Running Search_File_Excel.py...")
            script_path = os.path.join(current_dir, "resource", "Search_File_Excel.py")
            subprocess.run(["python", script_path])
        elif choice == "3":
            print("Running Search_File_PDF.py...")
            script_path = os.path.join(current_dir, "resource", "Search_File_PDF.py")
            subprocess.run(["python", script_path])
        else:
            main()
    except KeyboardInterrupt:
        main()
    main ()
    
if __name__ == "__main__":
    main()