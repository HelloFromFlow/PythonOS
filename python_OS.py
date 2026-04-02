import time


kernel_stability = True
cmd_caused = False
files = []
backup = []
packages_installed = []
omnimizer_used = False
optimized = 0
pythonshell_dev_tools = False
activated = False


print('...')
time.sleep(2)

print('checking file safety')
for a in range(21):
    print(f'{a * 5}% files checked')
    time.sleep(0.1)
print('file safety [OK]')
time.sleep(2)

print('starting /boot_menu...')
time.sleep(2)
init = int(input('Welcome to the boot menu: 1 = boot Python_OS, 2 = shutdown    '))

if init == 1:

    print('Now booting up to Python_OS!')
    time.sleep(1)
    for d in range(100):
        print(f'booted up {d}% of the OS...')
        time.sleep(0.001)
    time.sleep(1)
    print(f'booted up {100}% of the OS')
    time.sleep(1)
    print('___       _____       ___                  ___    _____')
    print('|__| \  /   |  |   | |   |  |\   |        |   |  |     ')
    print('|     \/    |  |---| |   |  | \  |        |   |  |_____')
    print('|     /     |  |   | |   |  |  \ |        |   |        |')
    print('|    /      |  |   | |___|  |   \| ______ |___|   _____|')
    print('Hello again! What are we doing today?')

    while True:
        if kernel_stability == True:
            choice = int(input('1 = access data, 2 = create file, 3 = delete file, 4 = check_integrity, 5 = clear data, 6 = inspect file, 7 = load backup files, 8 = command prompt, 9 = general info, 10 = shutdown   '))
            if choice == 1:
                print(f'All your created data: {files}')
            elif choice == 2:
                int_or_str = int(input('Do you want your file to be: 1 = int, 2 = str:    '))
                if int_or_str == 1:
                    file_name = int(input('What do you want to name your file? (int):   '))
                    files.append(file_name)
                    backup.append(file_name)
                    (f'successfully created {file_name}')
                elif int_or_str == 2:
                    file_name = input('What do you want to name your file? (str):   ')
                    files.append(file_name)
                    backup.append(file_name)
                    print(f'successfully created {file_name}')
                else:
                    print('Wrong file type! Returning...')

            elif choice == 3:
                int_or_str2 = int(input('Would you like to delete a file that`s 1 = int, 2 = str    '))
                if int_or_str2 == 1:
                    del_name = int(input('Please enter the exact name of the file you would like to remove (int):   '))
                    if files.count(del_name) >= 1:
                        files.remove(del_name)
                        backup.remove(del_name)
                        print(f'successfully removed {del_name}')
                    elif files.count(del_name) < 1:
                        kernel_stability = False
                        print('Wrongly-written file deletion order! Kernel panic will be initiated shortly...')
                if int_or_str2 == 2:
                    del_name = input('Please enter the exact name of the file you would like to remove (str):   ')
                    if files.count(del_name) >= 1:
                        files.remove(del_name)
                        backup.remove(del_name)
                        print(f'successfully removed {del_name}')
                    elif files.count(del_name) < 1:
                        kernel_stability = False
                        print('Wrongly-written file deletion order! Kernel panic will be initiated shortly...')
                else:
                    print('Wrong file type! Returning...')
            elif choice == 4:
                print('preparing scape_check (a.k.a. system integrity)...')
                for e in range(11):
                    print(f'system/firewall integrity check {e * 10}%')
                    if omnimizer_used == False:
                        time.sleep(0.1)
                    elif omnimizer_used == True:
                        time.sleep(0.000001)
                        optimized += 1
                time.sleep(1)
                print('system/firewall intact')
                time.sleep(2)
                for f in range(101):
                    print(f'system/OS integrity check {f}%')
                    if omnimizer_used == False:
                        time.sleep(0.01)
                    elif omnimizer_used == True:
                        time.sleep(0.000001)
                        optimized += 1
                time.sleep(1)
                print('Python_OS intact')
                time.sleep(2)
                for g in range(101):
                    print(f'system/kernel integrity check {g}%')
                    if omnimizer_used == False:
                        time.sleep(0.01)
                    elif omnimizer_used == True:
                        time.sleep(0.000001)
                        optimized += 1
                time.sleep(1)
                print('system/kernel stable')
                time.sleep(1)
            elif choice == 5:
                choice2 = int(input('are you sure you want to clear the list "directory"? 1 = Y  2 = N    '))
                if choice2 == 1:
                    print('clearing the list "directory"...')
                    time.sleep(1)
                    files.clear()
                    print('done!')
                elif choice2 == 2:
                    print('mission cancelled')
            elif choice == 6:
                inspection_t = int(input('what type is the file you want to inspect: 1 = int, 2 = str    '))
                if inspection_t == 1:
                    insp_n = int(input('Enter the name of the file:   '))
                    if files.count(insp_n) >= 1:
                        print(f'.int file {insp_n}, index in the list "directory" - {files.index(insp_n)}.')
                    elif files.count(insp_n) == 0:
                        print('Wrongly-written file inspection order! Kernel panic will be initiated shortly!')
                        kernel_stability = False
                if inspection_t == 2:
                    insp_n = input('Enter the name of the file:   ')
                    if files.count(insp_n) >= 1:
                        print(f'.str file {insp_n}, index in the list "directory" - {files.index(insp_n)}.')
                    elif files.count(insp_n) == 0:
                        print('Wrongly-written file inspection order! Kernel panic will be initiated shortly!')
                        kernel_stability = False
                else:
                    print('Wrong file type! Returning...')
            elif choice == 7:
                choice3 = int(input('Are you sure you want to load all list "backup" files into list "directory"? 1 = Y, 2 = N   '))
                if choice3 == 1:
                    files.clear()
                    list.extend(files, backup)
                    time.sleep(1)
                    print('done!')
            elif choice == 8:
                print('welcome to the Pythonshell command prompt (type in "ls commands" for info)')
                time.sleep(1)
                while True:
                    command = input('users/system/sys>   ')
                    if command == 'ls directory':
                        print(f'list "directory": {files}')
                    elif command == 'rm directory':
                        print('clearing "directory"')
                        time.sleep(0.5)
                        files.clear()
                        print('[####] 100% [OK]')
                        print('done')
                    elif command == 'ls backup':
                        print(f'list "backup": {backup}')
                    elif command == 'rm backup':
                        print('clearing "backup"')
                        time.sleep(0.5)
                        backup.clear()
                        print('[####] 100% [OK]')
                        print('done')
                    elif command == 'exit':
                        break
                    elif command == 'crt int':
                        file_n = int(input(''))
                        files.append(file_n)
                        backup.append(file_n)
                        print(f'int file {file_n} put into "directory", "backup"')
                    elif command == 'crt str':
                        file_n = input('')
                        files.append(file_n)
                        backup.append(file_n)
                        print(f'str file {file_n} put into "directory", "backup"')
                    elif command == 'pc f rbt':
                        print('pythonshell: pc forced reboot')
                        time.sleep(1)
                        print('[----] 0%')
                        time.sleep(1)
                        print('[#---] 25%')
                        time.sleep(1)
                        print('[##--] 50%')
                        time.sleep(2)
                        print('[###-] 75%')
                        time.sleep(3)
                        print('[####] 100% [OK]')
                        time.sleep(4)
                        break
                    elif command == 'ld backup':
                        print('loadng the list "backup" into the list "directory"')
                        files.clear()
                        list.extend(files, backup)
                    elif command == 'pc f krn_p':
                        print('pythonshell: pc forced kernel panic')
                        time.sleep(2)
                        kernel_stability = False
                        cmd_caused = True
                        break
                    elif command == 'rm':
                        print('clearing all lists...')
                        time.sleep(1)
                        files.clear()
                        print('[##--] 50%')
                        time.sleep(1)
                        backup.clear()
                        print('[####] 100%')
                        print('done')
                    elif command == 'ls commands':
                        print('commands list')
                        time.sleep(0.5)
                        print('ls directory - prints out the list "directory"')
                        print('ls backup - prints out the list "backup"')
                        print('ls verified_pi_packages - prints out all the verified software avaible for installation through the PyInstall manager')
                        print('ls software - prints out all the installed PyInstall manager software')
                        print('exit - exit pythonshell')
                        print('rm directory - clears the list "directory"')
                        print('rm backup - clears the list "backup"')
                        print('rm sw - deletes all the PyInstall software')
                        print('rm - clears all the lists except software')
                        print('crt int - creates an int file and puts it in both lists')
                        print('crt str - creates a str file and puts it in both lists')
                        print('pc f rbt - force the pc to reboot without powering it off')
                        print('pc f krn_p - force the pc to initialize kernel panic')
                        print('ld backup - loads the list "backup" into the list "directory"')
                        print('pi inst - install a package through the PyInstall manager')
                        print('run - runs a PyInstall software')
                        print('cease - stops a PyInstall software')
                        print('pi del - delete a package through the PyInstall manager')
                        print('act status - prints out your activation status')
                        print('advanced_ (license-only) commands:')
                        print('    advanced_ run NCT - run NCT (network configuration test) to make sure your network is doing alright')
                        print('    advanced_ run IP_DP - runs IP_DN (ip_decypher_negation) to make sure your IP stays private and undecryptable')
                    elif command == 'pi inst':
                        choice4 = input('enter verified package name (you can view them all by typing ls verified_pi_packages):   ')
                        if choice4 == 'Omnimizer' and packages_installed.count('Omnimizer') == 0:
                            print('installing "Omnimzer"')
                            time.sleep(2)
                            print('[##########] 100%')
                            time.sleep(0.75)
                            packages_installed.append('Omnimizer')
                            print('complete')
                        elif choice4 == 'Omnimizer' and packages_installed.count('Omnimizer') >= 1:
                            print('omnimizer already installed, returning...')
                        elif choice4 == 'InternetAccesser' and packages_installed.count('InternetAccesser') == 0:
                            print('installing "InternetAccesser"')
                            time.sleep(3)
                            print('[##########] 100%')
                            time.sleep(1)
                            packages_installed.append('InternetAccesser')
                            print('complete')
                        elif choice4 == 'InternetAccesser' and packages_installed.count('InternetAccesser') >= 1:
                            print('internetaccesser already installed, returning...')
                        else:
                            print('unknown/unexisting/unverified software')
                    elif command == 'run':
                        choice5 = input('enter installed software name you want to run:   ')
                        if choice5 == 'Omnimizer' and omnimizer_used == False and packages_installed.count('Omnimizer') >= 1:
                            print('Welcome to the Omnimizer software!')
                            time.sleep(1)
                            print('This is made for optimizing the processes your system runs so it can get faster!')
                            time.sleep(1)
                            print('However, once the omnimizer script finishes, it can never be ran again!')
                            time.sleep(3)
                            print('Accelerating the system...')
                            time.sleep(1)
                            print('Done!')
                            omnimizer_used = True
                        elif choice5 == 'Omnimizer' and omnimizer_used == True and packages_installed.count('Omnimizer') >= 1:
                            print('omnimizer already ran, returning...')
                        elif choice5 == 'Omnimizer' and packages_installed.count('Omnimizer') == 0:
                            print('not-installed software')
                        elif choice5 == 'InternetAccesser' and packages_installed.count('InternetAccesser') >= 1:
                            print('Welcome to the InternetAccesser web browser!')
                            time.sleep(1)
                            while True:
                                site = input('Please enter the exact link to the site you want to enter (exit to leave):   ')
                                if site == 'github.com/PythonOS_official/pythonshell_dev_tools':
                                    print('Do you want to install "pythonshell_dev_tools" package on your pc?')
                                    agreement = input('Y/N   ')
                                    if agreement == 'Y':
                                        time.sleep(1)
                                        print('[####] 100%')
                                        pythonshell_dev_tools = True
                                        print('installation successful')
                                    elif agreement == 'N':
                                        print('returning...')
                                elif site == 'exit':
                                    print('Closing InternetAccesser...')
                                    time.sleep(0.5)
                                    break
                                else:
                                    print('Unknown site')
                        else:
                            print('unknown/unexisting/uninstalled software')
                    elif command == 'cease':
                        choice6 = input('enter installed software name you want to stop:   ')
                        if choice6 == 'Omnimizer' and omnimizer_used == False and packages_installed.count('Omnimizer') >= 1:
                            print('Omnimizer not running')
                        elif choice6 == 'Omnimizer' and omnimizer_used == True and packages_installed.count('Omnimizer') >= 1:
                            print('Stopping "Omnimizer"...')
                            time.sleep(1)
                            print('[##########] 100%')
                            omnimizer_used = False
                            time.sleep(0.2)
                            print(f'Omnimizer disabled (managed to optimize {optimized} processes)')
                            optimized = 0
                        elif choice6 == 'Omnimizer' and packages_installed.count('Omnimizer') == 0:
                            print('not-installed software')
                    elif command == 'ls verified_pi_packages':
                        print('all the verified PyInstaller packages:')
                        time.sleep(1)
                        print('Omnimizer - Optimizing made simple')
                        print('InternetAccesser - Basic browser, currently supporting just a few sites.')
                    elif command == 'ls software':
                        print(f'All installed software: {packages_installed}')
                    elif command == 'rm sw':
                        print('deleting all the installed software...')
                        time.sleep(2)
                        print('[##########] 100%')
                        time.sleep(0.75)
                        packages_installed.clear()
                        omnimizer_used = False
                        print('done!')
                    elif command == 'pi del':
                        choice7 = input('enter installed software name you want to delete:   ')
                        if choice7 == 'Omnimizer' and packages_installed.count('Omnimizer') >= 1:
                            print('deleting "Omnimizer"...')
                            time.sleep(1)
                            omnimizer_used = False
                            packages_installed.remove('Omnimizer')
                            print('[##########] 100%')
                            time.sleep(0.75)
                            print('done!')
                        elif choice7 == 'Omnimizer' and packages_installed.count('Omnimizer') == 0:
                            print('not-installed software')
                        elif choice7 == 'InternetAccesser' and packages_installed.count('InternetAccesser') >= 1:
                            print('deleting InternetAcceser...')
                            time.sleep(1)
                            packages_installed.remove('InternetAcceser')
                            print('[##########] 100%')
                            time.sleep(0.75)
                            print('done!')
                        elif choice7 == 'InternetAccesser' and packages_installed.count('InternetAccesser') == 0:
                            print('not-installed software')
                        else:
                            print('unknown/unexisting/unverified software')
                    elif pythonshell_dev_tools == True and command == 'PyShell_developer_tools':
                        choice8 = input('what dev tool to use:   ')
                        if choice8 == 'auto_activation_script':
                            activated = True
                            print('ran auto_activation_script successfully')
                        elif choice8 == 'ls all':
                            print(f'list "directory": {files}, list "backup": {backup}, list "software": {packages_installed}, activation status: {activated}')
                    elif command == 'act status':
                        print(activated)
                    elif command == 'advanced_ run NCT' and activated == True:
                        print('loading NCT...')
                        time.sleep(2)
                        print('[###-] 75%')
                        time.sleep(1)
                        print('[####] 100%')
                        time.sleep(1)
                        print('activating nct:')
                        for a in range(21):
                            print(f'completed {a * 5}%')
                            time.sleep(0.3)
                    elif command == 'advanced_ run IP_DP' and activated == True:
                        print('running IP_DP...')
                        time.sleep(1)
                        print('done!')
                    else:
                        print('invalid command')
            elif choice == 9:
                print('PythonOS general tips & knowledge:')
                time.sleep(2)
                print('1. Access Data')
                print('    prints out the list "directory"')
                print('2. Create File')
                print('    create file of 2 different types - int or str, which are automatically put into the list "directory"')
                print('3. Delete File')
                print('    delete files from the list "directory" - please use exact names.')
                print('4. check_integrity')
                print('    list out all the system security & os parameters stability to check it')
                print('5. Clear Data')
                print('    clear the list "directory"')
                print('6. Inspect File')
                print('    enter an exact name of a file from the list "directory" - please use exact names - to list out it`s properties.')
                print('7. Load Backup Files')
                print('    clears the list "directory" and extends it with the list "backup". The list "backup" is affected by the files creations and deletions, but not by the clear action and kernel panic.')
                print('8. Command Prompt')
                print('    command prompt "pythonshell" - refer to the command "ls commands" in the prompt itself to list all the commands')
                print('9. General Info')
                print('    lists out all the info you`re reading right now')
                print('10. Shutdown')
                print('    powers off the OS and puts your files to hybernation')
                print('ADDITIONAL INFO:')
                print(f'    System Activation Status - can be checked in the command prompt and seen here. Currently - {activated}. Activating the OS will let you run advanced commands in the prompt.')
            elif choice == 10:
                print('Goodbye, have fun out there!')
                time.sleep(1)
                for c in range(11):
                    print(f'{c * 10}% of personal & OS files put to hybernation...')
                    time.sleep(0.1)
                time.sleep(2)
                print('all files hybernated [OK]')
                time.sleep(2)
                break
            if omnimizer_used == False:
                time.sleep(1)
            elif omnimizer_used == True:
                time.sleep(0.1)
                optimized += 1
        elif kernel_stability == False:
            if cmd_caused == True:
                print('kernel panic initialized through the pythonshell command prompt')
                cmd_caused = False
            elif cmd_caused == False:
                print('critical error: invalid file management')
            files.clear()
            time.sleep(1)
            print('Stabilizing your PC data, please stand by...')
            time.sleep(1)
            for b in range(101):
                print(f'{b}% recovery completed...')
                if omnimizer_used == False:
                    time.sleep(0.01)
                elif omnimizer_used == True:
                    time.sleep(0.000001)
                    optimized += 1
            time.sleep(2)
            print('Your data has been stored in the list "backup" load to restore.')
            kernel_stability = True
            time.sleep(1)
