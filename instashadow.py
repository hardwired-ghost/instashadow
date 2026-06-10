import sys
import os
from instagrapi import Client
from dotenv import load_dotenv

load_dotenv()

SESSION_FILE = "ig_session.json"
SOCK_PUPPET_USER = os.getenv("IG_USER")
SOCK_PUPPET_PASS = os.getenv("IG_PASS")

if not SOCK_PUPPET_USER or not SOCK_PUPPET_PASS:
    print("[-] Missing credentials. Set IG_USER and IG_PASS in a .env file.")
    sys.exit(1)
print(".::HΔRDWIRΞD ∇ GH0ST::.")
print("")

def login_with_session(cl):
    if os.path.exists(SESSION_FILE):
        try:
            cl.load_settings(SESSION_FILE)
            cl.login(SOCK_PUPPET_USER, SOCK_PUPPET_PASS)
            print("[+] Session restored successfully!")
            return True
        except Exception as e:
            print(f"[!] Saved session failed, trying fresh login: {e}")

    try:
        cl.login(SOCK_PUPPET_USER, SOCK_PUPPET_PASS)
        cl.dump_settings(SESSION_FILE)
        print("[+] Fresh login successful, session saved!")
        return True
    except Exception as e:
        print(f"[-] Login failed: {e}")
        return False


def extract_instagram_data(target_username):
    cl = Client()
    cl.set_country("US")
    cl.set_locale("en_US")
    cl.set_timezone_offset(-14400)

    print("[*] Initializing login...")
    if not login_with_session(cl):
        return

    try:
        target_username = target_username.lstrip("@").strip()

        user_by_username = cl.user_info_by_username_v1(target_username)
        target_user_id = user_by_username.pk

        user = cl.user_info_v1(target_user_id)

        print("\n" + "=" * 26)
        print("INSTAGRAM PROFILE")
        print("=" * 26)
        print(f"Username        : {user.username}")
        print(f"Full name       : {user.full_name}")
        print(f"User ID         : {target_user_id}")
        print(f"Private account : {'Yes' if user.is_private else 'No'}")
        print(f"Followers       : {user.follower_count}")
        print(f"Following       : {user.following_count}")
        print(f"Biography       : {user.biography}")
        print(f"External URL    : {user.external_url}")

        print("\n--- PUBLIC BUSINESS / CREATOR DETAILS ---")
        print(f"Public email    : {user.public_email or 'Not visible / Not provided'}")
        print(
            f"Phone           : "
            f"{user.public_phone_country_code or ''} "
            f"{user.public_phone_number or 'Not visible'}"
        )
        print(f"Category        : {user.category}")
        print(f"City / ZIP      : {user.city_name} / {user.zip}")
        print("=" * 26)

    except Exception as e:
        print(f"[-] Data extraction failed: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <instagram_username>")
        sys.exit(1)

    extract_instagram_data(sys.argv[1])
