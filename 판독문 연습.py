# "C:/Users/eun07/OneDrive/바탕 화면/captstone/medical_report.txt", "w"

with open("C:/Users/eun07/OneDrive/바탕 화면/captstone/medical_report.txt", 'r') as file:
    lines = file.readlines()  # 파일의 모든 줄을 읽어옴

new_lines = []
for line in lines:
    columns = line.strip().split(':')  # 각 줄을 ':'를 기준으로 분리하여 리스트로 변환
    new_lines.extend(columns)  # 분리된 열을 리스트에 추가
   
