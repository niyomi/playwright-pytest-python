def test_api_get(playwright):
    request = playwright.request.new_context()
    response = request.get("https://jsonplaceholder.typicode.com/posts/1")
    
    assert  response.status == 200
    json_response = response.json()
    assert json_response["id"] == 1
    print(json_response)
    
    request.dispose()
 
def test_api_get_with_headers(playwright):
    # request = playwright.request.new_context()
    # response = request.get("https://reqres.in/api/users?page=2", 
    #                        headers={
    #                           "Accept": "application/json"
    #                            })
    # OR
    request = playwright.request.new_context(
        extra_http_headers= {
            "Accept": "application/json"
        })
    response = request.get("https://reqres.in/api/users?page=2") 
    # above headers will be sent automatically as it was added as part of new_context
    