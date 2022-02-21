from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///user.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    def __repr__(self):
        return f'<User(name={self.name}, fullname={self.fullname}, nickname={self.nickname}'


if __name__ == '__main__':
    Base.metadata.create_all(engine)

    # Add single entry
    graham_user = User(name='Graham', fullname='Graham Morby', nickname='Grey')
    session.add(graham_user)
    session.commit()

    # Add multiple at once
    session.add_all([
        User(name='Grace', fullname='Grace Hopper', nickname='Pioneer'),
        User(name='Alan', fullname='Alan Turing', nickname='Computer Scientist'),
        User(name='Katherine', fullname='Katherine Johnson', nickname='')
        ])
    session.commit()

