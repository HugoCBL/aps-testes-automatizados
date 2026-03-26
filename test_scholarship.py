import pytest
from scholarship import evaluate_scholarship, Status

#entradas invalidas 
def test_invalid_gpa_below_zero():
    with pytest.raises(ValueError, match="GPA must be between 0 and 10."):
        evaluate_scholarship(18, -0.1, 90.0, True, False)

def test_invalid_attendance_above_hundred():
    with pytest.raises(ValueError, match="Attendance rate must be between 0 and 100."):
        evaluate_scholarship(18, 8.0, 100.1, True, False)

#APPROVED 
def test_approved_applicant():
    result = evaluate_scholarship(18, 8.5, 92.0, True, False)
    assert result.status == Status.APPROVED
    assert "Applicant meets all scholarship requirements." in result.reasons

#MANUAL_REVIEW 
def test_manual_review_age():
    result = evaluate_scholarship(17, 8.5, 92.0, True, False)
    assert result.status == Status.MANUAL_REVIEW
    assert "Applicant is under 18 and requires manual review." in result.reasons

#REJECTED (múltiplos motivos) 
def test_rejected_due_to_age():
    result = evaluate_scholarship(15, 8.5, 92.0, True, False)
    assert result.status == Status.REJECTED
    assert "Applicant is younger than the minimum age." in result.reasons

def test_rejected_due_to_gpa():
    result = evaluate_scholarship(18, 5.0, 92.0, True, False)
    assert result.status == Status.REJECTED
    assert "GPA is below the minimum required." in result.reasons

def test_rejected_due_to_disciplinary_record():
    result = evaluate_scholarship(18, 8.5, 92.0, True, True)
    assert result.status == Status.REJECTED
    assert "Applicant has a disciplinary record." in result.reasons

#valores limite 
@pytest.mark.parametrize("age, expected_status", [
    (15, Status.REJECTED),       #fronteira de idade < 16
    (16, Status.MANUAL_REVIEW),  #fronteira de idade >= 16 e <= 17
    (17, Status.MANUAL_REVIEW),  #fronteira de idade <= 17
    (18, Status.APPROVED),       #fronteira de idade > 17
])
def test_age_boundaries(age, expected_status):
    result = evaluate_scholarship(age, 8.5, 92.0, True, False)
    assert result.status == expected_status

@pytest.mark.parametrize("gpa, expected_status", [
    (5.9, Status.REJECTED),      #fronteira GPA < 6.0
    (6.0, Status.MANUAL_REVIEW), #fronteira GPA >= 6.0 e < 7.0
    (6.9, Status.MANUAL_REVIEW), #fronteira GPA < 7.0
    (7.0, Status.APPROVED),      #fronteira GPA >= 7.0
])
def test_gpa_boundaries(gpa, expected_status):
    result = evaluate_scholarship(20, gpa, 92.0, True, False)
    assert result.status == expected_status

@pytest.mark.parametrize("attendance, expected_status", [
    (74.9, Status.REJECTED),      #fronteira presença < 75.0
    (75.0, Status.MANUAL_REVIEW), #fronteira presença >= 75.0 e < 80.0
    (79.9, Status.MANUAL_REVIEW), #fronteira presença < 80.0
    (80.0, Status.APPROVED),      #fronteira presença >= 80.0
])
def test_attendance_boundaries(attendance, expected_status):
    result = evaluate_scholarship(20, 8.5, attendance, True, False)
    assert result.status == expected_status