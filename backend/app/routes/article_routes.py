from flask import Blueprint, request, jsonify
from app.models.article import Article
from app.validators.article_validator import validate_article

article_bp = Blueprint('article', __name__)

def serialize_article(article):
    return {
        "id": article.id,
        "title": article.title,
        "content": article.content,
        "category": article.category,
        "status": article.status,
        "created_date": article.created_date,
        "updated_date": article.updated_date
    }

@article_bp.route('/article/', methods=['POST'])
def create_article():
    data = request.get_json()
    errors = validate_article(data)
    if errors:
        return jsonify({"errors": errors}), 400
    
    try:
        article_id = Article.create(
            data['title'], 
            data['content'], 
            data['category'], 
            data['status']
        )
        return jsonify({"id": article_id, "message": "Article created successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@article_bp.route('/article/<int:limit>/<int:offset>', methods=['GET'])
def get_articles(limit, offset):
    try:
        articles = Article.get_all(limit, offset)
        return jsonify([serialize_article(a) for a in articles]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@article_bp.route('/article/<int:article_id>', methods=['GET'])
def get_article(article_id):
    try:
        article = Article.get_by_id(article_id)
        if article:
            return jsonify(serialize_article(article)), 200
        return jsonify({"error": "Article not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@article_bp.route('/article/<int:article_id>', methods=['PUT', 'PATCH', 'POST'])
def update_article(article_id):
    data = request.get_json()
    errors = validate_article(data)
    if errors:
        return jsonify({"errors": errors}), 400
    
    try:
        success = Article.update(
            article_id,
            data['title'], 
            data['content'], 
            data['category'], 
            data['status']
        )
        if success:
            return jsonify({"message": "Article updated successfully"}), 200
        return jsonify({"error": "Article not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@article_bp.route('/article/<int:article_id>', methods=['DELETE'])
def delete_article(article_id):
    try:
        success = Article.delete(article_id)
        if success:
            return jsonify({"message": "Article deleted successfully"}), 200
        return jsonify({"error": "Article not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
