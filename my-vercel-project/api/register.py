from flask import Flask, request, jsonify
from supabase import create_client
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

supabase = create_client(os.getenv('SUPABASE_URL'), os.getenv('SUPABASE_KEY'))

@app.route('/api/register', methods=['POST'])
def register():
    data = request.json
    supabase.table('akun_user').insert(data).execute()
    return jsonify({"message": "Registrasi berhasil!"})

if __name__ == '__main__':
    app.run()
