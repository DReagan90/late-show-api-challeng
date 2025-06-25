from server.app import app, db
from server.models.guest import Guest
from server.models.episode import Episode
from server.models.appearance import Appearance

with app.app_context():
    db.drop_all()
    db.create_all()

    guest1 = Guest(name="Emma Stone", occupation="Actress")
    guest2 = Guest(name="Bill Nye", occupation="Scientist")

    episode1 = Episode(date="2025-06-20", number=1)
    episode2 = Episode(date="2025-06-21", number=2)

    appearance1 = Appearance(guest=guest1, episode=episode1, rating=4)
    appearance2 = Appearance(guest=guest2, episode=episode1, rating=5)

    db.session.add_all([guest1, guest2, episode1, episode2, appearance1, appearance2])
    db.session.commit()
