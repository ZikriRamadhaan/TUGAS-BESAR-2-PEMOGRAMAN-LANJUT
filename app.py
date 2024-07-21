print("\n=== NOMOR 5 ===")

import logging
from flask import Flask, jsonify, request
from models import get_buku_by_id, save_buku
from buku import Buku

app = Flask(__name__)

# Setup logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.errorhandler(404)
def not_found(error):
    logger.error(f"Error 404: {error}")
    return jsonify({"error": "Not Found"}), 404

@app.errorhandler(500)
def internal_error(error):
    logger.error(f"Error 500: {error}")
    return jsonify({"error": "Internal Server Error"}), 500

@app.route('/buku/<int:buku_id>', methods=['GET'])
def get_buku(buku_id):
    print("\n=== NOMOR 6 ===")
    buku = get_buku_by_id(buku_id)
    if buku:
        return jsonify({
            "judul": buku.judul,
            "penulis": buku.penulis,
            "penerbit": buku.penerbit,
            "tahun_terbit": buku.tahun_terbit,
            "konten": buku.konten,
            "iktsar": buku.iktsar
        })
    else:
        return jsonify({"error": "Buku tidak ditemukan"}), 404

@app.route('/buku', methods=['POST'])
def add_buku():
    print("\n=== NOMOR 7 ===")
    data = request.json
    buku = Buku(
        judul=data['judul'],
        penulis=data['penulis'],
        konten=data['konten']
    )
    buku.penerbit = data.get('penerbit')
    buku.tahun_terbit = data.get('tahun_terbit')
    buku.iktsar = data.get('iktsar')
    
    save_buku(buku)
    return jsonify({"message": "Buku berhasil ditambahkan"}), 201

if __name__ == '__main__':
    app.run(debug=True)
