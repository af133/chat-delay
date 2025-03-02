from flask import Flask, request, jsonify
from supabase import create_client
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

supabase = create_client(os.getenv('SUPABASE_URL'), os.getenv('SUPABASE_KEY'))

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    user = supabase.table('akun_user').select('*').eq('username', data['username']).eq('password', data['password']).execute()
    return jsonify({"success": bool(user.data)})

if __name__ == '__main__':
    app.run()
