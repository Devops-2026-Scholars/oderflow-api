def test_health_check_without_database(client, monkeypatch):
    # Temporarily hide the database environment variable
    monkeypatch.delenv("DATABASE_URL", raising=False)

    # Execute the client request
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy",
        "database": "disconnected",
        "version": "1.0.0",
    }
