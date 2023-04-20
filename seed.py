from app import app
from models import db, Production, CastMember

print("========Seeding into the database🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱============")
with app.app_context():
    Production.query.delete()
    productions = []

    p1 = Production(title="Hamlet", genre="Drana", budget=200000, image="sadgajksdAJKS.jpg", director="Bill",
                    description="THe tragedy of the bridge", ongoing=True,)
    productions.append(p1)

    p2 = Production(title="SpiderMan", genre="Action", budget=8520000, image="sadgajksdAJKS.jpg", director="Kude",
                    description="THe tragedy of the bridge", ongoing=False,)

    productions.append(p2)

    p3 = Production(title="Harry Potter", genre="Action", budget=80000, image="sadgajksdAJKS.jpg", director="Kude",
                    description="The books are not reading themselves ", ongoing=True,)
    productions.append(p3)

    p4 = Production(title="Cmaran", genre="Action", budget=80000, image="sadgajksdAJKS.jpg", director="Kude",
                    description=" bridge along the waves", ongoing=False,)
    productions.append(p4)

    db.session.add_all(productions)
    db.session.commit()

# cast memebers
    CastMember.query.delete()
    cast_members = []

    c1 = CastMember(name="Hamlet", role="King", production_id=p1.id)
    cast_members.append(c1)
    c2 = CastMember(name="Hamlet", role="King", production_id=p2.id)
    cast_members.append(c2)
    c3 = CastMember(name="Hamlet", role="King", production_id=p3.id)
    cast_members.append(c3)
    c4 = CastMember(name="Hamlet", role="King", production_id=p4.id)
    cast_members.append(c4)

    db.session.add_all(cast_members)
    db.session.commit()

    # pthon seed.py
    # flask shell
    print("==========Done Seeding 🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱============")
