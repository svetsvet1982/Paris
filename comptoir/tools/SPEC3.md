# 《Le Comptoir de Marthe》 3·4·5부 제작 사양 (31~75화)

**먼저 `/home/user/Paris/comptoir/tools/SPEC.md` (규격·문체·데이터 파일 형식·품질 기준) 와 `SPEC2.md` §2·§3 (1~2부에서 확정된 사실)를 읽는다.** 이 문서는 3~5부 전용 덮어쓰기/추가 사항이며 우선한다. 완성된 앞 부분 예시: `tools/part2/ep30_data.py`, `tools/part1/ep15_data.py` (형식·톤 참고, 필요한 부분만).

## 0. 경로·명령
- 파일: `/home/user/Paris/comptoir/tools/partP/epNN_data.py` (P=부 번호, NN=화 번호 두 자리). 검증: `cd /home/user/Paris/comptoir/tools/partP && python3 -I ../check_ep.py epNN_data` → OK 될 때까지.
- META: `part=P`, `ep=NN`, part_label 은 아래 부별 값. `levelmix` 는 부별 값. 부 마지막 화 `next` 는 다음 부 첫 화 예고.
- docx/pdf 빌드·git commit 금지. 다른 화 파일 수정 금지. 끝나면 화별 확정 사실(날짜, 숫자, 새 설정)을 5줄 이내 보고.
- check_ep.py 는 한 문장 20단어 초과를 경고(0이 목표). 화당 지문 최대 6개. 화자 2~4명(독백 장면도 2~4명으로 구성: 예 `Hélène` + `Hélène (pensée)` + 전화 속 상대).

## 1. 부별 문체 조정
- **3부 Au bord du gouffre (가을, B2~C1; A2 10/B1 25/B2 40/C1 25)**: 위기의 정점. 날것의 구어: 욕설(merde, putain, bordel, chiant, con), 소리침, 말 끊기, 중얼거림 적극 사용(모욕·차별·성적 표현 금지, 손님·외부인 앞 금지). 은행·검사관·변호사·건물주 장면은 정중한 vous이되 **문어가 아닌 정중한 구어**. 공문·청원서는 짧게 낭독 후 곧바로 구어로 반응. 접속법(과거 포함), 조건법 과거, 수동태. part_label=`제3부 Au bord du gouffre · 가을`.
- **4부 La reconstruction (늦가을·겨울, B2~C1; A2 5/B1 20/B2 40/C1 35)**: 재건. 안도의 putain, enfin ! 같은 감탄으로 3부와 대비. 전문 어휘(회생 절차, 크라우드펀딩, 공사, 제철 요리, 미식 비평). 법원 장면은 변호사가 쉽게 풀어 말함. part_label=`제4부 La reconstruction · 늦가을·겨울`.
- **5부 Le Comptoir de Marthe (이듬해 봄·여름, B2~C1; A2 5/B1 15/B2 40/C1 40)**: 성공 뒤의 시험. 연설·축사·병상 독백은 문장을 짧게 끊고 구어 리듬 유지(Alors voilà… 식). 관용구·속담 풍부(Lucien). part_label=`제5부 Le Comptoir de Marthe · 이듬해 봄·여름`.
- 모든 부: 일상 구어(단순과거·접속법 반과거·대과거 금지, ne 생략, on, 축약, 담화표지). 한 호흡 15단어 이내. 분석: 구어 `[구어]`+« ↔ 정중 », 속어 `[속어]`+« 쓸 수 있음 / 금지 » 한 줄. 난이도가 오른 만큼 VOCAB 레벨 분포는 부별 비율을 따를 것(예: 3부 A2 2~3 / B1 5~6 / B2 8~9 / C1 5~6, VOCAB 22~26개).

