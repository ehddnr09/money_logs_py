좋아. 이 프로젝트 README는 “멋진 포장”보다 **내가 뭘 만들었고, 뭘 배웠고, 어떻게 실행하는지**가 보이면 충분해.

구성은 이렇게 추천해.

````md
# Moneylogs

개인 지출을 터미널에서 기록하고 조회하는 Python CLI 프로젝트입니다.

## 만든 목적

Python 기초 문법을 실제 프로젝트에 적용하기 위해 만들었습니다.  
단순 문법 연습이 아니라 파일 저장, 명령어 처리, 예외 처리, Docker 실행까지 경험하는 것을 목표로 했습니다.

## 주요 기능

- 지출 추가
- 전체 지출 목록 조회
- 월별 지출 조회
- 카테고리별 지출 조회
- 월별 지출 통계
- id 기반 지출 삭제
- CSV 내보내기
- JSON 저장 파일 검증 및 예외 처리

## 사용 기술

- Python 3.11
- argparse
- json
- csv
- jsonschema
- Docker
- Docker Compose

## 실행 방법

```bash
docker compose build
```
````

```bash
docker compose run --rm python add --date 2026-05-01 --category coffee --amount 8500 --memo coffee
```

```bash
docker compose run --rm python list
```

```bash
docker compose run --rm python stats --month 2026-05
```

```bash
docker compose run --rm python delete --id 0
```

```bash
docker compose run --rm python export --format csv
```

## 데이터 저장 형식

거래 목록은 `data/transactions.json`에 저장됩니다.

```json
[
  {
    "id": 0,
    "date": "2026-05-01",
    "category": "coffee",
    "amount": 8500,
    "memo": "coffee"
  }
]
```

## 예외 처리

다음 상황을 처리하도록 구현했습니다.

- 저장 파일이 없는 경우
- JSON 파일이 비어 있는 경우
- JSON 문법이 깨진 경우
- 저장 데이터가 기대한 형식과 다른 경우
- 잘못된 카테고리
- 삭제하려는 id가 없는 경우
- CSV 외 export format 요청

## 배운 점

- `json.dump()`와 `json.dumps()`의 차이
- JSON 파일을 읽고 쓸 때 데이터 형태를 고정하는 것의 중요성
- `id=0`이 조건문에서 false처럼 동작한다는 점
- `jsonschema.validate()`는 검증 성공 시 데이터를 반환하지 않는다는 점
- 검증 실패한 데이터가 `None`으로 흐르면 이후 로직이 깨질 수 있다는 점
- Docker Compose로 CLI 앱을 실행하는 방법

## 다음 목표

- 객체지향 구조로 리팩터링
- 테스트 코드 추가
- 예산 설정 및 확인 기능 추가

실제 데이터 파일은 `data/transactions.json`에 저장됩니다.  
개인 데이터 보호를 위해 이 파일은 Git에 포함하지 않습니다.

처음 실행 전 샘플 파일을 참고해 `data/transactions.json`을 만들 수 있습니다.
