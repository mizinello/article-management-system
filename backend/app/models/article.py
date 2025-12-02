from datetime import datetime
from app.database.db import db  # import db dari database.py

class Article(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    created_date = db.Column(db.DateTime, default=datetime.utcnow)
    updated_date = db.Column(db.DateTime, onupdate=datetime.utcnow)

    @staticmethod
    def create(title, content, category, status):
        article = Article(
            title=title,
            content=content,
            category=category,
            status=status
        )
        db.session.add(article)
        db.session.commit()
        return article.id

    @staticmethod
    def get_all(limit=10, offset=0):
        return Article.query.offset(offset).limit(limit).all()

    @staticmethod
    def get_by_id(article_id):
        return Article.query.get(article_id)

    @staticmethod
    def update(article_id, title, content, category, status):
        article = Article.query.get(article_id)
        if not article:
            return False
        article.title = title
        article.content = content
        article.category = category
        article.status = status
        db.session.commit()
        return True

    @staticmethod
    def delete(article_id):
        article = Article.query.get(article_id)
        if not article:
            return False
        db.session.delete(article)
        db.session.commit()
        return True
