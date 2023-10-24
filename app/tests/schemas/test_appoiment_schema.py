from app.schemas.appointment import Appoiment, AppoimentCreate, AppoimentOutput


def test_appoiment():
    appoiment = Appoiment(
        status=True,
        reason="reason",
        anonymous=True
    )

    assert appoiment.status
    assert appoiment.reason == "reason"
    assert appoiment.anonymous

def test_appoiment_input():
    appoiment = AppoimentCreate(
        agenda_day_hour_id=1,
        status=True,
        reason="reason",
        anonymous=True
        # psychologist_id=1,
        # patient_id=1
    )

    assert appoiment.agenda_day_hour_id == 1
    assert appoiment.status
    assert appoiment.reason == "reason"
    assert appoiment.anonymous
    # assert appoiment.psychologist_id == 1
    # assert appoiment.patient_id == 1

def test_appoiment_output():
    appoiment = AppoimentOutput(
        id=1,
        agenda_day_hour_id=1,
        status=True,
        reason="reason",
        anonymous=True,
        created_at="22-10-2023 00:00:00",
        updated_at="22-10-2023 00:00:00"
        # psychologist_id=1,
        # patient_id=1,
    )

    assert appoiment.id == 1
    assert appoiment.status
    assert appoiment.reason == "reason"
    assert appoiment.anonymous
    assert appoiment.created_at == "22-10-2023 00:00:00"
    assert appoiment.updated_at == "22-10-2023 00:00:00"
    # assert appoiment.agenda_day_hour_id == 1
    # assert appoiment.psychologist_id == 1
    # assert appoiment.patient_id == 1