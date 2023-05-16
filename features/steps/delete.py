from behave import *
from dropbox.exceptions import ApiError
from dropbox_api import dbx


@when('I delete file "{file_name}" in "{dir}"')
def delete_file(context, file_name, dir):
    dbx.delete_file(f'/{dir}/{file_name}')

@then('there is no "{file_name}" in "{dir}"')
def no_file(context, file_name, dir):
    try:
        dbx.delete_file(f'/{dir}/{file_name}', verbose=0)
        print(False)
    except ApiError as e:
        if e.error.get_path_lookup().is_not_found():
            print(True)
        else:
            print('Some problems with file deleting: ' + str(e))
        