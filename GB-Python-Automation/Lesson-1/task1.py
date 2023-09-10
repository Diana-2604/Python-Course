# Условие:
# Написать функцию на Python, которой передаются в качестве параметров команда и текст. 
# Функция должна возвращать True, если команда успешно выполнена и 
# текст найден в её выводе и False в противном случае. 
# Передаваться должна только одна строка, разбиение вывода использовать не нужно.

import subprocess

def check_command_output(command, text):
    try:
        # Run the command and capture the output
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        
        # Check if the text is present in the output
        if text in output:
            return True
        else:
            return False
    except subprocess.CalledProcessError:
        return False
    
