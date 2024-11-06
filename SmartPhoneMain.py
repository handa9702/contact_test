# SmartPhoneMain.py

from SmartPhone import SmartPhone
from Addr import Addr

def start():
    phone = SmartPhone()
    
    while True:
        print("\n--- Contact Management Menu ---")
        print("1. 연락처 저장")
        print("2. 연락처 수정")
        print("3. 연락처 출력")
        print("4. 연락처 삭제")
        print("5. 종료")
        choice = input("원하는 작업을 선택하세요: ")
        
        if choice == '1':
            # 연락처 저장
            name = input("이름을 입력하세요: ")
            phone_num = input("전화번호를 입력하세요: ")
            email = input("이메일을 입력하세요: ")
            address = input("주소를 입력하세요: ")
            group = input("그룹을 입력하세요 (예: 친구/가족): ")
            
            contact = Addr(name, phone_num, email, address, group)
            phone.add_contact(contact)

        elif choice == '2':
            # 연락처 수정
            name = input("수정할 연락처의 이름을 입력하세요: ")
            print("새로운 연락처 정보를 입력하세요.")
            new_name = input("새 이름: ")
            new_phone = input("새 전화번호: ")
            new_email = input("새 이메일: ")
            new_address = input("새 주소: ")
            new_group = input("새 그룹 (예: 친구/가족): ")
            
            new_contact = Addr(new_name, new_phone, new_email, new_address, new_group)
            phone.update_contact(name, new_contact)

        elif choice == '3':
            # 연락처 출력
            print("\n--- 모든 연락처 출력 ---")
            phone.show_contacts()

        elif choice == '4':
            # 연락처 삭제
            name = input("삭제할 연락처의 이름을 입력하세요: ")
            phone.delete_contact(name)

        elif choice == '5':
            # 종료
            print("연락처 관리 프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다. 다시 선택해 주세요.")

# 프로그램 실행
if __name__ == "__main__":
    start()
