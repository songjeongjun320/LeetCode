# 파일을 읽어 중복을 제거하고 정렬된 결과를 TSX 파일로 저장하는 코드
def create_tsx_file_with_unique_companies(input_filename, output_filename):
    try:
        # 입력 파일에서 회사 이름을 읽기
        with open(input_filename, 'r', encoding='utf-8') as file:
            company_list = file.readlines()
        
        # 회사 이름의 앞뒤 공백을 제거하고 중복된 이름을 제거한 후 정렬
        unique_companies = sorted(set(company.strip() for company in company_list))
        
        with open(output_filename, 'w', encoding='utf-8') as file:
            for company in unique_companies:
                file.write(company)
                file.write("\n")
        
        print(f"파일이 성공적으로 생성되었습니다: {output_filename}")
        
    except FileNotFoundError:
        print(f"입력 파일을 찾을 수 없습니다: {input_filename}")

# 실행 예시: companylist.txt에서 데이터를 읽고 company_sorted.tsx에 저장
create_tsx_file_with_unique_companies('companylist.txt', 'company_sorted.txt')
