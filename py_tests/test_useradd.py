async def test_useradd(client):
    resp = await client.get('/useradd')
    assert resp.status == 200
