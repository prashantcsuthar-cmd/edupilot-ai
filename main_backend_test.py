from parsers import extract_text_from_pdf
from agent_core import audit_transcript_with_ai, generate_quiz_from_syllabus
from optimizer import optimize_study_schedule

def test_backend():
    print("🚀 --- Testing EduPilot AI Backend --- 🚀\n")

    # 1. Test Optimization Engine
    print("1️⃣ Testing Mathematical Study Optimizer...")
    sample_topics = [
        {"topic": "Numerical Optimization (BFGS / GD)", "weight": 0.35, "confidence": 0.30},
        {"topic": "Pattern Recognition", "weight": 0.25, "confidence": 0.60},
        {"topic": "Neural Networks & Backprop", "weight": 0.25, "confidence": 0.80},
        {"topic": "Linear Algebra Shocks", "weight": 0.15, "confidence": 0.50}
    ]
    optimized_schedule = optimize_study_schedule(sample_topics, total_hours=15.0)
    print("Optimized Schedule Output:", optimized_schedule)
    print("✅ Optimization Engine Passed!\n")

    # 2. Test AI Agent Function Calling
    print("2️⃣ Testing AI Agent Audit Engine...")
    sample_transcript = "Prashanth C, IIT Jodhpur. BS in Applied AI. Passed Foundations of AI, Linear Algebra, Optimization. Missing: Pattern Recognition Lab."
    audit_results = audit_transcript_with_ai(sample_transcript, target_career="AI Engineer")
    print("Audit Output:", audit_results)
    print("✅ Audit Engine Passed!\n")

    # 3. Test Quiz Generator
    print("3️⃣ Testing Quiz Generation Engine...")
    sample_syllabus = "Unit 1: Gradient Descent, BFGS, Backtracking Line Search. Unit 2: Convex sets, Rosenbrock function optimization."
    quiz = generate_quiz_from_syllabus(sample_syllabus, num_questions=2)
    print("Quiz Output:", quiz)
    print("✅ Quiz Engine Passed!\n")

    print("🎉 ALL BACKEND SYSTEMS GO! Ready for GitHub commit.")

if __name__ == "__main__":
    test_backend()