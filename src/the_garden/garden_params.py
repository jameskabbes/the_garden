git_clone_suffix = '.git'

github_accounts = {

    'iCenter Public':{

        'url_base': 'https://github.com/AmerenICenter',
        'add_to_pythonpath': True,
        'repos': {
            'analytics_packages',
            'aws_connections',
            'aws_credentials',
            'database_connections',
            'dir_ops',
            'ml_pipeline',
            'nanoid',
            'parent_class',
            'py_starter',
            'pypi_builder',
            'real_time_input',
            'repository_generator',
            's3synchrony',
            'smart_documentation',
            'user_profile'
        },
    },

    'iCenter Enterprise':{

        'url_base': 'https://github.ameren.com/iCenter',
        'add_to_pythonpath': False,
        'repos': {
            'data_team',
            'Database-Playground'
        }

    }

}#end github accounts