## 2. 확정 사실 (1~2부, 계속 유효)
SPEC2.md §2·§3 + 2부 결과:
- 8/29(토) 마지막 서비스: 8월 매출 40,257 € / 지출 41,800 € (적자 1,543 €), 10월부터 임대료 5,200 €(월 약 2,943 € 적자 예상). 냉장고 수리비 1,450 € 지출 완료. Karim 7/31 떠남(리옹 Maison Perrault). Sofiane(단기 보조)은 8/29 마지막 근무. Victor의 L'Atelier de Victor(포뮬 14~16 €, 약 15% 저렴)는 맞은편. Victor는 19세 여름 Marthe 밑에서 plongeur 한 달 일함(25화), Hélène과 서로 vous 유지("Pas encore"). 칠판에 "Ici, tout est fait maison. Depuis trente-cinq ans." 가 25화부터 있음. 가게 개업 1991년(35년). Lucien이 제안한 "tablée du mardi"(화요일 저녁 12명 22 € 정액)를 2주 시험(27화, 8/11~).
- 22화: 메뉴를 19→12가지로 축소, plat de la semaine 도입(8/31까지 시험). 23화: M. Roussel 부인의 식중독 의심 사건(7/25), 118 € 환불. 24화: 인플루언서 Inès Marceau(@ines.mange)가 8/4 방문, story 후 예약 12건. 28화: 8/22(토) M. Roussel(인쇄소 사장) 은퇴 깜짝 파티 30명 1,950 € 행사(성사됨, 최종 수익 약 1,100 €). 29화: Julien에게 8구 Chez Armand(사장 Armand Belloc) 홀총괄 제안(월급 +1,000 €, 10/1 시작, 답변 기한 9/15) — Julien은 은행 약속 후 답하겠다고 함.
- **30화 클리프행어**: 9/3(목) 10시 Mme Garnier(은행 여신 담당)와 약속. 임대차 계약서·결산서 지참. Hélène 혼자 가겠다고 함(Lucien은 동행 원했음). 칠판의 « Août » 를 지우고 « Septembre ».
- 레시피 노트: 43화에서 **발견**. 그 전에는 언급 금지(단 2화 암시 한 번 있었음), 43화 이전 3부 화에서 노트를 언급하지 말 것(2화 암시 이후 "한 번도 못 찾았다" 상태).

