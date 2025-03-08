from routes.flashcard_routes import router as flashcard_router
from routes.flashcard_stack_routes import router as flashcard_stack_router
from routes.users_routes import router as users_router

routers = [users_router, flashcard_router, flashcard_stack_router]
