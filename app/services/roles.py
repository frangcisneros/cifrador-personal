from app.models import Role, User, UserData
from app import db
from app.services import UserService

user_service = UserService()


def create_admin_role():
    role = Role.query.filter_by(name="admin").first()
    if role:
        pass
    else:
        role = Role()
        role.name = "admin"
        role.description = "Administrador"
        role.save()


def create_user_role():
    role = Role.query.filter_by(name="user").first()
    if role:
        pass
    else:
        role = Role()
        role.name = "user"
        role.description = "Usuario"
        role.save()


def create_admin_user():
    user = User.query.filter_by(username="admin").first()
    if user:
        pass
    else:
        data = UserData()
        data.firstname = "Administrador"
        data.lastname = "Administrador"
        data.address = "Admin Address"
        data.city = "Admin Adress"
        data.country = "Admin Country"
        data.phone = "123456789"

        user = User(data)
        user.email = "admin@gmail.com"
        user.username = "admin"
        user.password = "admin"
        user.role_id = 1

        user_service.save(user)
