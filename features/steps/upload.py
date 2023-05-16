from behave import *
from dropbox_api import dbx


@given('I upload file "{file_name}" in "{dir}"')
def upload_file(context, file_name, dir):
    dbx.upload_file('.', file_name, dir)

@when('I upload second time file "{file_name}" in "{dir}"')
def upload_file(context, file_name, dir):
    dbx.upload_file('.', file_name, dir)

@then('there is only one file "{file_name}" in "{dir}"')
def only_one_file(context, file_name, dir):
    print(dbx.count_occurences(file_name, dir) == 1)
