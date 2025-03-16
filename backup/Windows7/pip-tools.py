import pkg_resources
import subprocess
import os
import sys

def check_package(package_name):
    try:
        package_version = pkg_resources.get_distribution(package_name).version
        return f"{package_name} is installed (Version: {package_version})"
    except pkg_resources.DistributionNotFound:
        return f"{package_name} is not installed"

def pip_install(error_message):
    os.system('cls')
    choice = 0
    print(error_message)
    print("=============================================================================")
    print("\t\t\tPIP Tools for Windows 7")
    print("=============================================================================")
    print("0. Exit  \t\t\t\t[EXIT]")
    print("1. Basic Package  \t\t\t[INSTALL]")
    print("2. Basic Package  \t\t\t[UNINSTALL]")
    print("3. Upgrade PIP  \t\t\t[UPGRADE]")
    print("4. Check Tools & Library Version \t[CHECK]")
    print("=============================================================================")
    print("Basic Package: [openpyxl] [PyPDF2] [python-docx]")
    print("=============================================================================")

    try:
        choice = (input("\nEnter your choice here : "))

        if choice == "0":
            sys.exit()

        elif choice == "1":
            try:
                os.system('cls')
                print("=============================================================================")
                print("Installing [openpyxl] [PyPDF2] [python-docx]")
                print("=============================================================================")
                subprocess.check_call(['pip', 'install', 'openpyxl'])
                subprocess.check_call(['pip', 'install', 'PyPDF2'])
                subprocess.check_call(['pip', 'install', 'python-docx'])

                print("=============================================================================")
                print("openpyxl installed successfully.")
                print("PyPDF2 installed successfully.")
                print("python-docx installed successfully.")

            except subprocess.CalledProcessError as e:
                print(f"Error when install : {e}")
            
            print("=============================================================================")
            back = input("Press [Enter] key to go back.")
            while True:
                if back == "":
                    os.system('cls')
                    main()
                else:
                    os.system('cls')
                    main()

        elif choice == "2":
            try:
                os.system('cls')
                print("=============================================================================")
                print("Uninstalling [openpyxl] [PyPDF2] [python-docx]")
                print("=============================================================================")
                subprocess.check_call(['pip', 'uninstall', '-y', 'openpyxl'])
                subprocess.check_call(['pip', 'uninstall', '-y', 'PyPDF2'])
                subprocess.check_call(['pip', 'uninstall', '-y', 'python-docx'])

                print("=============================================================================")
                print("openpyxl uninstall successfully.")
                print("PyPDF2 uninstall successfully.")
                print("python-docx uninstall successfully.")

            except subprocess.CalledProcessError:
                print(f"Error when uninstall : {e}")
            except KeyboardInterrupt:
                os.system('cls')
                print("You interrupted the program with CTRL + C.")
                main()

            print("=============================================================================")
            back = input("Press [Enter] key to go back.")
            while True:
                try:
                    if back == "":
                        os.system('cls')
                        main()
                    else:
                        os.system('cls')
                        main()
                except KeyboardInterrupt:
                    print("You interrupted the program with CTRL + C.")


        elif (choice == "3"):
            try:
                os.system('cls')
                print("=============================================================================")
                print("Upgrade PIP")
                print("=============================================================================")
                subprocess.check_call(['pip', 'install', '--upgrade', 'pip'])

                print("=============================================================================")
                print("Upgrade PIP successfully.")

            except subprocess.CalledProcessError:
                print(f"Error when uninstall : {e}")
            except KeyboardInterrupt:
                os.system('cls')
                print("You interrupted the program with CTRL + C.")
                main()

            print("=============================================================================")
            back = input("Press [Enter] key to go back.")
            while True:
                try:
                    if back == "":
                        os.system('cls')
                        main()
                    else:
                        os.system('cls')
                        main()
                except KeyboardInterrupt:
                    print("You interrupted the program with CTRL + C.")

        elif (choice == "4"):
            try:
                os.system('cls')
                print("=============================================================================")
                print("Check Tools & Library Version")
                print("=============================================================================")
                
                packages = [
                    "pip",
                    "openpyxl",
                    "PyPDF2",
                    "python-docx"
                ]
                
                for package in packages:
                    status = check_package(package)
                    print(status)
            
            except subprocess.CalledProcessError:
                print(f"Error when uninstall : {e}")
            except KeyboardInterrupt:
                os.system('cls')
                print("You interrupted the program with CTRL + C.")
                main()

            print("=============================================================================")
            back = input("Press [Enter] key to go back.")
            while True:
                try:
                    if back == "":
                        os.system('cls')
                        main()
                    else:
                        os.system('cls')
                        main()
                except KeyboardInterrupt:
                    print("You interrupted the program with CTRL + C.")


        else:
            error_message = "Invalid choice. Please enter the correct choice."
            pip_install(error_message)

    except KeyboardInterrupt:
        os.system('cls')
        error_message = "You interrupted the program with CTRL + C."
        pip_install(error_message)

        print("=============================================================================")
        back = input("Press [Enter] key to go back.")
        while True:
            try:
                if back == "":
                    os.system('cls')
                    main()
                else:
                    os.system('cls')
                    main()
            except KeyboardInterrupt:
                print("You interrupted the program with CTRL + C.")

def main():
    error_message = ""
    pip_install(error_message)
                

if __name__ == "__main__":
    main()