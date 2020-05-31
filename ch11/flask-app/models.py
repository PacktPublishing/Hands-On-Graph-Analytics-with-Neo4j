from datetime import date, datetime
from neomodel import (
    config,
    StructuredNode, StructuredRel,
    DateProperty, DateTimeProperty,
    StringProperty, EmailProperty,
    RelationshipFrom, RelationshipTo,
)
import flask_login

config.DATABASE_URL = 'bolt://neo4j:<YOUR_PASSWORD>@localhost:7687'  # default


class ContributedTo(StructuredRel):
    contribution_date = DateTimeProperty(required=True)


class User(StructuredNode, flask_login.UserMixin):
    login = StringProperty(required=True, primary=True)
    password = StringProperty(required=True)
    email = EmailProperty()
    birth_date = DateProperty()
    owned_repositories = RelationshipTo("Repository", "OWNS")
    contributed_repositories = RelationshipTo(
        "Repository", "CONTRIBUTED_TO",
        model=ContributedTo
    )
    recommended_repositories = RelationshipTo("Repository", "RECO")

    def get_id(self):
        return self.login


class Repository(StructuredNode):
    name = StringProperty()
    owner = RelationshipFrom(User, "OWNS")
    contributors = RelationshipFrom(
        User, "CONTRIBUTED_TO",
        model=ContributedTo
    )


if __name__ == '__main__':
    # Creating some toys users
    users = User.get_or_create(
        dict(
            login="me",
            password="<3Graphs",
            email="me@internet.com",
            birth_date=date(2000, 1, 1),
        ),
        dict(
            login="you",
            password="12345",
        ),
        dict(
            login="trinity",
            password="theMatrix",
        ),
    )

    # fetching existing users
    users = User.nodes.all()
    for u in users:
        print(u.login, u.email, u.birth_date)

    # creating toys repository
    repos = Repository.get_or_create(
        dict(name="hogan"),
        dict(name="flask4j"),
        dict(name="neopi"),
    )

    # connect all users to first repo
    for u in users:
        repos[0].contributors.connect(u, {"contribution_date": datetime.now()})

    repos[0].owner.connect(users[0])

    # fetching repos
    repos = Repository.nodes.all()
    for r in repos:
        print(r.name, r.contributors.all())

    # find users contributing to "hogan" and having a non null birth_date
    users = Repository.nodes.get(
        name="hogan"
    ).contributors.filter(birth_date__isnull=False)
    for u in users:
        print(u)
