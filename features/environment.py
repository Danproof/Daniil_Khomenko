def before_feature(context, feature):
    '''Will be called each time a new feature is being tested'''

    context.browser = context.config.userdata.get('browser', 'edge')
    context.base_url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
    context.expected_url = 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index'
    context.correct_username = 'Admin'
    context.correct_password = 'admin123'