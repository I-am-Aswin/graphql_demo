import unittest
from api import app


class TestRoutes( unittest.TestCase ) :

    def setUp(self):
        self.client = app.test_client()

    def test_list_post( self ):

        query = "query { listPosts { success post { id title } } }"

        # Send the GraphQL query as a POST request
        resp = self.client.post("/graphql", json={"query": query})

        print( resp.get_data() , "\t", resp.get_json())

        self.assertEqual(resp.status_code, 200)
        resp = resp.get_json()
        self.assertTrue(resp["data"]["listPosts"]["success"])
        self.assertIsInstance(resp["data"]["listPosts"]["post"], list)

    
    def test_hello(self):
        resp = self.client.get("hello");

        self.assertEqual(resp.status_code, 200)
        data = resp.get_data()
        self.assertEqual(data, b"First API Hurrayyyy...!")
