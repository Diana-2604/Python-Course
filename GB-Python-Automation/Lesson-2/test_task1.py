import subprocess
def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False
    
def test_step1():
    assert checkout("cd /home/user/tst; 7z a ../out/arx2", "Everything is Ok"), "test1 FAIL"

def test_step2():
    assert checkout("cd /home/user/out; 7z e arx2.7z -o /home/user/folder1 -y", "Everything is Ok"), "test2 FAIL"

def test_step3():
    assert checkout("cd /home/user/out; 7z t arx2.7z", "Everything is Ok"), "test3 FAIL"

def test_step4():
    assert checkout(f"cd {folderout}; 7z d arx2.7z", "Everything is Ok"), "test4 FAIL"

def test_step5():
    assert checkout(f"cd {folderin}; 7z u {folderout}/arx2.7z", "Everything is Ok"), "test5 FAIL"

def test_step6():
    res1 = checkout(f"cd {folderin}; 7z a {folderout}/arx2", "Everything is Ok")
    res2 = checkout(f"ls {folderout}", "arx2.7z")
    assert res1 and res2, "test6 FAIL"

def test_step7():
    res1 = checkout(f"cd {folderout}; 7z e arx2.7z -o{folderext} -y", "Everything is Ok"), "test7 FAIL"
    res2 = checkout(f"ls {folderext}", "test1.txt")
    res3 = checkout(f"ls {folderext}", "test2.txt")
    assert res1 and res2 and res3, "test7 FAIL"

def test_step8():
    assert checkout(f"cd {folderout}; 7z l arx2.7z", "2 files"), "test8 FAIL"

def test_step9():
    assert checkout(f"cd {folderin}; 7z l {folderout}/arh1", "test1.txt" "test2.txt"), "test9 FAIL"

def test_step10():
    assert checkout(f"cd {folderin}; 7z x {folderout}/arh1", "Everything is Ok"), "test10 FAIL"
                    