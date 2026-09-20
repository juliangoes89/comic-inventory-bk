from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app import database
from app.main import app
from app.models import Base, Comic, Editorial


def _override_db_session():
    engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(bind=engine)

    database.engine = engine
    database.SessionLocal = TestingSessionLocal

    def override_get_db():
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[database.get_db] = override_get_db
    return TestingSessionLocal


def test_health_check():
    _override_db_session()
    client = TestClient(app)

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
    app.dependency_overrides.clear()


def test_get_comics_returns_list():
    TestingSessionLocal = _override_db_session()
    client = TestClient(app)

    db = TestingSessionLocal()
    editorial = Editorial(nombre="Marvel")
    db.add(editorial)
    db.commit()
    db.refresh(editorial)
    editorial_id = editorial.id

    db.add_all(
        [
            Comic(
                titulo="The Amazing Spider-Man",
                numero="1",
                volumen="Vol. 1",
                id_editorial=editorial_id,
                url="https://example.com/spiderman",
                url_portada="https://example.com/spiderman-cover",
                calificacion=9,
                leido=True,
                anno_publicacion=2024,
            ),
            Comic(
                titulo="Guardians of the Galaxy",
                numero="2",
                volumen="Vol. 2",
                id_editorial=editorial_id,
                url="https://example.com/guardians",
                url_portada="https://example.com/guardians-cover",
                calificacion=8,
                leido=False,
                anno_publicacion=2025,
            ),
        ]
    )
    db.commit()
    db.close()

    response = client.get("/comics")

    assert response.status_code == 200
    payload = response.json()
    assert len(payload) == 2
    assert payload[0]["titulo"] == "The Amazing Spider-Man"
    assert payload[0]["id_editorial"] == editorial_id
    assert payload[0]["leido"] is True
    app.dependency_overrides.clear()


def test_get_editoriales_returns_list():
    TestingSessionLocal = _override_db_session()
    client = TestClient(app)

    db = TestingSessionLocal()
    db.add_all([Editorial(nombre="Marvel"), Editorial(nombre="DC")])
    db.commit()
    db.close()

    response = client.get("/editoriales")

    assert response.status_code == 200
    payload = response.json()
    assert len(payload) == 2
    assert {item["nombre"] for item in payload} == {"Marvel", "DC"}
    app.dependency_overrides.clear()
