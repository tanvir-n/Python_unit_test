import uuid


def fake_primary_external_api(message):
    """Mock the primary API"""
    result = {"api": "1"}
    if message["api_key"] != "alice":
        result["status"] = "403"
    else:
        result.update(
            {
                "recipient": message["phone"],
                "status": "SENT",
            }
        )
    return result


def fake_secondary_external_api(message):
    """Mock the secondary API"""
    result = {"api": "2"}
    if message["auth_key"] != "bob":
        result["status"] = "403"
    else:
        result.update(
            {
                "id": uuid.uuid4(),
                "status": "OK",
            }
        )
    return result
