import sys

sys.path.append('/home/dilshod/PycharmProjects/AdminWebBot/.venv/lib/python3.10/site-packages/')
import uvicorn
from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware
from starlette_admin.contrib.sqla import Admin, ModelView

from db import db
from db.models import User, Category
from web.provider import UsernameAndPasswordProvider

app = Starlette()
db.init()
admin = Admin(db._engine, title="Example: SQLAlchemy",
              base_url='/',
              auth_provider=UsernameAndPasswordProvider(),
              middlewares=[Middleware(SessionMiddleware, secret_key="qewrerthytju4")],
              )

class ExcludeModelView(ModelView):
    exclude_fields_from_create = ["created_at" , 'updated_at']
    exclude_fields_from_list = ["created_at" , 'updated_at']

admin.add_view(ExcludeModelView(User, icon="fas fa-home"))
admin.add_view(ExcludeModelView(Category))

admin.mount_to(app)

