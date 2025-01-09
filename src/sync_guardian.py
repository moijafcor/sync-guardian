import os
import shutil
import hashlib
import logging
from datetime import datetime
from pathlib import Path
import sys

class DirectorySync:
    def __init__(self, source_dir, target_dir, log_file=None):
        """
        Initialize the DirectorySync with source and target directories
        
        Args:
            source_dir (str): Path to source directory
            target_dir (str): Path to target directory
            log_file (str): Optional path to log file
        """
        self.source_dir = Path(source_dir)
        self.target_dir = Path(target_dir)
        
        # Setup logging
        log_file = log_file or f"sync_log_{datetime.now().strftime('%Y%m%d')}.log"
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler(sys.stdout)
            ]
        )
        self.logger = logging.getLogger(__name__)

    def get_file_hash(self, filepath):
        """Calculate MD5 hash of a file"""
        hash_md5 = hashlib.md5()
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()

    def sync_directories(self):
        """Synchronize the source directory to the target directory"""
        try:
            if not self.source_dir.exists():
                raise FileNotFoundError(f"Source directory {self.source_dir} does not exist")
            
            # Create target directory if it doesn't exist
            self.target_dir.mkdir(parents=True, exist_ok=True)
            
            self.logger.info(f"Starting sync from {self.source_dir} to {self.target_dir}")
            
            # Walk through source directory
            for root, dirs, files in os.walk(self.source_dir):
                # Convert root to Path object
                root_path = Path(root)
                
                # Calculate relative path
                rel_path = root_path.relative_to(self.source_dir)
                target_root = self.target_dir / rel_path
                
                # Create directories in target
                target_root.mkdir(parents=True, exist_ok=True)
                
                # Process files
                for file in files:
                    source_file = root_path / file
                    target_file = target_root / file
                    
                    # Check if target file exists and compare hashes
                    if not target_file.exists() or \
                       self.get_file_hash(source_file) != self.get_file_hash(target_file):
                        self.logger.info(f"Copying {source_file} to {target_file}")
                        shutil.copy2(source_file, target_file)
                
                # Remove extra files in target
                target_files = set(f.name for f in target_root.glob('*') if f.is_file())
                source_files = set(files)
                for extra_file in target_files - source_files:
                    extra_path = target_root / extra_file
                    self.logger.info(f"Removing extra file: {extra_path}")
                    extra_path.unlink()
            
            self.logger.info("Sync completed successfully")
            return True
            
        except Exception as e:
            self.logger.error(f"Error during sync: {str(e)}", exc_info=True)
            return False

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Synchronize two directories")
    parser.add_argument("source", help="Source directory path")
    parser.add_argument("target", help="Target directory path")
    parser.add_argument("--log", help="Log file path", default=None)
    
    args = parser.parse_args()
    
    syncer = DirectorySync(args.source, args.target, args.log)
    success = syncer.sync_directories()
    sys.exit(0 if success else 1)
