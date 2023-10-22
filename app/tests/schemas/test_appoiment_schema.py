from app.schemas.appoiment import Appoiment, AppoimentOutput, AppomeintInput


def test_appoiment():
    appoiment = Appoiment(
        status=True,
        description="description",
        reason="reason",
        anonymous=True
    )

    assert appoiment.status
    assert appoiment.description == "description"
    assert appoiment.reason == "reason"
    assert appoiment.anonymous

def test_appoiment_input():
    appoiment = AppomeintInput(
        agenda_day_hour_id=1,
        psychologist_id=1,
        patient_id=1,
        status=True,
        description="description",
        reason="reason",
        anonymous=True
    )

    assert appoiment.agenda_day_hour_id == 1
    assert appoiment.psychologist_id == 1
    assert appoiment.patient_id == 1
    assert appoiment.status
    assert appoiment.description == "description"
    assert appoiment.reason == "reason"
    assert appoiment.anonymous

def test_appoiment_output():
    appoiment = AppoimentOutput(
        id=1,
        agenda_day_hour_id=1,
        psychologist_id=1,
        patient_id=1,
        status=True,
        description="description",
        reason="reason",
        anonymous=True
    )

    assert appoiment.id == 1
    assert appoiment.agenda_day_hour_id == 1
    assert appoiment.psychologist_id == 1
    assert appoiment.patient_id == 1
    assert appoiment.status
    assert appoiment.description == "description"
    assert appoiment.reason == "reason"
    assert appoiment.anonymous