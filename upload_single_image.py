import os
import base64
import requests

# Konfiguration
GITHUB_USERNAME = "rukgithub"
REPO_NAME = "single-image-test"
IMAGE_PATH = r"C:\Users\ruk\Downloads\billeder\cyb.jpg"

# GitHub token fra miljøvariabel
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")


def main():
    print("\n=== Simple Image Upload Test ===")

    # Verificer token
    if not GITHUB_TOKEN:
        print("✗ Error: GitHub token not found!")
        return

    print(f"\nTesting with image: {IMAGE_PATH}")

    # Test file exists
    if not os.path.exists(IMAGE_PATH):
        print("✗ Error: Image file not found!")
        return

    # Læs billedfilen
    try:
        with open(IMAGE_PATH, "rb") as image_file:
            content = image_file.read()
            print("✓ Successfully read image file")
    except Exception as e:
        print(f"✗ Error reading image: {e}")
        return

    # Upload til GitHub
    url = f"https://api.github.com/repos/{GITHUB_USERNAME}/{REPO_NAME}/contents/test-image.jpg"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }

    # Encode image
    encoded_content = base64.b64encode(content).decode('utf-8')
    print("✓ Successfully encoded image")

    data = {
        "message": "Add test image",
        "content": encoded_content
    }

    print("\nUploading to GitHub...")
    response = requests.put(url, headers=headers, json=data)

    if response.status_code in [200, 201]:
        print("✓ Successfully uploaded image!")
        print(f"\nYou can see the image at:")
        print(f"https://github.com/{GITHUB_USERNAME}/{REPO_NAME}/blob/main/test-image.jpg")
    else:
        print(f"✗ Upload failed with status {response.status_code}")
        print(f"Error message: {response.json().get('message', 'Unknown error')}")


if __name__ == "__main__":
    main()