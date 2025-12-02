# MODEL UNTUK MIGRATION

# from app.database.db import db
# from sqlalchemy import CheckConstraint, text

# class PostModel(db.Model):
#     __tablename__ = "posts"

#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(200), nullable=False)
#     content = db.Column(db.Text, nullable=False)
#     category = db.Column(db.String(100), nullable=False)
    
#     created_date = db.Column(
#         db.TIMESTAMP,
#         server_default=text("CURRENT_TIMESTAMP")
#     )
    
#     updated_date = db.Column(
#         db.TIMESTAMP,
#         server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")
#     )
    
#     status = db.Column(db.String(100), nullable=False)

#     __table_args__ = (
#         CheckConstraint("status IN ('publish', 'draft', 'thrash')"),
#     )
