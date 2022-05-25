# 영국인 미국인 영어 발음 음성 분류 인공지능

<<<<<<< HEAD
=======
1. 주제
- 영국인, 미국인 간 영어 발음 차이 구분을 위한 음성 이진 분류 인공지능
- 평소 억양이 특이 -> 다른 사람의 억양 정보에도 관심 -> 영국인, 미국인 영어 발음 음성 분류 인공지능 설계

2. 핵심 요약<br>
  (1) 문제 배경<br>
  \- 데이터 수집 문제<br>
  \- 다음 사전 발음 음성 추출 -> 일정 단어 수집 후 사용 제한<br>
  \- 구글 번역 음성 추출 -> 데이터 억양 문제 및 일정 단어 수집 후사용 제한<br>
  (2) 해결 방안<br>
  -> common voice 영국인, 미국인 문장 데이터 이용<br>
  \- 전처리(mfcc, mel spectrogram)<br>
  \- lstm, cnn모델 구축<br>
  (3) 결론<br>
  \- 검증 손실 0.22, 검증 정확도 0.91<br><br>

3. 기여한 점
- 개인 프로젝트
- 데이터 수집, 데이터 전처리, 인공지능 모델 설계

4. 사용 기술
- 데이터 전처리: Python librosa, pickle
- 인공지능 설계: Python tensorflow
- 시각화: Python matplotlib

5. 의견
- 학습에 사용된 데이터 외 다른 데이터에서의 정확도 향상 필요
- 현재 다른 데이터(미국, 영국 644개 문장 데이터) 테스트 결과, 검증 손실 1.89, 검증 정확도 0.50
>>>>>>> 3a5daf0769701794098d1166d783b2e0e2aad1a9
