import pathlib
import dropbox
from dropbox.exceptions import AuthError


class DBX:
    def __init__(self):
        """Create a connection to Dropbox."""

        try:
            self.dbx = dropbox.Dropbox(app_key='ew5usmbbcsxa8ab', app_secret='xa1he8qdkggfgs3', oauth2_refresh_token='n6Lf0P_2gGMAAAAAAAAAAVy0uA_mBe0xx7TkTM8AcHcA4PwJjUBKw0FUgWV83psE')
        except AuthError as e:
            print('Error connecting to Dropbox with access token: ' + str(e))


    def upload_file(self, local_path, file_name, dropbox_dir, verbose=1):
        """Upload a file from the local machine to a path in the Dropbox app directory.

        Args:
            local_path (str): The path to the local file.
            local_file (str): The name of the local file.
            dropbox_file_path (str): The path to the file in the Dropbox app directory.

        Example:
            dropbox_upload_file('.', 'test.csv', '/stuff/test.csv')

        Returns:
            meta: The Dropbox file metadata.
        """

        try:
            local_file_path = pathlib.Path(local_path) / file_name
            dropbox_file_path = f'/{dropbox_dir}/{file_name}'
            with local_file_path.open("rb") as f:
                meta = self.dbx.files_upload(f.read(), dropbox_file_path, mode=dropbox.files.WriteMode("overwrite"))
                return meta
        except Exception as e:
            if verbose:
                print('Error uploading file to Dropbox: ' + str(e))
            raise


    def delete_file(self, path, verbose=1):
        """Delete a file given in a path from Dropbox in the Apps directory."""
        try:
            return self.dbx.files_delete_v2(path)
        except Exception as e:
            if verbose:
                print('Error deletting a file from Dropbox: ' + str(e))
            raise


    def get_metadata(self, file_id, verbose=1):
        """Return a metadata of a given file path."""

        try:
            return self.dbx.files_get_metadata(file_id)
        except Exception as e:
            if verbose:
                print('Error getting a metadata from Dropbox: ' + str(e))
            raise


    def count_occurences(self, file_name, dropbox_dir, verbose=1):
        """Return an amount of files in a given Dropbox folder path in the Apps directory."""

        try:
            files = self.dbx.files_list_folder('/' + dropbox_dir).entries
            file_names = [file.name for file in files]
            return file_names.count(file_name)
        except Exception as e:
            if verbose:
                print('Error getting list of files from Dropbox: ' + str(e))
            raise


dbx = DBX()

# print(dbx.upload_file('.', 'default.jpg', '/images'))
# print(dbx.count_occurences('default.jpg', 'images'))
# print(dbx.delete_file('/images/default.jpg'))


