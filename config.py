
auth0_config = {
    'AUTH0_DOMAIN': 'ivancheng.eu.auth0.com',
    'ALGORITHMS': ['RS256'],
    'API_AUDIENCE': 'player'
}


jwt_tokens = {
    "Concert_Assistant": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImVMVWRJVFVwVk1oNTRPOUg4cHhFXyJ9.eyJpc3MiOiJodHRwczovL2l2YW5jaGVuZy5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVkNzc0MTY2NDg5NWEwMDE5OWEyNDBmIiwiYXVkIjoicGxheWVyIiwiaWF0IjoxNTkxMjAwNDE0LCJleHAiOjE1OTEyODY4MTQsImF6cCI6IkZvbHZlN3hlM09KMEYzeXZ6SUJHc2l2cWJmSU5KQWE3Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6Y29uY2VydHMiLCJnZXQ6cGxheWVycyJdfQ.mJLHm2e8OA5vI6CqVZAbeI_rIotXTb7pLB-BUUj2MyAPxQOpZki1txXaIbelUdoMLZXvn5R0mdbZnpcf8rQfeS4jEq1o4vMoK5tGtoHjNcf_ULWHVGKoo5Ube3igO-BVkBjn7j_VzZpn8-riM9cDNBGcZU9WYl_p5Lstf5R55y_-T98HujdPJSG7TSUbzUPYqM1gziCO7cmoVF5gN9cPr-Z6yYGoZ5JEkZ5Q_exRLCtz2u4JuPRQBTHkHWDrgfnCtUH5HupSu6Kz4uNykcJ2myQYQ5G4ONI7JnJWvXgi69ZSF067aK7jPUIoQY6DhQV8UCPUp_cOzU-fMK14Z_d2AA",
    "Concert_Fixer": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImVMVWRJVFVwVk1oNTRPOUg4cHhFXyJ9.eyJpc3MiOiJodHRwczovL2l2YW5jaGVuZy5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVkNzZhZTY2NDg5NWEwMDE5OWExOGE0IiwiYXVkIjoicGxheWVyIiwiaWF0IjoxNTkxMjAwMzY3LCJleHAiOjE1OTEyODY3NjcsImF6cCI6IkZvbHZlN3hlM09KMEYzeXZ6SUJHc2l2cWJmSU5KQWE3Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6cGxheWVycyIsImdldDpjb25jZXJ0cyIsImdldDpwbGF5ZXJzIiwicGF0Y2g6cGxheWVycyIsInBvc3Q6cGxheWVycyJdfQ.HYg-CHRPhwchJlZYxSn9oQnD9xN9GI8qmGo8MLgExbF3UKJIh9N5HfdI0gGiZMZe2xRU3QdkL23sQW-BPs5uHMtXYpnGFMIzzlUXDvPmsU-JdtY369k-w9wsxNqdqDmjncn68-giSuN_jUU_uyyFjx9rZAJZMwArSI3tnsLLAMmX5FfL6AYdOog4kHZeIB8EcuyLA2LRAfFVOzivBwb-_L1B_d5eRhlqN-Ek87A-3mSAjf91F03fRjjxJy6_lHbVdecjETzZjGS6zo6yZltTgHobDiw3GC7YjRan_dpHh4MCS0UyiPvupHmixU9kUjf6OgeENPUTRE9x04rEgMnfgA",
    "Concert_Manager": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImVMVWRJVFVwVk1oNTRPOUg4cHhFXyJ9.eyJpc3MiOiJodHRwczovL2l2YW5jaGVuZy5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVkNjI2NzY1NDEwNmUwYjk3ZGVjOTg1IiwiYXVkIjoicGxheWVyIiwiaWF0IjoxNTkxMjAwMzE1LCJleHAiOjE1OTEyODY3MTUsImF6cCI6IkZvbHZlN3hlM09KMEYzeXZ6SUJHc2l2cWJmSU5KQWE3Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6Y29uY2VydHMiLCJkZWxldGU6cGxheWVycyIsImdldDpjb25jZXJ0cyIsImdldDpwbGF5ZXJzIiwicGF0Y2g6Y29uY2VydHMiLCJwYXRjaDpwbGF5ZXJzIiwicG9zdDpjb25jZXJ0cyIsInBvc3Q6cGxheWVycyJdfQ.hGt4M4gtORabkseUso8RhJ2BPK8oJHYDtKUOH4LrcBGW3xdPoAzxAO1YXBdFOTIZ_NnwOQVISTzKkF4Rx107dznsHjlL88dsFWzgUpRJ2XG_E534rSeNflCkfWZXswaU3LkSfqCiZVj-1fLD_GH0Z8FV5MpQE05GDuLzaQvRwJM8KIxWIYG6qItoy_6iLNazzMptAProzc-5IoO8UcSHsULhwGg3_Mb9jsUkmUCjZ_tK5J7019JjKFE5XqrWBz73OtUn-1U7bYkNOyUuVK8nTtz1MEJAIzJS6IAJOzH9XQnbp4osi3cFZI4MSynq-zQBq2EwChd-1KlqTleU50oAHg"
}