## 3. 3부 확정 줄거리·날짜 (31~45화, 2026년)
| 화 | 날짜 | 제목 | 확정 사건/숫자 | 학습 포인트 |
|---|---|---|---|---|
| 31 | 9/3(목) 10시 | Rendez-vous à la banque | Mme Garnier(40대, 정중·냉정, 은행 « Crédit Parisien »)와 상담. 요청 대출 60,000 €(8년). 자료: 임대차계약, 최근 12개월 결산, 월별 매출, 차입 계획. Hélène 혼자 감. 은행은 « 검토 후 일주일 내 회신 ». | 금융 어휘, 격식 대화, 설득 |
| 32 | 9/10(목) | Le refus | Garnier 전화+서면 거절: ① 최근 6개월 현금흐름 적자 ② 임대료 인상으로 상환능력 부족 ③ 담보·개인보증 한도 부족. Hélène 충격, Julien·Lucien 반응. 같은 날 Julien은 Armand에게 « 10/31까지 시간을 달라 » 요청해 승낙받음(답변 기한 연장). | 감정 서술, 수동태 |
| 33 | 9/15(화) | L'inspection | Inspecteur Morel(DDPP, 50대 담담) 불시 방문(익명 신고 암시, 출처 밝히지 말 것). 적발: ① 건식 창고에 쥐 배설물 흔적 ② 6/30 냉장고 고장 때 온도 기록 누락 ③ 일부 식재료 DLC 라벨 미표기 ④ 손 씻는 세면대 비누 부족. | 규정·행정 어휘, 접속법 |
| 34 | 9/18(금) | Fermeture administrative | 도 지사 명의 폐쇄 명령(arrêté) 15일간(9/18~10/2). 정문에 게시. 공문 짧게 낭독 후 구어 반응. 재개점 조건: 방제업체 시공 + 기록 체계 + 재검사(contre-visite). 필요 비용 약 2,300 €. | 법률 어휘, 공문 낭독 |
| 35 | 9/21(월) | Les adieux au personnel | Hélène이 직원들에게 « 휴직(chômage partiel) » 통보. Chloé·Moussa·Julien 반응. Julien은 « tant que le navire flotte » 남겠다고. | 완곡·유감 표현, 접속법 |
| 36 | 9/24(목) 밤 | Nuit blanche | Hélène의 내적 독백. 빈 홀, 계산기, 전화(Julien·Lucien 목소리). 생략·반복·끊어 말하기. 화자: `Hélène`, `Hélène (pensée)` 등 2~4. | 혼잣말 구어, 내면 서술 |
| 37 | 9/27(일) | Conseil de famille | Lucien·Hélène(+선택 Julien) 가족 회의. Lucien이 모아둔 40,000 €와 자기 아파트 담보 제안, Hélène 거절. | 조건법 과거, 가정 |
| 38 | 10/6(화) | L'offre de rachat | 가게는 10/3(토) 재개점(방제·기록 체계 시공 후 재검사 통과). 10/6 Faure(외식 체인 Groupe Faure, 14개 브라스리, 50대 세련된 달변) 인수 제안: 영업권 180,000 €, 브랜드 « Le Comptoir de Marthe » 유지, Hélène은 월급제 « chef consultant », 임대료·채무는 그룹이 인수. 회신 기한 11/4. | 계약·협상 어휘, 양보 |
| 39 | 10/8(목) | Chloé ne lâche pas | 견습생 Chloé가 « 인수는 안 돼요 »며 반전 제안: 생산자 직거래 + 짧은 제철 메뉴 + tablée du mardi 확대(데이터 첨부). Hélène 처음엔 일축. | 논증 구조, 설득 |
| 40 | 10/13(화) | La pétition des habitués | Mme Vasseur 주도 단골 청원서(서명 214명) 낭독(짧게) + 구어 반응. | 호소·공감 표현 |
| 41 | 10/16(금) | Le critique revient | 비평가 Étienne Roux(60대, 까다로운 신문 칼럼니스트) 재방문, 솔직하고 날카로운 평(혼합). | 미식 비평 어휘, 형용사 |
| 42 | 10/20(화) | La grande dispute | 부녀 대폭발. Lucien은 « 팔아라, 네 건강이 먼저 » / Hélène은 « 아빠는 엄마가 아팠을 때 가게만 봤잖아 » 식 묵은 감정. 욕설·소리침·말 끊기 최대치. 마지막 침묵. | 접속법 과거, 비난·화해 |
| 43 | 10/22(목) | Le carnet de Marthe | Lucien이 자기 집 오래된 공구함 속에서 Marthe의 손글씨 레시피 노트(« le carnet ») 발견해 가져옴. Hélène이 첫 쪽(« Pour ma fille ») 낭독. 부녀 화해 시작. | 대과거, 회상 서사 |
| 44 | 10/27(화) | Chez Maître Aubry | Me Aubry(변호사 40대 후반)가 « procédure de sauvegarde » 설명: 지급정지 전 단계라 가능, 관찰기간 6개월, 채무 동결, 상환계획. redressement/liquidation과 비교. 필요 서류. | 법률 상담 어휘, 조건·절차 |
| 45 | 11/3(화) | La décision d'Hélène | Faure에게 인수 거절(전화/방문), 변호사에게 sauvegarde 신청 지시, 직원·Lucien에게 선언. 3부 마무리. next: 제4부 46화 Le tribunal de commerce. | 결정·의지 표현, 가정문 종합 |
- 3부 영업 상황: 10/3 재개점 후 매출은 낮음(일평균 점심 30·저녁 28 couverts 수준). 임대료 5,200 €(10/1~)은 10/5 첫 월세를 못 냄(미납). 총부채 추정 약 92,000 €(임대료 미납분 + 납품업체 + 세금·사회보험 + 장비). Bastide에게 4,200 € 외상.
- 3부 인물 추가: Mme Garnier, Insp. Morel, Étienne Roux, Me Aubry, M. Faure(Groupe Faure Restauration). 이들은 해당 화에만 등장.

