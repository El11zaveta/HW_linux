import subprocess
import zlib

FOLDER_IN = "/home/user/tst"
FOLDER_OUT = "/home/user/out"
FOLDER_EXT = "/home/user/folder1"



def checkout(cmd, text):
    res = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='uft-8')
    if not res.returncode and text in res.stdout:
        return True
    else:
        return False
    

def test_step1():
    res1 = checkout(f"cd {FOLDER_IN}; 7z e arz2.7z -o{FOLDER_OUT}/arx2", "Everything is Ok")
    res2 = checkout(f"ls {FOLDER_OUT}", "arx2.7z")
    assert res1 and res2, "test1 FAIL"


def test_step2():
    res1 = checkout(f"cd {FOLDER_OUT}; 7z e arz2.7z -o{FOLDER_EXT} -y", "Everything is Ok")
    res2 = checkout(f"ls {FOLDER_EXT}", "arx2.7z")
    assert res1 and res2, "test2 FAIL"


def test_step3():
    assert checkout(f"cd {FOLDER_OUT}; 7z t arx2.7z", "Everything is Ok"), "test3 FAIL"


def test_step4():
    assert checkout(f"cd {FOLDER_OUT}; 7z d arx2.7z", "Everything is Ok"), "test4 FAIL"


def test_step5():
    assert checkout(f"cd {FOLDER_OUT}; 7z u arx2.7z", "Everything is Ok"), "test5 FAIL"


#Дополнить проект тестами, проверяющими команды вывода списка файлов (l) и разархивирования с путями (x).
def test_step6():
    res1 = checkout(f"cd {FOLDER_IN}; 7z a {FOLDER_EXT}/arx2", "Everything is Ok")
    res2 = checkout(f"cd {FOLDER_OUT}; 7z l arx2.7z", "text.txt")
    assert res1 and res2, "test6 FAIL"


def test_step7():
    res1 = checkout(f"cd {FOLDER_OUT}; 7z x arx2.7z -o{FOLDER_EXT} -y", "Everything is Ok")
    res2 = checkout(f"ls {FOLDER_EXT}", "tst2")
    res3 = checkout(f"ls {FOLDER_EXT}/tst2", "text.txt")
    assert res1 and res2 and res3, "test7 FAIL"    


#Доработать проект, добавив тест команды расчёта хеша (h). Проверить, что хеш совпадает с рассчитанным командой crc32.
def crc32(cmd):
        with open(cmd, 'rb') as g:
            hash = 0
            while True:
                s = g.read(65536)
                if not s:
                    break
                hash = zlib.crc32(s, hash)
        return "%08X" % (hash % 0xFFFFFFFF)
    

def test_stap8():
    res1 = crc32(f"{FOLDER_OUT}/arx2.7z".lower())
    assert checkout(f"crc32 {FOLDER_OUT}/arx2.7z", res1), "test8 FAIL"