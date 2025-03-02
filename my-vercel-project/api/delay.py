from flask import Flask, request, jsonify
from supabase import create_client
import os
from dotenv import load_dotenv
import time
from datetime import datetime
import pywhatkit as kit

app = Flask(__name__)
load_dotenv()

supabase = create_client(os.getenv('SUPABASE_URL'), os.getenv('SUPABASE_KEY'))

@app.route('/api/delay_chat', methods=['POST'])
def delay_chat():
    data = request.json
    phone = data['phone']
    message = data['message']
    schedule_time = datetime.strptime(data['scheduleTime'], '%Y-%m-%dT%H:%M')

    delay = (schedule_time - datetime.now()).total_seconds()
    if delay > 0:
        time.sleep(delay)
        kit.sendwhatmsg_instantly(phone, message, wait_time=10)
        return jsonify({"message": "Pesan terkirim sesuai jadwal!"})
    else:
        return jsonify({"message": "Waktu tidak valid!"})

if __name__ == '__main__':
    app.run()
