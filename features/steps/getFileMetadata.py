from behave import *
from dropbox_api import dbx


@given('I upload "{file_name}" in "{dir}"')
def upload_file(context, file_name, dir):
    context.file_id = dbx.upload_file('.', file_name, dir).id

    
@when('I get metadata of uploaded file')
def get_metadata(context):
    context.file_name = dbx.get_metadata(context.file_id).name


@then('uploaded file has "{file_name}" name')
def compare_names(context, file_name):
    print(file_name == context.file_name)
