from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_all_resource_data():
    response = client.get("/people/?page=1")
    assert response.status_code == 200
    assert response.json()["count"] == 82
    assert response.json()["previous"] == None
    assert response.json()["next"] == 2

    response = client.get("/people/?search=vader")
    assert response.status_code == 200
    assert response.json()["results"][0]["name"] == "Darth Vader"
    

def test_get_person():
    response = client.get("/person/1")
    assert response.status_code == 200

    data = response.json()
    assert data["name"] == "Luke Skywalker"
    assert data["height"] == "172"
    assert data["mass"] == "77"

def test_get_person_films():
    response = client.get("/person/1/films")
    assert response.status_code == 200
    assert len(response.json()) == 4

def test_get_person_vehicles():
    response = client.get("/person/1/vehicles")
    assert response.status_code == 200
    assert len(response.json()) == 2

def test_get_person_starships():
    response = client.get("/person/1/starships")
    assert response.status_code == 200
    assert len(response.json()) == 2

    response = client.get("/person/2/starships")
    assert response.status_code == 200
    assert len(response.json()) == 0


def test_get_film():
    response = client.get("/film/2")
    assert response.status_code == 200

    data = response.json()
    assert data["title"] == "The Empire Strikes Back"
    assert data["episode_id"] == 5
    assert data["release_date"] == "1980-05-17"

def test_get_film_characters():
    response = client.get("/film/2/characters")
    assert response.status_code == 200
    assert len(response.json()) == 16

def test_get_film_planets():
    response = client.get("/film/2/planets")
    assert response.status_code == 200
    assert len(response.json()) == 4

def test_get_film_species():
    response = client.get("/film/2/species")
    assert response.status_code == 200
    assert len(response.json()) == 5


def test_get_starship():
    response = client.get("/starship/9")
    assert response.status_code == 200

    data = response.json()
    assert data["name"] == "Death Star"

def test_get_starship_pilots():
    response = client.get("/starship/9/pilots")
    assert response.status_code == 200
    assert len(response.json()) == 0

def test_get_starship_films():
    response = client.get("/starship/9/films")
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_get_vehicle():
    response = client.get("/vehicle/1")
    assert response.status_code != 200

    response = client.get("/vehicle/18")
    assert response.status_code == 200

    data = response.json()
    assert data["name"] == "AT-AT"
    assert data["manufacturer"] == "Kuat Drive Yards, Imperial Department of Military Research"

def test_get_vehicle_pilots():
    response = client.get("/vehicle/18/pilots")
    assert response.status_code == 200
    assert len(response.json()) == 0

def test_get_vehicle_films():
    response = client.get("/vehicle/18/films")
    assert response.status_code == 200
    assert len(response.json()) == 2


def test_get_specie():
    response = client.get("/specie/2")
    assert response.status_code == 200

    data = response.json()
    assert data["name"] == "Droid"

def test_get_specie_people():
    response = client.get("/specie/2/people")
    assert response.status_code == 200
    assert len(response.json()) == 4


def test_get_planet():
    response = client.get("/planet/0")
    assert response.status_code != 200

def test_get_planet_residents():
    response = client.get("/planet/2/residents")
    assert response.status_code == 200
    assert len(response.json()) == 3

def test_get_planet_films():
    response = client.get("/planet/2/films")
    assert response.status_code == 200
    assert len(response.json()) == 2