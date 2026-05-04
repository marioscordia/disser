import csv
import urllib.request
import urllib.parse
import json
import time
import ssl

def fetch_apa_citation(item):
    if not item:
        return ""
    
    # encode item for url
    encoded_item = urllib.parse.quote(item)
    url = f"https://api.citeas.org/product/{encoded_item}?email=gybraty@gmail.com"
    
    try:
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, context=ctx) as response:
            data = json.loads(response.read().decode())
            if 'citations' in data:
                for c in data['citations']:
                    if c.get('style_shortname') == 'apa':
                        return c.get('citation', '')
    except Exception as e:
        print(f"[WARN] Failed to fetch APA for {item}: {e}")
    return ""

def normalize_doi(doi):
    if not doi:
        return ""
    doi = doi.strip().lower()
    if doi.startswith("http://doi.org/"):
        return doi[15:]
    if doi.startswith("https://doi.org/"):
        return doi[16:]
    if doi.startswith("doi.org/"):
        return doi[8:]
    return doi

def main():
    sourcelist_file = "ranked list of resources - sourcelist.csv"
    export_file = "second-export.csv"
    
    # 1. Read existing sourcelist
    existing_dois = set()
    existing_titles = set()
    
    with open(sourcelist_file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            doi = normalize_doi(row.get("DOI", ""))
            if doi:
                existing_dois.add(doi)
            title = row.get("Title", "").strip().lower()
            if title:
                existing_titles.add(title)
                
    # 2. Read export file and find new items
    new_items = []
    
    with open(export_file, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            doi = row.get("DOI", "").strip()
            norm_doi = normalize_doi(doi)
            title = row.get("Title", "").strip()
            norm_title = title.lower()
            
            # Check if exists
            exists = False
            if norm_doi and norm_doi in existing_dois:
                exists = True
            elif norm_title and norm_title in existing_titles:
                exists = True
                
            if not exists:
                new_items.append(row)
                
    print(f"Found {len(new_items)} new items to add.")
    
    # 3. Append to sourcelist
    if new_items:
        with open(sourcelist_file, "a", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            
            for item in new_items:
                title = item.get("Title", "")
                authors = item.get("Authors", "")
                year = item.get("Year", "")
                source = item.get("Source title", "")
                doi = item.get("DOI", "")
                abstract = item.get("Abstract", "")
                keywords = item.get("Author Keywords", "")
                link = item.get("Link", "")
                
                # Fetch APA citation using test.txt/index.js logic via API
                query_item = doi if doi else link
                print(f"Fetching APA for: {query_item}")
                apa = fetch_apa_citation(query_item)
                time.sleep(0.5) # rate limit respect
                
                # Format DOI correctly if it exists
                formatted_doi = f"doi.org/{doi}" if doi else ""
                
                # Write row: Database,Article source,Authors,Title,Year,DOI,Short description,Keywords,APA
                database = "Scopus (new export)"
                
                writer.writerow([
                    database,
                    source,
                    authors,
                    title,
                    year,
                    formatted_doi,
                    abstract,
                    keywords,
                    apa
                ])
                print(f"Added: {title}")

if __name__ == "__main__":
    import urllib.parse
    main()
