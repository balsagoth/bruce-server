import falcon


import falcon
from falcon_auth import FalconAuthMiddleware, BasicAuthBackend, TokenAuthBackend
# https://github.com/loanzen/falcon-auth


def user_loader(username, password):
    return {"username": username}


auth_backend = BasicAuthBackend(user_loader)
auth_middleware = FalconAuthMiddleware(
    auth_backend, exempt_routes=["/exempt"], exempt_methods=["HEAD"]
)

# auth = {"auth_disabled": True}


class AppsResource:
    auth = {"backend": TokenAuthBackend(user_loader), "exempt_methods": ["GET", "HEAD"]}

    def on_get(self, req, resp):
        """Handles GET requests."""

        quote = {
            "quote": (
                "I've always been more interested in the future than in the past."
            ),
            "author": "Grace Hopper",
        }

        resp.media = quote

    def on_post(self, req, resp):
        """Handles POST requests."""

        user = req.context["user"]
        resp.body = f"User Found: {user['username']}"


api = falcon.API(middleware=[auth_middleware])
api.add_route("/apps", AppsResource())
