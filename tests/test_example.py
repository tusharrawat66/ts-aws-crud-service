from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from src.api.country import router
from src.schema.Countryschema import CountryRead

client = TestClient(router)

@patch('src.api.country.dynamodb_handler')
@patch('src.api.country.config.get')
def test_get_countries(config_get_mock, dynamodb_mock):
    # Mock the DynamoDB table
    dynamodb_mock.return_value = MagicMock()
    # Mock the config get method
    config_get_mock.return_value = "TABLE_NAME"

    # Mock data to be returned by DynamoDB
    mock_items = [
        {"id": 1, "country": "USA", "capital": "Washington", "continent": "North America", "population": 300000000, "code": 1},
        {"id": 2, "country": "Canada", "capital": "Ottawa", "continent": "North America", "population": 37000000, "code": 2}
    ]
    dynamodb_mock.return_value.scan.return_value = {"Items": mock_items}

    response = client.get("/api/")
    assert response.status_code == 200

    # Check if the response data matches the expected format
    response_countries = response.json()
    assert len(response_countries) == 2

    # Additional checks can be performed based on the specific data returned
    print(f"RESPONSE: {response_countries}")
    assert response_countries[0]["country"] == "USA"
    assert response_countries[1]["capital"] == "Ottawa"

    # Additional assertions for mock calls if needed
    dynamodb_mock.return_value.scan.assert_called_once()
    config_get_mock.assert_called_once_with("TABLE_NAME")
