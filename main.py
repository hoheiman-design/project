from models import Student, Teacher
import logic

def show_menu():
    print("\n" + "="*30)
    print(" SCHOOL MANAGEMENT SYSTEM ")
    print("="*30)
    print("1. Add New Student")
    print("2. Add Student Grade")
    print("3. Show All Reports (Polymorphism)")
    print("4. Rank Students by Performance (Heap Sort)")
    print("5. Exit")
    print("="*30)

def main():
    
    students = []
    teachers = [Teacher("Mr. Wong", "T001", "Science")] 

    while True:
        show_menu()
        choice = input("Select an option (1-5): ")

        if choice == '1':
            name = input("Enter Student Name: ")
            s_id = input("Enter Student ID: ")
            students.append(Student(name, s_id))
            print(f"Success: Student {name} has been added.")

        elif choice == '2':
            if not students:
                print("Error: No students found. Please add a student first.")
                continue
            
            # 
            print("\nSelect a student to update:")
            for idx, s in enumerate(students):
                print(f"{idx}. {s.name} ({s.id_number})")
            
            try:
                s_idx = int(input("Enter index number: "))
                subject = input("Enter Subject Name: ")
                score = float(input("Enter Score (0-100): "))
                
                students[s_idx].add_grade(subject, score)
                print(f"Grade updated for {students[s_idx].name}.")
            except (ValueError, IndexError):
                print("Invalid input. Please try again.")

        elif choice == '3':
            print("\n--- Generating All Member Reports ---")
            # Polymorphism
            all_members = teachers + students
            if not all_members:
                print("System is empty.")
            else:
                for person in all_members:
                    
                    print(person.generate_report())

        elif choice == '4':
            if not students:
                print("No student data available for ranking.")
                continue
            
            print("\n--- Ranking Students (Powered by Heap Sort) ---")
            #
            ranked_list = logic.rank_students(students)
            for i, s in enumerate(ranked_list):
                print(f"Rank {i+1}: {s.name} | Average: {s.get_average():.1f}")

        elif choice == '5':
            print("Exiting System... Have a nice day, Teacher!")
            break
        
        else:
            print("Invalid option. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()