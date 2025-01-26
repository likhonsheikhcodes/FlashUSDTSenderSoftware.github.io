import os
import xml.etree.ElementTree as ET

def parse_sitemap(sitemap_path):
    """Parse sitemap.xml and return a list of URLs"""
    try:
        tree = ET.parse(sitemap_path)
        root = tree.getroot()

        # Extract namespace
        namespace = {"ns": root.tag.split("}")[0].strip("{")}
        urls = []

        for url in root.findall("ns:url", namespace):
            loc = url.find("ns:loc", namespace)
            if loc is not None:
                urls.append(loc.text)

        return urls
    except Exception as e:
        print(f"Error parsing sitemap: {e}")
        return []

def create_folders(urls, base_dir):
    """Create folder structure based on URLs"""
    try:
        for url in urls:
            # Convert URL to folder path
            folder_path = url.replace("https://", "").replace("http://", "").replace("/", os.sep)
            folder_path = os.path.join(base_dir, folder_path)

            # Create the directories if they don't exist
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
                print(f"Created directory: {folder_path}")
            else:
                print(f"Directory already exists: {folder_path}")
    except Exception as e:
        print(f"Error creating folders: {e}")

def main():
    sitemap_path = "sitemap.xml"  # Path to the sitemap.xml
    base_dir = "output"  # Base directory where the folder structure will be created

    # Step 1: Parse the sitemap and get URLs
    urls = parse_sitemap(sitemap_path)

    # Step 2: Create folder structure based on URLs
    if urls:
        create_folders(urls, base_dir)
    else:
        print("No URLs found to create folder structure.")

if __name__ == "__main__":
    main()
