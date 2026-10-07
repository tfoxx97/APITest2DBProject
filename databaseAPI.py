from datetime import datetime
from sqlalchemy.orm import sessionmaker
from models import (
    engine,
    Firmware,
    Release,
    Results,
)
from shared import RELEASE

# --------------------------------------------------------------------------- #
#  Database helpers
# --------------------------------------------------------------------------- #

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_or_create_release(session, name: str = "default") -> Release:
    """Return a Release record – create it if it does not exist."""
    release = session.query(Release).filter_by(name=name).first()
    if release is None:
        release = Release(name=name)
        session.add(release)
        session.flush() # gives us the new ID without commit
    return release

def get_or_create_firmware(session, firmware_str: str, release_name: str = "default") -> Firmware:
    """
    Return a Firmware record – create it if it does not exist.
    The firmware is stored with a reference to a Release.
    """
    release = get_or_create_release(session, RELEASE)
    firmware = (
        session.query(Firmware)
        .filter_by(firmware=firmware_str, release_id=release.id)
        .first()
    )
    if firmware is None:
        firmware = Firmware(firmware=firmware_str, release_id=release.id)
        session.add(firmware)
        session.flush()
    return firmware

def write_test_result(
    session,
    firmware_str: str,
    date_tested: datetime,
    component: str,
    feature: str,
    scenario_id: int,
    result: bool,
    debug: str | None,
):
    """
    Persist a test result in the database.
    """
    firmware = get_or_create_firmware(session, firmware_str, RELEASE)
    result_record = Results(
        firmware_id=firmware.id,
        date_tested=date_tested,
        component=component,
        feature=feature,
        scenarioID=scenario_id,
        result=result,
        debug=debug,
    )
    # the database is being locked due to multi-threading situations where a 
    session.add(result_record)
    session.commit()