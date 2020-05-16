async def test_healthcheck(client):
    resp = await client.get('/healthcheck')
    assert resp.status == 200
    data = await resp.json()
    assert data["status"] == 'success'