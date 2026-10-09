# 《Le Comptoir de Marthe》 1부 "Mise en place (봄)" 제작 사양 (모든 집필자 공통)

원본 기획: `/root/.claude/uploads/f563b996-930d-50d6-9abd-62722ee653a1/c6f8fa2e-Le_Comptoir_de_Marthe____.xlsx`
(필요하면 `python3 -I -c "import openpyxl..."` 로 직접 읽어 확인. 이 문서가 우선.)

## 0. 산출물
화마다 파일 1개: `/home/user/Paris/comptoir/tools/part1/epNN_data.py` (NN = 01~15, 두 자리).
작성 후 반드시 `cd /home/user/Paris/comptoir/tools/part1 && python3 -I ../check_ep.py epNN_data` 를 실행해 `OK` 가 나올 때까지 고친다.
docx/pdf 빌드는 하지 말 것 (총괄이 한다). 다른 화 파일은 건드리지 말 것.

## 1. 기본 규격
- 대화 **정확히 120턴** (화자 발화 1회 = 1턴). 지문(stage direction)은 `(None, 프랑스어, 한글)` 로 넣고 턴에 포함되지 않음. 지문은 화당 최대 6개, 짧게.
- 화자 2~4명. 2인 대화 위주, 홀 장면은 3~4인. 화자 이름은 `Hélène`, `Lucien`, `Julien`, `Chloé`, `Karim`, `Mme Vasseur`, `M. Bastide` 처럼 짧게 (builder 색상 지정됨). 새 조연은 이름만 쓰면 기본색.
- **턴 번호 표기 금지.**
- 한 호흡(한 문장) 15단어 이내가 기본. 긴 설명도 두세 덩어리로 끊을 것.
- 난이도: 1부는 A2 45% / B1 35% / B2 15% / C1 5% (문장 단위 대략치). 쉬운 맞장구·확인과 긴 설명·관용구를 번갈아 배치. 고급 관용구는 Lucien이 공급.
- 문체: **일상 구어**. 단순과거, 접속법 반과거·대과거, 과도한 도치 금지. 구어 특징 적극 사용: ne 생략(Je sais pas), on(=nous), t'as/y a/j'sais 축약, 생략문, 문장 끝 확인(hein, non ?, quoi), 담화표지(ben, bah, enfin, alors, du coup, en fait, bon, tiens, écoute).
- tu/vous: 손님 앞은 정중한 vous. 주방·가족·동료 사이는 tu. 직원끼리는 tu (Chloé는 1화에서 Lucien에게 « monsieur Lucien » + vous, 3화부터 Lucien이 « tu » 하라고 해서 tu로 전환; Hélène·Julien·Karim과는 처음부터 tu).
- 거친 표현: 1부는 평온하므로 순한 속어(bouffe, boulot, galère, ras-le-bol, j'en ai marre, chiant, putain, merde 정도)만, **주방 안/직원끼리**에서만 가끔. 손님·외부인 앞에서는 절대 쓰지 않음. 모욕·차별·성적 표현 금지.
- 낭독용 대화이므로 숫자·가격은 읽기 쉽게(« dix-neuf euros » 처럼 단어 또는 « 19 € » — 한 화 안에서 통일하고 낭독 포인트에서 읽는 법 언급).
- 프랑스어 타이포: « 인용 » 은 공백 포함, ? ! : ; 앞에는 공백 한 칸 (builder가 nbsp 처리). 파이썬 문자열은 큰따옴표로 감싸고, 문자열 안에는 큰따옴표를 쓰지 말 것 (프랑스어 인용은 « »).
- 한글 해석: 자연스러운 한국어, 화자 말투(구어/존댓말/반말) 반영, 직역 금지, 1:1로 턴과 대응.

## 2. 고정 설정 (모든 화 공통, 어기지 말 것)
- 가게: **Le Comptoir de Marthe**, 파리 11구 오베르캄프 인근 rue Saint-Maur 근처의 가족 비스트로. 돌아가신 어머니 **Marthe**의 이름. 홀 30석 + 테라스 8석. 영업: 화~토 점심 12h–14h30, 저녁 19h–22h30 / 일요일 브런치 10h–15h / 월요일 휴무.
- 칠판 메뉴판(ardoise)은 입구 쪽 벽. 매일 아침 Hélène이 쓴다. Marthe의 손글씨 레시피 노트는 **분실된 상태** — 1부에서는 노트를 등장시키지 말 것. 단 2화에서 Lucien이 « le cahier de Marthe, on ne l'a jamais retrouvé » 식으로 한 번 암시(복선, 43화에서 발견됨). 다른 화에서 반복 언급하지 말 것.
- 인물: Hélène Marchand(42, 주인 겸 셰프, 완벽주의자·과묵·화나면 단호, 미슐랭 식당 부주방장 출신, 3년 전 어머니 식당 인수), Lucien Marchand(72, 아버지, 매일 아침 8시경 들러 참견, 속담·관용구, 은퇴한 창업자), Julien Benali(33, 홀 매니저, 유머러스·손님 응대의 달인), Chloé Dubois(22, 견습 서버·요리학교 alternance, 1화가 첫 출근, 질문 많음, 작은 어휘 수첩을 들고 다님), Karim Haddad(27, 부주방장, 재능·야심), Mme Vasseur(79세, 7번 창가 테이블 단골, 불평쟁이지만 가게를 가장 아낌), M. Bastide(채소·고기 납품업자, 쾌활한 시골 억양 느낌), M. Delmas(건물주, 15화 마지막 서류).
- 고정 메뉴/가격(최근 칠판 기준, 화마다 일부 바뀌는 건 OK): 점심 formule — plat du jour 16 €, entrée+plat 또는 plat+dessert 19 €, entrée+plat+dessert 24 €. 저녁 단품: entrée 9–12 €, plat 19–26 €, dessert 8–9 €. 대표 메뉴: œuf mayonnaise, velouté de petits pois, terrine de campagne, salade de chèvre chaud, steak-frites (21 €), blanquette de veau (Marthe의 방식, 22 €), cabillaud rôti, tarte Tatin, mousse au chocolat, crème brûlée, île flottante. 와인: vin de la maison (verre 5 €, pichet 25 cl 9 €), Sancerre, Brouilly 등.
- 시간 흐름: 1화 = 4월 첫 주 화요일. 이후 화들은 대략 하루~수 주 간격으로 흘러 15화 = 6월 중순 토요일 마감. 화 사이의 시간 경과는 첫 지문 또는 첫 대사로 분명히.
- 1부 분위기: 평온하고 따뜻한 유머. 긴장은 14화(주문 누락)와 15화 마지막에서만.
- 15화 마지막(클리프행어): 마감 정산 후 Hélène이 우편함에서 건물주 M. Delmas 명의의 등기우편(lettre recommandée)을 발견해 읽기 시작하고 안색이 변하는 데서 끝남. 내용(임대료 인상)은 구체적으로 밝히지 말 것 (16화에서 공개).

## 3. 1부 전체 15화 개요 (연속성 참고용 — 자기 담당 화만 쓰되 앞뒤를 고려)
| 화 | 제목 | 사건 | 학습 포인트 |
|---|---|---|---|
| 1 | Ouverture du mardi | 신입 클로에의 첫 출근, 칠판에 첫 메뉴를 씀. 직원 소개 | 인사, être/avoir, 시간·요일, 직업 |
| 2 | L'ardoise du jour | 오늘의 요리 설명 연습 | 부분관사, 음식 어휘, 설명 문형 |
| 3 | Une table pour deux | 예약 전화와 좌석 안내 | 예약 표현, 인원·시각, 정중한 vous |
| 4 | Prendre la commande | 첫 주문받기, 알레르기 확인 | 주문 표현, 의문문 3형태, vouloir/pouvoir |
| 5 | Entrée, plat, dessert | 점심 포뮬(formule) 단체 손님 | 수량·선택, 숫자, 가격 |
| 6 | Le steak trop cuit | 소소한 불만 1: 고기 익힘 정도 | cuisson 어휘, 사과·해결 표현 |
| 7 | Livraison du matin | 납품업자 바스티드와 재료 검수 | 식재료, 무게·가격, 비교급 |
| 8 | Le coup de feu | 점심 피크, 주방-홀 빠른 소통 | 명령형, 단문 지시, 대명사 입문 |
| 9 | L'addition, s'il vous plaît | 계산, 더치페이, 결제 오류, 팁 | 결제 어휘, 숫자, 수동적 표현 |
| 10 | Mme Vasseur et sa table | 단골 불평쟁이 응대 | imparfait(습관), 완곡 거절 |
| 11 | Un touriste perdu | 외국인 손님에게 메뉴 설명 | 설명·대안 제시, 영어 혼용 대처 |
| 12 | Anniversaire surprise | 깜짝 생일 케이크 이벤트 | futur proche, 축하 표현 |
| 13 | Dimanche en famille | 일요일 가족 브런치, 아이 손님 | 가족 어휘, 취향·선호 |
| 14 | La commande oubliée | 주문 누락과 주방 실수 | passé composé 서사, 책임·사과 |
| 15 | Fermeture et bilan | 마감 정산. 우편함에서 건물주 서류 발견(클리프행어) | 하루 정리, 현재·미래, 불안 표현 |

(각 화 학습 포인트의 문형이 대화 안에서 **반복 노출**되도록 설계. 단 설명조 대사로 어색하게 만들지 말고 장면 속 자연스러운 필요로 끌어낼 것 — Chloé의 질문이 좋은 장치.)

## 4. 데이터 파일 형식 (`epNN_data.py`)
```python
# -*- coding: utf-8 -*-
# (speaker, french, korean); speaker None => stage direction (not a turn)
H, L, J, C, K = "Hélène", "Lucien", "Julien", "Chloé", "Karim"   # 필요한 것만
D = [
(None, "Mardi, 9 h 40. ...", "화요일 오전 9시 40분. ..."),
(C, "Bonjour, je suis Chloé, la nouvelle.", "안녕하세요, 신입 클로에예요."),
# ... 정확히 120개의 (화자, ...) 튜플 (지문 제외)
]

VOCAB = [   # 최소 20개. (레벨, 표현, 뜻, 용법·메모). 레벨: "A2","B1","B2","C1" — 문장 난이도 비율과 비슷하게 분포(A2 8~9, B1 6~7, B2 3~4, C1 1~2)
("A2", "Bienvenue au Comptoir.", "…", "…"),
]
# 구어 표현은 메모 맨 앞에 [구어] 를 붙이고 같은 뜻의 정중한 표현을 « ↔ 정중: … » 형태로 비교.
# 속어(merde, putain, chiant 등)는 메모 맨 앞에 [속어] 를 붙이고 "쓸 수 있음: 가까운 주방 동료 사이 / 금지: 손님·상사·외부인 앞" 한 줄 명시.

GRAM = [    # 5~7개. (레벨, 제목, 설명) — 대화 속 실제 문장을 « » 로 인용해 설명. 해당 화 학습 포인트를 반드시 포함.
("A2", "…", "…"),
]

READ = [    # 낭독 포인트 5~7개. (제목, 설명) — 리에종·엘리종, r, u/ou, 비음, 억양, 호흡 구간을 이 화의 실제 문장으로. 한 문장 이상은 호흡 구간을 '/' 로 표시해 보여 줄 것. 한글로 설명하되 프랑스어 문장은 원문 그대로 인용.
("리에종 — vous_avez", "…"),
]

CULTURE = [  # 1~2개. (제목, 설명)
("…", "…"),
]

META = dict(part=1, ep=NN, part_label="제1부 Mise en place · 봄", title_fr="…", title_ko="…",
 place="…(장소·날짜·시간)", chars="Hélène Marchand (…) · …", wine="상황·주제 한 줄",
 focus="…학습 포인트…", levelmix="A2 45% / B1 35% / B2 15% / C1 5% 목표",
 next="제N+1화 « … » : 다음 화 예고 한 줄")
```
- 15화의 `next` 는 « 제2부 제16화 « Le courrier du propriétaire » : … » 로.
- `wine` 키 이름은 그대로 유지(빌더가 "상황·주제"로 표시).
- 확인 사항: 파이썬 문법 오류 없을 것, 튜플 끝 쉼표, 따옴표 짝.

## 5. 품질 기준 (집필자 셀프체크)
1. 프랑스어가 실제 프랑스인이 말하는 구어처럼 자연스러운가? (교과서 톤 금지, 단 학습자가 따라 읽을 수 있는 선)
2. 120턴 내내 장면에 서사(작은 갈등/전개/웃음)가 있는가? 똑같은 인사·맞장구의 반복으로 턴을 채우지 말 것.
3. 한 문장 15단어 초과를 피했는가? (check_ep.py가 20단어 초과를 경고)
4. 분석(VOCAB/GRAM/READ)이 대화 속 실제 문장에서 나왔는가? 일반론 금지.
5. 인물 말투·tu/vous·고정 설정을 지켰는가?
