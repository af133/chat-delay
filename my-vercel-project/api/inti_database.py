import os
from dotenv import load_dotenv
from supabase import create_client

env_path = 'C:/Projek Pribadi/Website/Delay Chat/my-vercel-project/.env'
load_dotenv(env_path)
url = os.getenv('SUPABASE_URL')
key = os.getenv('SUPABASE_KEY')
if not url or not key:
    raise ValueError("SUPABASE_URL atau SUPABASE_KEY tidak ditemukan")
data = create_client(url, key)
def supabase():
    supaBase=data
    return supaBase