## 4. 4부 확정 줄거리·날짜 (46~60화, 2026-11~2027-01)
| 화 | 날짜 | 제목 | 확정 사건/숫자 | 학습 포인트 |
|---|---|---|---|---|
| 46 | 11/12(목) | Le tribunal de commerce | 파리 상사법원. 판사·검사 관여, Me Aubry가 쉽게 풀이. 절차 개시 판결(sauvegarde, 관찰기간 6개월), 법원 지정 mandataire judiciaire Mme Lemaire(50대). | 법원 절차 설명, 전문 어휘 |
| 47 | 11/16(월 휴무일) | Les créanciers | 채권자 협의: Delmas(미납 임대료 5,200 × 월분), Bastide(4,200 €), 세무·URSSAF, 설비업체. 총 채무 92,000 €→ 8년 분할 상환안(1년차 거치+단계 상승). Delmas는 임대료 인하는 거부, 미납분 12개월 분할만 수락. | 협상·양보, 수치 설명 |
| 48 | 11/19(목) | Le financement participatif | 크라우드펀딩 영상 촬영, 목표 40,000 €, 30일. 보상: 시식권·칠판에 이름. Hélène 카메라 앞에서 어색. 첫날 3,200 € 모금. | 구어체 호소, 수사 질문 |
| 49 | 11/23(월) | Le retour de Karim | Karim이 리옹 후 3개월 만에 복귀(« une brigade qui crie, ce n'est pas pour moi »). 화해, 접속법. Hélène이 받아줌. | 사과·용서, 접속법 |
| 50 | 11/26(목) | Les producteurs répondent | Bastide와 노르망디·부르고뉴 소규모 생산자 4명이 연대 계약(후불 60일, 최소 구매 약속, 가격 안정). Bastide 외상 4,200 € 12개월 분할 수락. | 농산물·계약 어휘 |
| 51 | 12/1(화) | Chantier et bonnes surprises | 가게는 11/22~12/14 보수 공사 휴업(주방 환기·바닥·홀 페인트·칠판 새 벽). 벽 속에서 오래된 신문·병 등 발견 같은 작은 놀라움. 공사업자 M. Lopes. 예산 14,000 €. | 건축·공사 어휘, faire + 부정사 |
| 52 | 12/7(월) | La carte de saison | 제철 겨울 메뉴 재구성(노트 참고, Marthe의 방식). 메뉴 10가지, 대표: soupe à l'oignon, blanquette Marthe, poule au pot, tarte Tatin. | 요리 설명, 미식 어휘 |
| 53 | 12/11(금) | Le repas test | 후원자·이웃 초청 시식회 40명. 감각 표현, 평가. | 감각 표현, 평가 |
| 54 | 12/15(화) | Rouvrir | 재개점 첫날 점심 긴장·안도. Mme Vasseur 7번석 복귀. | 환영 인사, 긴장·안도 |
| 55 | 12/17(목) | Victor frappe à la porte | Victor가 공동 구매·행사 협력 제안(진심 + 계산). Hélène 처음 tu로 전환 시작. | 화해·타협, 비교 |
| 56 | 12/19(토) | Le soir des critiques | 기자(Julie Marchetti, 일간지)와 Étienne Roux 동시 방문, 인터뷰. | 인터뷰 화법, 간접화법 |
| 57 | 12/22(화) | Le guide passe | 익명 미식 가이드 « Guide Lacroix » 심사관 방문(누군지 모른 채 긴장), 마지막에 의심 정황만. | 긴장 서사, 완곡 표현 |
| 58 | 12/31(목) | Réveillon au Comptoir | 만석 60명, 건배·덕담, 크라우드펀딩 최종 모금 총액 발표(43,870 €). | 건배·덕담, 다인 대화 |
| 59 | 1/15(금) | Le premier bilan | 재개점(12/15)~1/14 첫 한 달 결산: 흑자 + 3,150 €. 숫자 요약. | 숫자·결산 표현, 요약 |
| 60 | 1/18(월 휴무일) | Résolutions de janvier | 새해 결심, 호텔 Le Grand Parisien 지배인 Mme Delorme의 케이터링 제안서 도착(클리프행어). next: 제5부 61화. | 결심·계획, 미래 서술 |
- 4부 새 설정: 매일 칠판 « Ici, tout est fait maison. Depuis trente-cinq ans. » 위에 새 문구 « Merci à vous 1 237. » (후원자 수). 크라우드펀딩 수수료 후 수령액은 필요 시 계산해 쓰되 모순 없게.
- 4부에서 Karim 복귀 후 팀: Hélène, Karim, Julien, Chloé, Moussa. 3부의 Julien 문제(Armand 답변 기한 10/31)는 **4부 시작 전에 Julien이 거절·잔류로 정리**했다고 46~47화에서 한 줄 언급(« J'ai dit non à Armand fin octobre. ») — 66화 동업 복선.

## 5. 5부 확정 줄거리·날짜 (61~75화, 2027-03~07)
| 화 | 날짜 | 제목 | 확정 사건/숫자 | 학습 포인트 |
|---|---|---|---|---|
| 61 | 3/16(화) | Le succès et ses revers | 예약 폭주(3주 후까지 만석), 직원 과로, Karim·Chloé 탈진. 3월 매출 사상 최고 | 원인·결과 연결어, 피로 표현 |
| 62 | 3/23(화) | Recruter | 신규 채용 면접(요리사 보조 1·서버 1). 후보 2~3명, 질문 화법. 합격 Léna(서버)·Malik(요리 보조) | 채용·이력서 어휘 |
| 63 | 4/1(목) | L'offre de l'hôtel | Mme Delorme(Le Grand Parisien 지배인, 50대 세련·직설)와 케이터링 계약 협상: 연회 월 2회, 인당 68 €, 최소 80명 | 호텔 서비스 어휘, 조건 협상 |
| 64 | 4/20(화)~4/24(토) | Banquet au Grand Hôtel | 4/24(토) 120명 연회 서비스. 격식 지시 | 대규모 서비스 지시, 격식 |
| 65 | 5/4(화) | La tentation de s'agrandir | 옆 점포(전 빵집) 임대 제안·확장(홀 20석 추가) 투자 120,000 € 검토 | 투자·위험, 가정문 |
| 66 | 5/11(화) | Julien, associé | Julien이 지분 20%를 갖는 동업자가 됨(Hélène 80%). 계약·지분 대화 | 지분·계약, 격식 대화 |
| 67 | 5/18(화) | Un client célèbre | 유명 배우 Thomas Valmont(40대, 가상 인물) 방문, 프라이버시 | 완곡·신중한 응대, 조건법 |
| 68 | 5/25(화) | Le reportage télé | TV 촬영 팀(채널 « France Cuisine », 가상) 방문, 인터뷰 | 미디어 어휘, 인터뷰 |
| 69 | 6/1(화) | Grève et pénurie | 파업으로 납품 차질, 임기응변, Bastide·Victor와 협력 | 비상 대응, 대안 제시 |
| 70 | 6/8(화) | Lucien à l'hôpital | Lucien이 가게에서 쓰러짐(심장 부정맥, 병원 입원, 안정적 상태) | 병원·의료 어휘, 불안과 위로 |
| 71 | 6/12(토) | Transmission | 병상에서 레시피 노트의 의미와 가게 전수. 차분한 구어 독백 | 회상, 차분한 구어 독백 |
| 72 | 6/19(토) | Le courrier du guide | Guide Lacroix 선정 소식(별 2개 « deux fourchettes » 와 « 올해의 재건 » 상) | 기쁨·감정 폭발, 감탄 |
| 73 | 6/22(화) | Mme Vasseur fête ses quatre-vingts ans | 80세(그녀는 6/20생) 생일 잔치, 축사·회고 | 덕담, 축사, 회고 |
| 74 | 6/29(화) | Lucien raccroche son tablier | 퇴원 후 은퇴 연설(짧은 문장, 관용구) | 구어체 연설, 관용구 |
| 75 | 7/6(화) | Le Comptoir de Marthe | 다시 화요일 아침. 신입 견습생 Maxime(19)을 Chloé가 맞이하고 칠판에 글씨. 1화 수미상관(« Bonjour, je suis… la nouvelle »의 역전) | 1화 수미상관, 총정리 |
- 5부 설정: Chloé는 이제 견습 2년 차 졸업 예정, 정규직 서버·부매니저 제안. 5부 가격 인상: 점심 formule 22/27 €. Victor와는 상호 tu. 호텔 연회 수익으로 채무 상환이 계획보다 앞섬(61~66화에서 한 줄씩).
- 75화는 1화와 구조·표현을 의도적으로 겹쳐 쓰고(1화 ep01_data.py 를 읽어 대응), 120턴.

## 6. 담당 에이전트 간 연계 규칙
- 날짜·숫자는 이 문서가 기준. 이 문서에 없는 새 사실은 **자기 화 안에서만** 쓰고, 다른 화가 이를 전제하지 않도록 한다(꼭 필요하면 보고에 명시).
- 인물 호칭: Lucien·Hélène는 «Papa». Chloé→Lucien tu, Julien→Lucien tu. Hélène↔Julien·Karim·Chloé tu. 외부인(은행·법원·검사관·호텔)에게는 vous.
- 이름 중복 주의: Roussel(1부 5화 단체 대표, 2부 23·28화 손님, 3부 41화 Étienne Roux 와 혼동 금지), Perrin, Garnier(은행 Mme Garnier — 1부 4화의 Mme Garnier 손님과는 **동명이인**이지만 3부 31·32화에서는 '이름이 같은 다른 사람'이라고 굳이 언급하지 않음).
