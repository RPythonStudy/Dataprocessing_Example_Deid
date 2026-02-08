# Chrome Browser에서 md 파일 보기 - Markdown Reader extension

- Markdown reader extension 설치
- chrome brower 주소창에.

```
chrome://extensions
```

- allow local file URL access

# Windows 에서 파이썬 설치  (Scoop)

### 1. Powershell 업그레이드, 정리.

- 설치

```powershell
winget install --id Microsoft.Powershell --source winget
```

- 실행  : `pwsh.exe`
- Powershell 7 의 위치  `C:\Program Files\PowerShell\7\pwsh.exe`
- 최신 버전 파워셀 설치 명령어

```powershell
iex "& { $(irm https://aka.ms/install-powershell.ps1) } -UseMSI"
```

- restrict 제거

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser  
```

### 2. Scoop 설치

- Powershell  일반 모드에서 실행해야 함.

```powershell
Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression
```

```Powershell
irm get.scoop.sh | iex
```

- Git 설치 :  Scoop 을 이용해서  설치

```powershell
scoop install main/git  
```

- bucket에  versions 폴더 추가

```shell
scoop bucket add versions
```

### 3. Scoop 을 이용해서 파이썬 설치

- Python 설치

```Powershell
scoop install versions/python39  
scoop install versions/python312
```

- Scoop 에 설치된 패키지 리스트 보기

```powershell
scoop list 
```

- Switch to specific python

```Powershell
scoop reset python312
```

### 4. Project folder 만들고 Virtual Environment  설정 , 실행.

- 현재 파이썬 버전 확인

```shell
python -V 
```

    -`V`  가 대문자

- 프로젝트 폴더로 이동

```shell
cd  Py_Project
```

    - cd : change directory

- 가상환경 설치

```shell
python -m venv .venv 
```

- 가상환경 활성화

```powershell
.\.venv\Scripts\Activate.ps1
```

- 파이썬 실행 파일이 어디있나?

```powershell
where.exe python 
```

```
C:\Users\bclee\Codes\PyLib\.venv\Scripts\python.exe  (가상환경 파이썬)
C:\Users\bclee\scoop\apps\python311\current\python.exe (Scoop 에서 현재 설정된 파이썬 )
C:\Users\bclee\AppData\Local\Microsoft\WindowsApps\python.exe (윈도우즈 패키지로 설치한 파이썬)
```

- 가상환경 끄기

```powershell
deactivate
```

# Mac 에서 파이썬 설치 (Pyenv)

# 1. brew 설치

- install git  (if needed)

```shell
apt update 
```

```shell
apt install git
```

- install curl (if needed)

```shell
apt install curl 
```

- brew 설치 with curl

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

- brew 를 path에 넣어주기

```
(echo; echo 'eval "$(/opt/homebrew/bin/brew shellenv)"') >> /Users/charlie/.zprofile
```

    - (User 이름이 charlie 인 경우)

# 2. pyenv 설치

```shell
brew install pyenv
```

# 3. pyenv 을 이용해서 파이썬 설치

- 현재 사용  가능한 파이썬 버전 보기 (3.9 버전)

```shell
pyenv install --list | grep " 3\.9\.." 
```

- 특정버전 설치

```shell
pyenv install 3.11
```

- 현재 설치된 버전 보기

```shell
pyenv versions 
```

- 사용할 버전 지정

```shell
pyenv global 3.11.9
```

### 4. Project folder 만들고 Virtual Environment  설정 , 실행.  (윈도우와 거의 동일, 단, activate 명령만 다름)

- 현재 파이썬 버전 확인

```shell
python -V 
```

    -`V`  가 대문자

- 프로젝트 폴더로 이동

```shell
cd  Py_Project
```

    - cd : change directory

- 가상환경 설치

```shell
python -m venv .venv 
```

- 가상환경 활성화 (윈도우와 다른 점)

```shell
source ./.venv/bin/activate
```

- 파이썬 실행 파일이 어디있나? (윈도우와 다른점)

```powershell
where python 
```

```
C:\Users\bclee\Codes\PyLib\.venv\Scripts\python.exe  (가상환경 파이썬)
C:\Users\bclee\scoop\apps\python311\current\python.exe (Scoop 에서 현재 설정된 파이썬 )
C:\Users\bclee\AppData\Local\Microsoft\WindowsApps\python.exe (윈도우즈 패키지로 설치한 파이썬)
```

- 가상환경 끄기

```powershell
deactivate
```
