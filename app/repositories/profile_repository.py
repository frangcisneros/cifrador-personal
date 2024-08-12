from typing import List, Type
from app.models import Profile
from app import db


class ProfileRepository:
    """
    Clase que representa un repositorio de perfiles.
    Métodos:
    - save(profile: Profile) -> Profile: Guarda un perfil en la base de datos y lo devuelve.
    - update(profile: Profile, id: int) -> Profile: Actualiza un perfil existente en la base de datos y lo devuelve.
    - delete(profile: Profile) -> None: Elimina un perfil de la base de datos.
    - all() -> List[Profile]: Devuelve una lista de todos los perfiles en la base de datos.
    - find(id: int) -> Profile: Busca un perfil por su ID en la base de datos y lo devuelve.
    """

    def save(self, profile: Profile) -> Profile:
        db.session.add(profile)
        db.session.commit()
        return profile

    def update(self, profile: Profile, id: int) -> Profile:
        entity = self.find(id)
        entity.name = profile.name
        db.session.add(entity)
        db.session.commit()
        return entity

    def delete(self, profile: Profile) -> None:
        db.session.delete(profile)
        db.session.commit()

    def all(self) -> List[Profile]:
        users = db.session.query(Profile).all()
        return users

    def find(self, id: int) -> Profile:
        if id is None or id == 0:
            return None
        try:
            return db.session.query(Profile).filter(Profile.id == id).one()
        except:
            return None
