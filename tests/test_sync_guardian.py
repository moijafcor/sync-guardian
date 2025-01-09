import unittest
import tempfile
import shutil
import os
from pathlib import Path
import time
from directory_sync import DirectorySync

class TestDirectorySync(unittest.TestCase):
    def setUp(self):
        """Create temporary directories for testing"""
        self.source_dir = Path(tempfile.mkdtemp())
        self.target_dir = Path(tempfile.mkdtemp())
        self.test_files = {}
        self.syncer = DirectorySync(self.source_dir, self.target_dir)

    def tearDown(self):
        """Clean up temporary directories after testing"""
        shutil.rmtree(self.source_dir, ignore_errors=True)
        shutil.rmtree(self.target_dir, ignore_errors=True)

    def create_test_file(self, path, content):
        """Helper to create a test file with specific content"""
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, 'w') as f:
            f.write(content)
        self.test_files[path] = content

    def verify_file_content(self, path, expected_content):
        """Helper to verify file content"""
        with open(path, 'r') as f:
            content = f.read()
        self.assertEqual(content, expected_content)

    def test_basic_sync(self):
        """Test basic file synchronization"""
        # Create test files in source
        self.create_test_file(self.source_dir / "file1.txt", "content1")
        self.create_test_file(self.source_dir / "file2.txt", "content2")

        # Run sync
        self.assertTrue(self.syncer.sync_directories())

        # Verify files exist in target
        self.assertTrue((self.target_dir / "file1.txt").exists())
        self.assertTrue((self.target_dir / "file2.txt").exists())

        # Verify content
        self.verify_file_content(self.target_dir / "file1.txt", "content1")
        self.verify_file_content(self.target_dir / "file2.txt", "content2")

    def test_nested_directories(self):
        """Test synchronization of nested directory structure"""
        # Create nested directory structure
        self.create_test_file(self.source_dir / "dir1" / "file1.txt", "nested1")
        self.create_test_file(self.source_dir / "dir1" / "dir2" / "file2.txt", "nested2")

        # Run sync
        self.assertTrue(self.syncer.sync_directories())

        # Verify structure and contents
        self.assertTrue((self.target_dir / "dir1" / "file1.txt").exists())
        self.assertTrue((self.target_dir / "dir1" / "dir2" / "file2.txt").exists())
        self.verify_file_content(self.target_dir / "dir1" / "file1.txt", "nested1")
        self.verify_file_content(self.target_dir / "dir1" / "dir2" / "file2.txt", "nested2")

    def test_file_updates(self):
        """Test updating existing files"""
        # Create initial file
        test_file = self.source_dir / "update_test.txt"
        self.create_test_file(test_file, "original")

        # First sync
        self.assertTrue(self.syncer.sync_directories())
        self.verify_file_content(self.target_dir / "update_test.txt", "original")

        # Update file and sync again
        time.sleep(0.1)  # Ensure timestamp changes
        self.create_test_file(test_file, "updated")
        self.assertTrue(self.syncer.sync_directories())
        self.verify_file_content(self.target_dir / "update_test.txt", "updated")

    def test_file_deletions(self):
        """Test removal of files that no longer exist in source"""
        # Create files in both directories
        self.create_test_file(self.source_dir / "keep.txt", "keep")
        self.create_test_file(self.target_dir / "remove.txt", "remove")

        # Run sync
        self.assertTrue(self.syncer.sync_directories())

        # Verify only correct files exist
        self.assertTrue((self.target_dir / "keep.txt").exists())
        self.assertFalse((self.target_dir / "remove.txt").exists())

    def test_source_not_found(self):
        """Test handling of non-existent source directory"""
        # Create syncer with non-existent source
        bad_syncer = DirectorySync("/nonexistent/path", self.target_dir)
        self.assertFalse(bad_syncer.sync_directories())

    def test_large_file_sync(self):
        """Test synchronization of larger files"""
        # Create a 1MB file
        large_content = "x" * (1024 * 1024)  # 1MB of data
        self.create_test_file(self.source_dir / "large_file.txt", large_content)

        # Run sync
        self.assertTrue(self.syncer.sync_directories())

        # Verify file
        self.assertTrue((self.target_dir / "large_file.txt").exists())
        self.verify_file_content(self.target_dir / "large_file.txt", large_content)

    def test_file_permissions(self):
        """Test preservation of file permissions"""
        # Create test file
        test_file = self.source_dir / "permissions_test.txt"
        self.create_test_file(test_file, "test")
        
        # Set specific permissions (read-only)
        test_file.chmod(0o444)

        # Run sync
        self.assertTrue(self.syncer.sync_directories())

        # Verify permissions are preserved
        target_file = self.target_dir / "permissions_test.txt"
        self.assertEqual(
            test_file.stat().st_mode & 0o777,
            target_file.stat().st_mode & 0o777
        )

    def test_empty_directory_sync(self):
        """Test synchronization of empty directories"""
        # Create empty directory structure
        (self.source_dir / "empty_dir" / "nested_empty").mkdir(parents=True)

        # Run sync
        self.assertTrue(self.syncer.sync_directories())

        # Verify directories were created
        self.assertTrue((self.target_dir / "empty_dir").is_dir())
        self.assertTrue((self.target_dir / "empty_dir" / "nested_empty").is_dir())

if __name__ == '__main__':
    unittest.main()
