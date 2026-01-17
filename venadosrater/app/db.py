import os
from supabase import create_client, Client

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")

supabase: Client = None

if not url or not key:
    print("WARNING: Supabase URL and Key not found in environment variables. Database features will fail.")
else:
    try:
        supabase = create_client(url, key)
    except Exception as e:
        print(f"ERROR: Failed to initialize Supabase client: {e}")
