import data
import sender_stand_request

def get_kit_body(name):
    body = data.kit_body.copy()
    body["name"] = name
    return body

def positive_assert(kit_body):
    auth_token = sender_stand_request.get_new_user_token(data.user_body)
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == kit_body["name"]

def negative_assert_code_400(kit_body):
    auth_token = sender_stand_request.get_new_user_token(data.user_body)
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert kit_response.status_code == 400

def get_kit_body_empty():
    return {}

def get_kit_body_number_type():
    return {"name": 123}

#Prueba 1
def test_1_character_in_name_and_201_code():
    positive_assert(get_kit_body("a"))

#Prueba 2
def test_511_characters_in_name_and_201_code():
    positive_assert(get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"))

#Prueba 3
def test_0_character_in_name_and_400_code():
    negative_assert_code_400(get_kit_body(""))

#Prueba 4
def test_512_characters_in_name_and_400_code():
    negative_assert_code_400(get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"))

#Prueba 5
def test_symbol_character_in_name_and_201_code():
    positive_assert(get_kit_body("a!\"L&"))

#Prueba 6
def test_spaces_in_name_and_201_code():
    positive_assert(get_kit_body(" A aa m"))

#Prueba 7
def test_numbers_in_name_and_201_code():
    positive_assert(get_kit_body("123"))

#Prueba 8
def test_create_kit_empty_body():
    kit_body = get_kit_body_empty()
    negative_assert_code_400(kit_body)

#Prueba 9
def test_create_kit_number_body():
    kit_body = get_kit_body_number_type()
    negative_assert_code_400(kit_body)

