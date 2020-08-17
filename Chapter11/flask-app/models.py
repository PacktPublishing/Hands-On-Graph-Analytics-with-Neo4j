from datetime import date, datetime, timedelta
from neomodel import (
    config,
    StructuredNode, StructuredRel,
    DateProperty, DateTimeProperty,
    StringProperty, EmailProperty,
    RelationshipFrom, RelationshipTo,
)
import flask_login

config.DATABASE_URL = 'bolt://neo4j:admin@localhost:7687'  # default


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
    print("*** CREATING TEST USERS")
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
        print("USER: login =", u.login, ", email =", u.email, ", birth_date =", u.birth_date)

    # creating toys repository
    print("*** CREATING TEST REPOSITORIES AND ADDING CONTRIBUTORS")
    repos = Repository.get_or_create(
        dict(name="hogan"),
        dict(name="flask4j"),
        dict(name="neopi"),
    )

    # connect all users to first repo
    # with different contribution dates
    start_date = datetime(2020, 8, 10, 14)
    for k, u in enumerate(users):
        repos[0].contributors.connect(u, {"contribution_date": start_date + timedelta(hours=k, minutes=1)})

    repos[0].owner.connect(users[0])

    # fetching repos
    repos = Repository.nodes.all()
    for r in repos:
        print("REPOSITORY: name =", r.name, ", contributors =", r.contributors.all())

    # find users contributing to "hogan" and having a non null birth_date
    print("*** MATCHING USERS contributing to Repository named 'hogan', whose birth_date is not null")
    users = Repository.nodes.get(
        name="hogan"
    ).contributors.filter(birth_date__isnull=False)
    for u in users:
        print("Marching user:", u)


    # find repositories
    print("*** MATCHING USERS contributing to Repository named 'hogan' before 2020-08-10 at 3pm")
    users = Repository.nodes.get().contributors.match(
        contribution_date__gt=datetime(2020, 8, 10, 15, 0)
    ).all()
    for u in users:
        print("Marching user:", u)

"""
Cypher equivalent of the last query:
MATCH (u:User)-[r:CONTRIBUTED_TO]->(:Repository {name: "hogan"}) 
// contribution_date is saved as a floating point timestamp, transform to datetime
WITH u, DATETIME({epochSeconds: toInteger(r.contribution_date)}) as dt
WHERE dt >= DATETIME("2020-08-10T15:00:00") 
RETURN u
"""
