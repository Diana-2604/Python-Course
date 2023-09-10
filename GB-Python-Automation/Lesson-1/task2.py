# Доработать функцию из предыдущего задания таким образом, чтобы у неё появился 
# дополнительный режим работы, в котором вывод разбивается на слова с 
# удалением всех знаков пунктуации (их можно взять из списка string.punctuation модуля string). 
# В этом режиме должно проверяться наличие слова в выводе.

import subprocess
import string

def check_command_output(command, text, mode='line'):
    try:
        # Run the command and capture the output
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        
        # Remove punctuation marks from the output
        if mode == 'word':
            output = output.translate(str.maketrans('', '', string.punctuation))
            output = output.split()
        
        # Check if the text or word is present in the output
        if text in output:
            return True
        else:
            return False
    except subprocess.CalledProcessError:
        return False