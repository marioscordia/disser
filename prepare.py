import os
import shutil
from pathlib import Path
import pymupdf4llm

def process_pdfs():
    all_dir = Path("all")
    prepared_dir = Path("prepared")
    
    # Ensure prepared directory exists
    prepared_dir.mkdir(exist_ok=True)
    
    count = 0
    
    # Find all pdfs in the 'all' directory (recursively)
    for pdf_path in all_dir.rglob("*.pdf"):
        # Get the filename without extension
        pdf_name = pdf_path.stem
        
        # Define the target folder inside prepared/
        target_folder = prepared_dir / pdf_name
        
        # Check if the folder already exists
        if target_folder.exists():
            print(f"Skipping '{pdf_name}' - already exists in prepared/")
            continue
            
        print(f"Processing '{pdf_name}'...")
        # Create the new folder
        target_folder.mkdir()
        
        # Create images directory
        images_dir = target_folder / "images"
        images_dir.mkdir(exist_ok=True)
        
        # Create MD and extract images
        target_md = target_folder / f"{pdf_name}.md"
        try:
            # pymupdf4llm extracts text to markdown, and writes images to the image_path
            # It also automatically updates the image links in the markdown text
            md_text = pymupdf4llm.to_markdown(str(pdf_path), write_images=True, image_path=str(images_dir))
            
            # Save the markdown text
            with open(target_md, "w", encoding="utf-8") as f:
                f.write(md_text)
            print(f"  -> Successfully created MD and extracted images for '{pdf_name}'")
            count += 1
        except Exception as e:
            print(f"  -> Error processing '{pdf_name}': {e}")
            
    print(f"\nDone! Processed {count} new PDFs.")

if __name__ == "__main__":
    process_pdfs()
