import json
from parsers import extract_text_from_pdf
from agent_core import audit_transcript_with_ai, generate_quiz_from_syllabus
from optimizer import optimize_study_schedule

def run_interactive_menu():
    print("==========================================")
    print("      EDUPILOT AI - BACKEND TESTER        ")
    print("==========================================\n")

    while True:
        print("\nChoose a module to test:")
        print("1. Test Mathematical Optimizer Engine")
        print("2. Test Live Transcript Audit (AI Agent)")
        print("3. Test Quiz Generator (AI Agent)")
        print("4. Exit")

        choice = input("\nEnter choice (1-4): ").strip()

        if choice == "1":
            print("\n--- Testing Study Allocation Engine ---")
            topics = [
                {"topic": "Numerical Optimization", "weight": 0.40, "confidence": 0.20},
                {"topic": "Pattern Recognition", "weight": 0.30, "confidence": 0.70},
                {"topic": "Linear Algebra", "weight": 0.30, "confidence": 0.50},
            ]
            hours = float(input("Enter available total study hours (e.g. 15): ") or 15)
            result = optimize_study_schedule(topics, total_hours=hours)
            print("\n[OPTIMIZER RESULT]:")
            print(json.dumps(result, indent=2))

        elif choice == "2":
            print("\n--- Testing AI Degree Audit ---")
            career = input("Enter Target Career (e.g. AI Engineer, Data Scientist): ") or "AI Engineer"
            sample_text = input("Paste sample transcript text (or press Enter for default): ")
            if not sample_text:
                sample_text = "Prashanth C, IIT Jodhpur. BS in Applied AI. Completed: Linear Algebra, Foundations of AI. Missing: Pattern Recognition, Optimization."
            
            print("\nAuditing with Gemini 2.5 Flash...")
            audit = audit_transcript_with_ai(sample_text, target_career=career)
            print("\n[AUDIT RESULT]:")
            print(json.dumps(audit, indent=2))

        elif choice == "3":
            print("\n--- Testing Quiz Generator ---")
            sample_syllabus = input("Paste sample syllabus text (or press Enter for default): ")
            if not sample_syllabus:
                sample_syllabus = "Gradient Descent, Armijo Backtracking Line Search, Newton-Raphson Optimization, Convexity."
            
            print("\nGenerating Quiz with Gemini 2.5 Flash...")
            quiz = generate_quiz_from_syllabus(sample_syllabus, num_questions=2)
            print("\n[QUIZ RESULT]:")
            print(json.dumps(quiz, indent=2))

        elif choice == "4":
            print("\nExiting Backend Tester. You're ready to win!")
            break
        else:
            print("Invalid selection. Try again.")

if __name__ == "__main__":
    run_interactive_menu()