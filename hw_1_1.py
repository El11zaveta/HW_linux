import subprocess

def subprocess_file(directiry: str, find_name: str) -> bool:
    res = subprocess.run('cat /etc/os-release', shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    out = res.stdout
    if res.returncode == 0:
        list = out.split('\n')
        if find_name in list:
            return True
        return False
    return False

if __name__ == '__main__':
    print(subprocess_file('cat /etc/os-release', 'PRETTY_NAME='Ubuntu 22.04.1 LTS'))