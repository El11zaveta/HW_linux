import subprocess
import string

def subprocess_file(directiry: str, find_name: str, splite_mode=False) -> bool:
    res = subprocess.run('cat /etc/os-release', shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    out = res.stdout

    if res.returncode == 0:
        if split_mode:
            res_words = ''.join(char if char.isalnum() or char.isspace() else ' ' for char in out)
            return find_name in res_words.split()
        else: return False

if __name__ == '__main__':
    print(subprocess_file('cat /etc/os-release', 'PRETTY_NAME='Ubuntu 22.04.1 LTS'))