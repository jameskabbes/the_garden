envs = { #Envs
    'base':{ #Env
        'python_version': None,
        'mediums': {#Mediums
            'pip': { #Medium
                'installations': { #Installations
                    'pyperclip':    { 'version': None }, #Installation
                    'pandas':       { 'version': None },
                    'winshell':     { 'version': None },
                    'boto3':        { 'version': None }
                    }
            },
            'conda': {
                'installations': { #Installations
                    '-c anaconda sqlite':       { 'version': None }
                }
            }
        }
    },
    'analytics':{
        'python_version': None,
        'mediums': {
            'pip': {
                'installations': {
                    'pyperclip':    { 'version': None },
                    'boto3':        { 'version': None },
                    'fastparquet':  { 'version': None },
                    'teradatasql':  { 'version': None },
                    'winshell':     { 'version': None },
                }
            },
            'conda': {
                'installations': { #Installations
                    'pandas':                       { 'version': None },
                    'numpy':                        { 'version': None },
                    '-c anaconda sqlite':           { 'version': None },
                    '-c conda-forge pyathena':      { 'version': None },
                    '-c anaconda cx_oracle':        { 'version': None },
                    '-c anaconda psycopg2':         { 'version': None },
                    '-c anaconda sqlalchemy':       { 'version': None },
                }
            }
        }
    }
}
