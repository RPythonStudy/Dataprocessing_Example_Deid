- 파이썬 키워드 정리하기 
  
  ```
  파이썬 초급자가 @reorder_prompts.py 코드를  이해하는데 필요한 기본 지식에 대한 키워드만 
  나열해서 keywords.md 에 한글, 영어 로 표롤 정리해주세요
  ```

- 제목 기준 역순으로 정렬하기

```
prompts.md 파일의 제목을 기준으로 역순으로 정렬해주세요
```

```
"-" 로 시작하는 행을 제목으로 보고 ,  제목과 그 아래 텍스트는 한 덩어리입니다.  
이 덩어리들을  prompts.md 에 배치되어 있는 역순으로 재배치해서 
prompts-1.md에 저장해주세요
```

- 결손치 확인

```
@deid_clinicaldata.xlsx 의 데이터 중에서 결손치가 있는지 확인해주세요. 결손치가 있는 경우, 결손치가 있는 컬럼과 결손치의 수를 json 포맷과 yaml 포맷으로 결과를 저장해주세요
```

- 중복데이터 확인
  
  ```
  @deid_clinicaldata.xlsx 안의 sheet 중에서 중복된 환자 데이터가 있는가?  있다면,  어느 시트에 어느 환자가 몇개 중복인지, json 포맷과 yaml 포맷으로 결과를 저장해주세요
  ```

- 등재번호 채우기

```
  @deid_clinicaldata.xlsx 의 B 컬럼을 @deid_mapping.xlsx 를 참고해서  채워 주세요
```

- Sheet List 구하기

```
@deid_clinicaldata파일의 sheet 들의 리스트를 sheet_list.txt 로 저장해주세요
```

- 원본 보관

```
  @deid_전체환자_등록번호+등재번호.xlsx 는 deid_mapping.xlsx 로 복사해주고, @deid_KQIPS eCRF (수신-전산팀) 20250508 수정_수술전후검사결과제공_20250529.xlsx 는 deid_clinicaldata.xlsx 로 복사해주세요
```

- 가상환경을 생성하거나 ,  기존 가상환경을 이용해주세요.

